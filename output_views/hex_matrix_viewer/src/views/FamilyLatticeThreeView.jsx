import React, { useEffect, useRef } from "react";
import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls.js";
import { SECTORS, BANDS, cylinderPosition, spherePosition, familyLinearIndex } from "../topology/spheroidLattice.js";
import { getFillColor } from "../render/modes.js";

/**
 * @param {'cylinder' | 'sphere'} projection
 * @param {import('../schema/hexSchema.js').HexState[]} cells
 * @param {import('../render/modes.js').RenderMode} renderMode
 */
export default function FamilyLatticeThreeView({ projection, cells, renderMode, selectedId, hoveredId, onSelect, onHover }) {
  const mountRef = useRef(null);
  const rendererRef = useRef(null);
  const sceneRef = useRef(null);
  const cameraRef = useRef(null);
  const controlsRef = useRef(null);
  const meshesRef = useRef([]);
  const raycasterRef = useRef(new THREE.Raycaster());
  const pointerRef = useRef(new THREE.Vector2());

  function posFor(s, b) {
    if (projection === "cylinder") return cylinderPosition(s, b, 1.15, 2.4);
    return spherePosition(s, b, 1.05);
  }

  function cellAt(sbMap, s, b) {
    return sbMap.get(`${s},${b}`);
  }

  useEffect(() => {
    const el = mountRef.current;
    if (!el) return;

    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x08111f);
    const camera = new THREE.PerspectiveCamera(50, el.clientWidth / Math.max(el.clientHeight, 1), 0.05, 100);
    camera.position.set(2.8, 1.4, 3.2);
    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
    renderer.setPixelRatio(window.devicePixelRatio || 1);
    renderer.setSize(el.clientWidth, el.clientHeight);
    el.appendChild(renderer.domElement);

    const controls = new OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.target.set(0, 0, 0);

    const amb = new THREE.AmbientLight(0xffffff, 0.55);
    scene.add(amb);
    const dir = new THREE.DirectionalLight(0xffffff, 0.65);
    dir.position.set(3, 5, 4);
    scene.add(dir);

    const geom = new THREE.SphereGeometry(0.038, 14, 14);
    /** @type {THREE.MeshStandardMaterial[]} */
    const mats = [];
    /** @type {THREE.Mesh[]} */
    const meshes = [];
    const sbMap = new Map();
    for (const c of cells) {
      sbMap.set(`${c.sector ?? c.q},${c.band ?? c.r}`, c);
    }

    for (let b = 0; b < BANDS; b++) {
      for (let s = 0; s < SECTORS; s++) {
        const h = cellAt(sbMap, s, b);
        const mat = new THREE.MeshStandardMaterial({ color: 0x8899aa, metalness: 0.1, roughness: 0.55 });
        const mesh = new THREE.Mesh(geom, mat);
        const p = posFor(s, b);
        mesh.position.set(p.x, p.y, p.z);
        mesh.userData = { id: h?.id ?? null, s, b };
        scene.add(mesh);
        meshes.push(mesh);
        mats.push(mat);
      }
    }

    const edgeMat = new THREE.LineBasicMaterial({ color: 0x334155, transparent: true, opacity: 0.35 });
    const edgeGeom = new THREE.BufferGeometry();
    const positions = [];
    for (let b = 0; b < BANDS; b++) {
      for (let s = 0; s < SECTORS; s++) {
        const p0 = posFor(s, b);
        const pr = posFor((s + 1) % SECTORS, b);
        positions.push(p0.x, p0.y, p0.z, pr.x, pr.y, pr.z);
        if (b < BANDS - 1) {
          const pd = posFor(s, b + 1);
          positions.push(p0.x, p0.y, p0.z, pd.x, pd.y, pd.z);
        }
      }
    }
    edgeGeom.setAttribute("position", new THREE.Float32BufferAttribute(positions, 3));
    const lines = new THREE.LineSegments(edgeGeom, edgeMat);
    scene.add(lines);

    sceneRef.current = scene;
    cameraRef.current = camera;
    rendererRef.current = renderer;
    controlsRef.current = controls;
    meshesRef.current = meshes;

    let raf = 0;
    function tick() {
      raf = requestAnimationFrame(tick);
      controls.update();
      renderer.render(scene, camera);
    }
    tick();

    const ro = new ResizeObserver(() => {
      if (!mountRef.current) return;
      const w = mountRef.current.clientWidth;
      const h = mountRef.current.clientHeight;
      camera.aspect = w / Math.max(h, 1);
      camera.updateProjectionMatrix();
      renderer.setSize(w, h);
    });
    ro.observe(el);

    function onPointerMove(ev) {
      const r = el.getBoundingClientRect();
      pointerRef.current.x = ((ev.clientX - r.left) / r.width) * 2 - 1;
      pointerRef.current.y = -((ev.clientY - r.top) / r.height) * 2 + 1;
      raycasterRef.current.setFromCamera(pointerRef.current, camera);
      const hits = raycasterRef.current.intersectObjects(meshes, false);
      if (hits.length && hits[0].object.userData.id) {
        onHover(hits[0].object.userData.id);
      } else {
        onHover(null);
      }
    }

    function onPointerDown(ev) {
      const r = el.getBoundingClientRect();
      pointerRef.current.x = ((ev.clientX - r.left) / r.width) * 2 - 1;
      pointerRef.current.y = -((ev.clientY - r.top) / r.height) * 2 + 1;
      raycasterRef.current.setFromCamera(pointerRef.current, camera);
      const hits = raycasterRef.current.intersectObjects(meshes, false);
      if (hits.length && hits[0].object.userData.id) {
        onSelect(hits[0].object.userData.id);
      } else {
        onSelect(null);
      }
    }

    el.addEventListener("pointermove", onPointerMove);
    el.addEventListener("pointerdown", onPointerDown);

    return () => {
      cancelAnimationFrame(raf);
      ro.disconnect();
      el.removeEventListener("pointermove", onPointerMove);
      el.removeEventListener("pointerdown", onPointerDown);
      controls.dispose();
      geom.dispose();
      edgeGeom.dispose();
      edgeMat.dispose();
      for (const m of mats) m.dispose();
      renderer.dispose();
      el.removeChild(renderer.domElement);
    };
  }, [projection]);

  useEffect(() => {
    const meshes = meshesRef.current;
    if (!meshes.length) return;
    const sbMap = new Map();
    for (const c of cells) {
      sbMap.set(`${c.sector ?? c.q},${c.band ?? c.r}`, c);
    }
    let i = 0;
    for (let b = 0; b < BANDS; b++) {
      for (let s = 0; s < SECTORS; s++) {
        const h = sbMap.get(`${s},${b}`);
        const mesh = meshes[i++];
        if (!h) continue;
        const idx = familyLinearIndex(s, b);
        const css = getFillColor(h, renderMode, idx);
        const col = new THREE.Color(css);
        if (mesh.material && mesh.material.color) {
          mesh.material.color.copy(col);
          mesh.material.emissive = new THREE.Color(0x000000);
          if (h.id === selectedId) mesh.material.emissive.setHex(0x334455);
          else if (h.id === hoveredId) mesh.material.emissive.setHex(0x222833);
        }
        mesh.userData.id = h.id;
      }
    }
  }, [cells, renderMode, selectedId, hoveredId]);

  return <div ref={mountRef} className="absolute inset-0" />;
}
