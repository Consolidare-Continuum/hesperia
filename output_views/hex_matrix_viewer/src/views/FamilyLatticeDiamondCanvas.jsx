import React, { useCallback, useEffect, useRef, useState } from "react";
import { SECTORS, BANDS, familyLinearIndex, diamondLayout } from "../topology/spheroidLattice.js";
import { getFillColor } from "../render/modes.js";

function clamp(v, lo, hi) {
  return Math.max(lo, Math.min(hi, v));
}

/**
 * Band-centered diamond: inspection / cognition layout (not 3D truth). 288 cells F(s,b).
 */
export default function FamilyLatticeDiamondCanvas({ cells, renderMode, selectedId, hoveredId, search, onSelect, onHover }) {
  const canvasRef = useRef(null);
  const wrapRef = useRef(null);
  const dprRef = useRef(1);
  const draggingRef = useRef(false);
  const lastMouseRef = useRef({ x: 0, y: 0 });
  const [zoom, setZoom] = useState(1);
  const [pan, setPan] = useState({ x: 0, y: 0 });

  const bySb = useCallback(() => {
    const m = new Map();
    for (const c of cells) {
      const s = c.sector ?? c.q;
      const b = c.band ?? c.r;
      m.set(`${s},${b}`, c);
    }
    return m;
  }, [cells]);

  function diamondCenter(s, b, rect, pad, gw, gh) {
    const { width, col } = diamondLayout(s, b);
    const centerX = rect.width / 2;
    const rowInner = (width / 12) * gw;
    const cellPitch = width > 0 ? rowInner / width : rowInner;
    const cx = centerX - rowInner / 2 + (col + 0.5) * cellPitch;
    const spread = (s - 5.5) * (cellPitch * 0.12);
    const ch = gh / BANDS;
    const cy = pad + (b + 0.5) * ch;
    return { cx: cx + spread, cy, cellPitch, ch };
  }

  useEffect(() => {
    const el = wrapRef.current;
    const canvas = canvasRef.current;
    if (!el || !canvas) return;
    function resize() {
      const r = el.getBoundingClientRect();
      const dpr = window.devicePixelRatio || 1;
      dprRef.current = dpr;
      canvas.width = Math.floor(r.width * dpr);
      canvas.height = Math.floor(r.height * dpr);
      canvas.style.width = `${r.width}px`;
      canvas.style.height = `${r.height}px`;
    }
    resize();
    const ro = new ResizeObserver(resize);
    ro.observe(el);
    return () => ro.disconnect();
  }, []);

  useEffect(() => {
    const canvas = canvasRef.current;
    const el = wrapRef.current;
    if (!canvas || !el) return;
    const ctx = canvas.getContext("2d");
    const rect = el.getBoundingClientRect();
    const dpr = dprRef.current;
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.scale(dpr, dpr);
    ctx.fillStyle = "#08111f";
    ctx.fillRect(0, 0, rect.width, rect.height);

    const pad = 28;
    const gw = rect.width - pad * 2;
    const gh = rect.height - pad * 2;
    const map = bySb();

    ctx.save();
    ctx.translate(rect.width / 2 + pan.x, rect.height / 2 + pan.y);
    ctx.scale(zoom, zoom);
    ctx.translate(-rect.width / 2, -rect.height / 2);

    ctx.strokeStyle = "rgba(255,255,255,0.14)";
    ctx.lineWidth = 1 / zoom;
    for (let b = 0; b < BANDS; b++) {
      for (let s = 0; s < SECTORS; s++) {
        const p0 = diamondCenter(s, b, rect, pad, gw, gh);
        const pr = diamondCenter((s + 1) % SECTORS, b, rect, pad, gw, gh);
        ctx.beginPath();
        ctx.moveTo(p0.cx, p0.cy);
        ctx.lineTo(pr.cx, pr.cy);
        ctx.stroke();
        if (b < BANDS - 1) {
          const pd = diamondCenter(s, b + 1, rect, pad, gw, gh);
          ctx.beginPath();
          ctx.moveTo(p0.cx, p0.cy);
          ctx.lineTo(pd.cx, pd.cy);
          ctx.stroke();
        }
      }
    }
    ctx.setLineDash([4 / zoom, 4 / zoom]);
    ctx.strokeStyle = "rgba(250, 204, 21, 0.28)";
    for (let b = 0; b < BANDS; b++) {
      const a = diamondCenter(11, b, rect, pad, gw, gh);
      const o = diamondCenter(0, b, rect, pad, gw, gh);
      ctx.beginPath();
      ctx.moveTo(a.cx, a.cy);
      ctx.bezierCurveTo(a.cx + gw * 0.04, a.cy + gh * 0.04, o.cx - gw * 0.04, o.cy + gh * 0.04, o.cx, o.cy);
      ctx.stroke();
    }
    ctx.setLineDash([]);

    if (renderMode === "boundary") {
      ctx.lineWidth = 1.3 / zoom;
      for (let b = 0; b < BANDS; b++) {
        for (let s = 0; s < SECTORS; s++) {
          const h = map.get(`${s},${b}`);
          if (!h) continue;
          const pr = map.get(`${(s + 1) % SECTORS},${b}`);
          if (pr && pr.dominant_area !== h.dominant_area) {
            const p0 = diamondCenter(s, b, rect, pad, gw, gh);
            const p1 = diamondCenter((s + 1) % SECTORS, b, rect, pad, gw, gh);
            ctx.beginPath();
            ctx.moveTo(p0.cx, p0.cy);
            ctx.lineTo(p1.cx, p1.cy);
            ctx.strokeStyle = "rgba(255,255,255,0.42)";
            ctx.stroke();
          }
          if (b < BANDS - 1) {
            const pd = map.get(`${s},${b + 1}`);
            if (pd && pd.dominant_area !== h.dominant_area) {
              const p0 = diamondCenter(s, b, rect, pad, gw, gh);
              const p1 = diamondCenter(s, b + 1, rect, pad, gw, gh);
              ctx.beginPath();
              ctx.moveTo(p0.cx, p0.cy);
              ctx.lineTo(p1.cx, p1.cy);
              ctx.strokeStyle = "rgba(255,255,255,0.42)";
              ctx.stroke();
            }
          }
        }
      }
    }

    for (let b = 0; b < BANDS; b++) {
      for (let s = 0; s < SECTORS; s++) {
        const h = map.get(`${s},${b}`);
        if (!h) continue;
        const idx = familyLinearIndex(s, b);
        const pos = diamondCenter(s, b, rect, pad, gw, gh);
        const nodeR = Math.min(pos.cellPitch, pos.ch) * 0.28;
        ctx.beginPath();
        ctx.arc(pos.cx, pos.cy, nodeR, 0, Math.PI * 2);
        ctx.fillStyle = getFillColor(h, renderMode, idx);
        ctx.fill();
        if (h.id === selectedId || h.id === hoveredId) {
          ctx.lineWidth = h.id === selectedId ? 2.4 / zoom : 1.6 / zoom;
          ctx.strokeStyle = "rgba(255,255,255,0.92)";
          ctx.stroke();
        }
        if (search.trim()) {
          const needle = search.trim().toLowerCase();
          const hit =
            h.id.toLowerCase().includes(needle) ||
            String(h.family_id).includes(needle) ||
            `s${s}b${b}`.includes(needle) ||
            String(h.dominant_area).includes(needle);
          if (hit) {
            ctx.beginPath();
            ctx.arc(pos.cx, pos.cy, nodeR + 4 / zoom, 0, Math.PI * 2);
            ctx.strokeStyle = "rgba(255,255,255,0.7)";
            ctx.lineWidth = 1.1 / zoom;
            ctx.stroke();
          }
        }
      }
    }

    ctx.restore();

    ctx.fillStyle = "rgba(226,232,240,0.75)";
    ctx.font = "11px sans-serif";
    ctx.fillText("Diamond · b=0 north", 8, 16);
    ctx.fillText("b=23 south", 8, rect.height - 8);
  }, [cells, renderMode, selectedId, hoveredId, search, zoom, pan, bySb]);

  function worldFromClient(clientX, clientY) {
    const el = wrapRef.current;
    if (!el) return { lx: 0, ly: 0 };
    const r = el.getBoundingClientRect();
    const x = clientX - r.left;
    const y = clientY - r.top;
    return {
      lx: (x - r.width / 2 - pan.x) / zoom + r.width / 2,
      ly: (y - r.height / 2 - pan.y) / zoom + r.height / 2,
    };
  }

  function hitDiamond(clientX, clientY) {
    const el = wrapRef.current;
    if (!el) return null;
    const r = el.getBoundingClientRect();
    const pad = 28;
    const gw = r.width - pad * 2;
    const gh = r.height - pad * 2;
    const { lx, ly } = worldFromClient(clientX, clientY);
    let best = null;
    let bestD = 1e9;
    for (let b = 0; b < BANDS; b++) {
      for (let s = 0; s < SECTORS; s++) {
        const pos = diamondCenter(s, b, r, pad, gw, gh);
        const nodeR = Math.min(pos.cellPitch, pos.ch) * 0.28;
        const d = Math.hypot(lx - pos.cx, ly - pos.cy);
        if (d <= nodeR * 1.35 && d < bestD) {
          best = { s, b };
          bestD = d;
        }
      }
    }
    return best;
  }

  function handleMouseDown(e) {
    draggingRef.current = true;
    lastMouseRef.current = { x: e.clientX, y: e.clientY };
  }

  function handleMouseMove(e) {
    if (draggingRef.current) {
      const dx = e.clientX - lastMouseRef.current.x;
      const dy = e.clientY - lastMouseRef.current.y;
      lastMouseRef.current = { x: e.clientX, y: e.clientY };
      setPan((p) => ({ x: p.x + dx, y: p.y + dy }));
      return;
    }
    const lb = hitDiamond(e.clientX, e.clientY);
    if (!lb) {
      onHover(null);
      return;
    }
    const c = cells.find((x) => (x.sector ?? x.q) === lb.s && (x.band ?? x.r) === lb.b);
    onHover(c ? c.id : null);
  }

  function handleMouseUp(e) {
    const moved = Math.abs(e.clientX - lastMouseRef.current.x) + Math.abs(e.clientY - lastMouseRef.current.y);
    draggingRef.current = false;
    if (moved < 4) {
      const lb = hitDiamond(e.clientX, e.clientY);
      if (!lb) {
        onSelect(null);
        return;
      }
      const c = cells.find((x) => (x.sector ?? x.q) === lb.s && (x.band ?? x.r) === lb.b);
      onSelect(c ? c.id : null);
    }
  }

  function handleWheel(e) {
    e.preventDefault();
    const el = wrapRef.current;
    if (!el) return;
    const r = el.getBoundingClientRect();
    const mx = e.clientX - r.left;
    const my = e.clientY - r.top;
    const scale = e.deltaY < 0 ? 1.1 : 0.91;
    const next = clamp(zoom * scale, 0.35, 8);
    const wx = (mx - r.width / 2 - pan.x) / zoom;
    const wy = (my - r.height / 2 - pan.y) / zoom;
    setZoom(next);
    setPan({
      x: mx - r.width / 2 - wx * next,
      y: my - r.height / 2 - wy * next,
    });
  }

  return (
    <div className="relative w-full h-full" ref={wrapRef}>
      <canvas
        ref={canvasRef}
        className="absolute inset-0 cursor-grab active:cursor-grabbing"
        onMouseDown={handleMouseDown}
        onMouseMove={handleMouseMove}
        onMouseUp={handleMouseUp}
        onMouseLeave={() => {
          draggingRef.current = false;
          onHover(null);
        }}
        onWheel={handleWheel}
      />
    </div>
  );
}
