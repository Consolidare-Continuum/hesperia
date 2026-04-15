import React, { useEffect, useMemo, useRef, useState } from "react";
import { motion } from "framer-motion";
import { Search, ZoomIn, ZoomOut, RotateCcw, Layers, Eye, Grid3X3, Play, Pause } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "./components/ui/card";
import { Button } from "./components/ui/button";
import { Input } from "./components/ui/input";
import { Slider } from "./components/ui/slider";
import { Badge } from "./components/ui/badge";
import { Switch } from "./components/ui/switch";

/**
 * HESPERIA Hex Matrix Viewer
 *
 * Purpose:
 * - Render up to ~72,000 hexes interactively
 * - Canvas-based for performance
 * - Pan / zoom / hover / click / search / playback
 * - Visualize area, family, dynamics and time slices
 *
 * Notes:
 * - This is intentionally canvas-first. SVG at 72k interactive nodes will become heavy.
 * - The mock dataset is generated locally so the viewer can run in preview.
 * - Replace generateMockData() with real HESPERIA export payload.
 *
 * Suggested real data shape:
 * {
 *   frames: [
 *     {
 *       t: 0,
 *       hexes: [
 *         {
 *           id: "A01-F034-H0021",
 *           q: 0,
 *           r: 0,
 *           area: "A01",
 *           family: "F034",
 *           value: 0.82,
 *           dominance: 0.66,
 *           label: "conflict_load",
 *           metrics: { signal: 0.4, inhibition: 0.2, stability: 0.9 }
 *         }
 *       ]
 *     }
 *   ]
 * }
 */

const AREA_NAMES = Array.from({ length: 12 }, (_, i) => `A${String(i + 1).padStart(2, "0")}`);
const FAMILY_COUNT = 288;
const HEX_COUNT = 72000;
const FRAMES = 24;

function clamp(v, min, max) {
  return Math.max(min, Math.min(max, v));
}

function lerp(a, b, t) {
  return a + (b - a) * t;
}

function hexToPixel(q, r, size) {
  const x = size * Math.sqrt(3) * (q + r / 2);
  const y = size * 1.5 * r;
  return { x, y };
}

function pointToHex(x, y, size) {
  const q = ((Math.sqrt(3) / 3) * x - (1 / 3) * y) / size;
  const r = ((2 / 3) * y) / size;
  return hexRound(q, r);
}

function hexRound(q, r) {
  let x = q;
  let z = r;
  let y = -x - z;

  let rx = Math.round(x);
  let ry = Math.round(y);
  let rz = Math.round(z);

  const xDiff = Math.abs(rx - x);
  const yDiff = Math.abs(ry - y);
  const zDiff = Math.abs(rz - z);

  if (xDiff > yDiff && xDiff > zDiff) {
    rx = -ry - rz;
  } else if (yDiff > zDiff) {
    ry = -rx - rz;
  } else {
    rz = -rx - ry;
  }

  return { q: rx, r: rz };
}

function polygonPoints(cx, cy, size) {
  const pts = [];
  for (let i = 0; i < 6; i++) {
    const angle = ((60 * i - 30) * Math.PI) / 180;
    pts.push({ x: cx + size * Math.cos(angle), y: cy + size * Math.sin(angle) });
  }
  return pts;
}

function hashString(str) {
  let h = 2166136261;
  for (let i = 0; i < str.length; i++) {
    h ^= str.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return h >>> 0;
}

function areaColor(areaIndex, value) {
  const base = [
    [220, 38, 38],
    [234, 88, 12],
    [202, 138, 4],
    [22, 163, 74],
    [5, 150, 105],
    [6, 182, 212],
    [37, 99, 235],
    [79, 70, 229],
    [124, 58, 237],
    [168, 85, 247],
    [217, 70, 239],
    [236, 72, 153],
  ][areaIndex % 12];

  const light = clamp(0.28 + value * 0.52, 0, 1);
  return `rgba(${Math.round(base[0] * light)}, ${Math.round(base[1] * light)}, ${Math.round(base[2] * light)}, 0.95)`;
}

function familyColor(familyIndex, value) {
  const hue = (familyIndex * 17) % 360;
  const sat = 55 + Math.round(value * 25);
  const light = 28 + Math.round(value * 30);
  return `hsl(${hue} ${sat}% ${light}%)`;
}

function dominanceColor(v) {
  const hue = lerp(220, 0, v);
  const sat = 70;
  const light = lerp(35, 60, v);
  return `hsl(${hue} ${sat}% ${light}%)`;
}

function stabilityColor(v) {
  const hue = lerp(0, 140, v);
  return `hsl(${hue} 68% 45%)`;
}

function buildHexSpiral(count) {
  const coords = [];
  let q = 0;
  let r = 0;
  coords.push({ q, r });
  if (count === 1) return coords;

  const directions = [
    { q: 1, r: 0 },
    { q: 1, r: -1 },
    { q: 0, r: -1 },
    { q: -1, r: 0 },
    { q: -1, r: 1 },
    { q: 0, r: 1 },
  ];

  let radius = 1;
  while (coords.length < count) {
    q = -radius;
    r = radius;
    for (let side = 0; side < 6; side++) {
      for (let step = 0; step < radius; step++) {
        if (coords.length >= count) break;
        coords.push({ q, r });
        q += directions[side].q;
        r += directions[side].r;
      }
    }
    radius++;
  }

  return coords;
}

function generateMockData() {
  const coords = buildHexSpiral(HEX_COUNT);
  const hexes = coords.map((c, i) => {
    const familyIndex = i % FAMILY_COUNT;
    const areaIndex = Math.floor((familyIndex / FAMILY_COUNT) * AREA_NAMES.length) % AREA_NAMES.length;
    const family = `F${String(familyIndex + 1).padStart(3, "0")}`;
    const area = AREA_NAMES[areaIndex];
    const label = `hex-${i + 1}`;
    const seed = hashString(`${area}-${family}-${i}`);
    return {
      id: `${area}-${family}-H${String(i + 1).padStart(5, "0")}`,
      q: c.q,
      r: c.r,
      area,
      areaIndex,
      family,
      familyIndex,
      label,
      base: (seed % 1000) / 1000,
      metrics: {
        signal: ((seed >> 3) % 1000) / 1000,
        inhibition: ((seed >> 7) % 1000) / 1000,
        stability: ((seed >> 11) % 1000) / 1000,
      },
    };
  });

  const frames = Array.from({ length: FRAMES }, (_, frameIndex) => {
    const t = frameIndex / Math.max(1, FRAMES - 1);
    return {
      t,
      hexes: hexes.map((h, i) => {
        const wave = 0.5 + 0.5 * Math.sin(t * Math.PI * 2 + h.q * 0.07 + h.r * 0.11 + (i % 19) * 0.1);
        const pulse = 0.5 + 0.5 * Math.cos(t * Math.PI * 4 + h.familyIndex * 0.08);
        const value = clamp(h.base * 0.35 + wave * 0.4 + pulse * 0.25, 0, 1);
        const dominance = clamp((value * 0.7 + (1 - h.metrics.inhibition) * 0.3), 0, 1);
        const stability = clamp((1 - Math.abs(wave - pulse)) * 0.7 + h.metrics.stability * 0.3, 0, 1);
        return {
          ...h,
          value,
          dominance,
          stability,
        };
      }),
    };
  });

  return { frames };
}

function fitBounds(hexes, size) {
  let minX = Infinity;
  let minY = Infinity;
  let maxX = -Infinity;
  let maxY = -Infinity;

  for (const h of hexes) {
    const { x, y } = hexToPixel(h.q, h.r, size);
    minX = Math.min(minX, x - size);
    minY = Math.min(minY, y - size);
    maxX = Math.max(maxX, x + size);
    maxY = Math.max(maxY, y + size);
  }

  return { minX, minY, maxX, maxY, width: maxX - minX, height: maxY - minY };
}

function getColor(hex, mode) {
  if (mode === "area") return areaColor(hex.areaIndex, hex.value);
  if (mode === "family") return familyColor(hex.familyIndex, hex.value);
  if (mode === "dominance") return dominanceColor(hex.dominance);
  if (mode === "stability") return stabilityColor(hex.stability);
  return areaColor(hex.areaIndex, hex.value);
}

function readDataUrlParam() {
  if (typeof window === "undefined") return null;
  const u = new URLSearchParams(window.location.search).get("data");
  return u && u.trim() ? u.trim() : null;
}

export default function HesperiaHexMatrixViewer() {
  const canvasRef = useRef(null);
  const wrapRef = useRef(null);
  const dprRef = useRef(1);
  const draggingRef = useRef(false);
  const lastMouseRef = useRef({ x: 0, y: 0 });

  const [dataset, setDataset] = useState(() => generateMockData());
  const [dataError, setDataError] = useState(null);

  useEffect(() => {
    const url = readDataUrlParam();
    if (!url) return;
    let cancelled = false;
    (async () => {
      try {
        const res = await fetch(url, { credentials: "omit" });
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const json = await res.json();
        if (!json || !Array.isArray(json.frames)) throw new Error("JSON must have { frames: [...] }");
        if (!cancelled) {
          setDataset(json);
          setDataError(null);
        }
      } catch (e) {
        if (!cancelled) {
          setDataError(e instanceof Error ? e.message : String(e));
        }
      }
    })();
    return () => {
      cancelled = true;
    };
  }, []);
  const [frameIndex, setFrameIndex] = useState(0);
  const [zoom, setZoom] = useState(0.12);
  const [offset, setOffset] = useState({ x: 0, y: 0 });
  const [hoveredId, setHoveredId] = useState(null);
  const [selectedId, setSelectedId] = useState(null);
  const [colorMode, setColorMode] = useState("area");
  const [showGridStroke, setShowGridStroke] = useState(false);
  const [showLabels, setShowLabels] = useState(false);
  const [search, setSearch] = useState("");
  const [isPlaying, setIsPlaying] = useState(false);
  const [hexSize, setHexSize] = useState(7);

  const currentFrame = dataset.frames[frameIndex];
  const currentHexes = currentFrame.hexes;

  const hexMap = useMemo(() => {
    const m = new Map();
    for (const h of currentHexes) {
      m.set(`${h.q},${h.r}`, h);
      m.set(h.id.toLowerCase(), h);
      m.set(h.family.toLowerCase(), h);
    }
    return m;
  }, [currentHexes]);

  const selectedHex = useMemo(() => {
    if (!selectedId) return null;
    return currentHexes.find((h) => h.id === selectedId) || null;
  }, [currentHexes, selectedId]);

  const hoveredHex = useMemo(() => {
    if (!hoveredId) return null;
    return currentHexes.find((h) => h.id === hoveredId) || null;
  }, [currentHexes, hoveredId]);

  useEffect(() => {
    if (!isPlaying) return;
    const id = setInterval(() => {
      setFrameIndex((v) => (v + 1) % dataset.frames.length);
    }, 220);
    return () => clearInterval(id);
  }, [isPlaying, dataset]);

  useEffect(() => {
    const el = wrapRef.current;
    const canvas = canvasRef.current;
    if (!el || !canvas) return;

    function resize() {
      const rect = el.getBoundingClientRect();
      const dpr = window.devicePixelRatio || 1;
      dprRef.current = dpr;
      canvas.width = Math.floor(rect.width * dpr);
      canvas.height = Math.floor(rect.height * dpr);
      canvas.style.width = `${rect.width}px`;
      canvas.style.height = `${rect.height}px`;
    }

    resize();
    const observer = new ResizeObserver(resize);
    observer.observe(el);
    return () => observer.disconnect();
  }, []);

  useEffect(() => {
    const el = wrapRef.current;
    if (!el) return;
    const rect = el.getBoundingClientRect();
    const bounds = fitBounds(currentHexes, hexSize);
    const scaleX = rect.width / Math.max(bounds.width, 1);
    const scaleY = rect.height / Math.max(bounds.height, 1);
    const initialZoom = Math.min(scaleX, scaleY) * 0.92;
    setZoom(initialZoom);
    setOffset({
      x: rect.width / 2 - (bounds.minX + bounds.width / 2) * initialZoom,
      y: rect.height / 2 - (bounds.minY + bounds.height / 2) * initialZoom,
    });
  }, [hexSize]);

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

    const viewLeft = (-offset.x) / zoom - hexSize * 4;
    const viewTop = (-offset.y) / zoom - hexSize * 4;
    const viewRight = (rect.width - offset.x) / zoom + hexSize * 4;
    const viewBottom = (rect.height - offset.y) / zoom + hexSize * 4;

    const shouldDrawLabels = showLabels && zoom > 1.8;

    for (const h of currentHexes) {
      const p = hexToPixel(h.q, h.r, hexSize);
      if (p.x < viewLeft || p.x > viewRight || p.y < viewTop || p.y > viewBottom) continue;

      const sx = p.x * zoom + offset.x;
      const sy = p.y * zoom + offset.y;
      const radius = hexSize * zoom;
      if (sx < -radius * 2 || sx > rect.width + radius * 2 || sy < -radius * 2 || sy > rect.height + radius * 2) continue;

      const pts = polygonPoints(sx, sy, radius);
      ctx.beginPath();
      ctx.moveTo(pts[0].x, pts[0].y);
      for (let i = 1; i < pts.length; i++) ctx.lineTo(pts[i].x, pts[i].y);
      ctx.closePath();
      ctx.fillStyle = getColor(h, colorMode);
      ctx.fill();

      if (showGridStroke || h.id === hoveredId || h.id === selectedId) {
        ctx.lineWidth = h.id === selectedId ? 2.2 : h.id === hoveredId ? 1.6 : 0.5;
        ctx.strokeStyle = h.id === selectedId ? "rgba(255,255,255,0.95)" : h.id === hoveredId ? "rgba(255,255,255,0.75)" : "rgba(255,255,255,0.12)";
        ctx.stroke();
      }

      if (shouldDrawLabels) {
        ctx.fillStyle = "rgba(255,255,255,0.8)";
        ctx.font = `${Math.max(9, radius * 0.48)}px sans-serif`;
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(h.family, sx, sy);
      }
    }

    if (search.trim()) {
      const needle = search.trim().toLowerCase();
      const found = currentHexes.filter(
        (h) => h.id.toLowerCase().includes(needle) || h.family.toLowerCase().includes(needle) || h.area.toLowerCase().includes(needle)
      );
      for (const h of found.slice(0, 250)) {
        const p = hexToPixel(h.q, h.r, hexSize);
        const sx = p.x * zoom + offset.x;
        const sy = p.y * zoom + offset.y;
        const radius = hexSize * zoom;
        ctx.beginPath();
        ctx.arc(sx, sy, Math.max(4, radius * 0.45), 0, Math.PI * 2);
        ctx.strokeStyle = "rgba(255,255,255,0.85)";
        ctx.lineWidth = 1.5;
        ctx.stroke();
      }
    }
  }, [currentHexes, zoom, offset, hoveredId, selectedId, colorMode, showGridStroke, showLabels, search, hexSize]);

  function screenToWorld(clientX, clientY) {
    const rect = wrapRef.current.getBoundingClientRect();
    const x = clientX - rect.left;
    const y = clientY - rect.top;
    return {
      x: (x - offset.x) / zoom,
      y: (y - offset.y) / zoom,
      sx: x,
      sy: y,
    };
  }

  function hitTest(clientX, clientY) {
    const { x, y } = screenToWorld(clientX, clientY);
    const h = pointToHex(x, y, hexSize);
    return hexMap.get(`${h.q},${h.r}`) || null;
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
      setOffset((o) => ({ x: o.x + dx, y: o.y + dy }));
      return;
    }

    const h = hitTest(e.clientX, e.clientY);
    setHoveredId(h ? h.id : null);
  }

  function handleMouseUp(e) {
    const moved = Math.abs(e.clientX - lastMouseRef.current.x) + Math.abs(e.clientY - lastMouseRef.current.y);
    draggingRef.current = false;
    if (moved < 4) {
      const h = hitTest(e.clientX, e.clientY);
      setSelectedId(h ? h.id : null);
    }
  }

  function handleWheel(e) {
    e.preventDefault();
    const rect = wrapRef.current.getBoundingClientRect();
    const mx = e.clientX - rect.left;
    const my = e.clientY - rect.top;
    const scale = e.deltaY < 0 ? 1.12 : 0.9;
    const nextZoom = clamp(zoom * scale, 0.03, 8);
    const wx = (mx - offset.x) / zoom;
    const wy = (my - offset.y) / zoom;
    setZoom(nextZoom);
    setOffset({
      x: mx - wx * nextZoom,
      y: my - wy * nextZoom,
    });
  }

  function resetView() {
    const el = wrapRef.current;
    if (!el) return;
    const rect = el.getBoundingClientRect();
    const bounds = fitBounds(currentHexes, hexSize);
    const scaleX = rect.width / Math.max(bounds.width, 1);
    const scaleY = rect.height / Math.max(bounds.height, 1);
    const initialZoom = Math.min(scaleX, scaleY) * 0.92;
    setZoom(initialZoom);
    setOffset({
      x: rect.width / 2 - (bounds.minX + bounds.width / 2) * initialZoom,
      y: rect.height / 2 - (bounds.minY + bounds.height / 2) * initialZoom,
    });
  }

  function zoomBy(factor) {
    const el = wrapRef.current;
    if (!el) return;
    const rect = el.getBoundingClientRect();
    const cx = rect.width / 2;
    const cy = rect.height / 2;
    const nextZoom = clamp(zoom * factor, 0.03, 8);
    const wx = (cx - offset.x) / zoom;
    const wy = (cy - offset.y) / zoom;
    setZoom(nextZoom);
    setOffset({ x: cx - wx * nextZoom, y: cy - wy * nextZoom });
  }

  function focusHexBySearch() {
    const needle = search.trim().toLowerCase();
    if (!needle) return;
    const found = currentHexes.find(
      (h) => h.id.toLowerCase().includes(needle) || h.family.toLowerCase().includes(needle) || h.area.toLowerCase().includes(needle)
    );
    if (!found || !wrapRef.current) return;
    const rect = wrapRef.current.getBoundingClientRect();
    const p = hexToPixel(found.q, found.r, hexSize);
    const nextZoom = Math.max(zoom, 1.3);
    setZoom(nextZoom);
    setOffset({
      x: rect.width / 2 - p.x * nextZoom,
      y: rect.height / 2 - p.y * nextZoom,
    });
    setSelectedId(found.id);
  }

  const infoHex = selectedHex || hoveredHex;
  const byArea = useMemo(() => {
    const out = new Map();
    for (const a of AREA_NAMES) out.set(a, 0);
    for (const h of currentHexes) out.set(h.area, out.get(h.area) + h.value);
    return Array.from(out.entries()).sort((a, b) => b[1] - a[1]);
  }, [currentHexes]);

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-4 md:p-6">
      {dataError ? (
        <div className="mb-4 rounded-2xl border border-amber-700/60 bg-amber-950/40 px-4 py-3 text-sm text-amber-100">
          <span className="font-semibold">Data URL failed:</span> {dataError} (showing mock data until fixed)
        </div>
      ) : null}
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        className="grid grid-cols-1 xl:grid-cols-[360px_1fr] gap-4"
      >
        <div className="space-y-4">
          <Card className="bg-slate-900/80 border-slate-800 rounded-2xl shadow-2xl">
            <CardHeader>
              <CardTitle className="flex items-center gap-2 text-xl">
                <Grid3X3 className="w-5 h-5" />
                HESPERIA Hex Matrix
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="text-sm text-slate-300 leading-6">
                Canvas viewer for large-scale interactive hex topology. Built for area/family state inspection, dynamic playback, and bounded navigation across all 72,000 hexes.
              </div>

              <div className="grid grid-cols-2 gap-2 text-sm">
                <div className="p-3 rounded-2xl bg-slate-800/70">
                  <div className="text-slate-400">Hexes</div>
                  <div className="text-lg font-semibold">72,000</div>
                </div>
                <div className="p-3 rounded-2xl bg-slate-800/70">
                  <div className="text-slate-400">Families</div>
                  <div className="text-lg font-semibold">288</div>
                </div>
                <div className="p-3 rounded-2xl bg-slate-800/70">
                  <div className="text-slate-400">Areas</div>
                  <div className="text-lg font-semibold">12</div>
                </div>
                <div className="p-3 rounded-2xl bg-slate-800/70">
                  <div className="text-slate-400">Frame</div>
                  <div className="text-lg font-semibold">{frameIndex + 1} / {FRAMES}</div>
                </div>
              </div>

              <div className="space-y-2">
                <div className="text-sm text-slate-300">Search hex / family / area</div>
                <div className="flex gap-2">
                  <Input
                    value={search}
                    onChange={(e) => setSearch(e.target.value)}
                    placeholder="A01, F034, H00021..."
                    className="bg-slate-800 border-slate-700"
                  />
                  <Button variant="secondary" onClick={focusHexBySearch} className="rounded-2xl">
                    <Search className="w-4 h-4" />
                  </Button>
                </div>
              </div>

              <div className="space-y-2">
                <div className="text-sm text-slate-300">Color mode</div>
                <select
                  value={colorMode}
                  onChange={(e) => setColorMode(e.target.value)}
                  className="w-full rounded-2xl border border-slate-700 bg-slate-800 px-3 py-2 text-sm text-slate-100"
                >
                  <option value="area">Area bands</option>
                  <option value="family">Family spectrum</option>
                  <option value="dominance">Dominance heat</option>
                  <option value="stability">Stability heat</option>
                </select>
              </div>

              <div className="space-y-3">
                <div className="flex items-center justify-between text-sm">
                  <span className="text-slate-300">Frame playback</span>
                  <Button variant="secondary" className="rounded-2xl" onClick={() => setIsPlaying((v) => !v)}>
                    {isPlaying ? <Pause className="w-4 h-4" /> : <Play className="w-4 h-4" />}
                  </Button>
                </div>
                <Slider
                  value={[frameIndex]}
                  min={0}
                  max={FRAMES - 1}
                  step={1}
                  onValueChange={(v) => setFrameIndex(v[0])}
                />
              </div>

              <div className="space-y-3">
                <div className="text-sm text-slate-300">Base hex radius: {hexSize}</div>
                <Slider
                  value={[hexSize]}
                  min={4}
                  max={12}
                  step={1}
                  onValueChange={(v) => setHexSize(v[0])}
                />
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div className="flex items-center justify-between p-3 rounded-2xl bg-slate-800/70">
                  <div className="flex items-center gap-2 text-sm"><Layers className="w-4 h-4" /> Grid stroke</div>
                  <Switch checked={showGridStroke} onCheckedChange={setShowGridStroke} />
                </div>
                <div className="flex items-center justify-between p-3 rounded-2xl bg-slate-800/70">
                  <div className="flex items-center gap-2 text-sm"><Eye className="w-4 h-4" /> Labels</div>
                  <Switch checked={showLabels} onCheckedChange={setShowLabels} />
                </div>
              </div>

              <div className="grid grid-cols-3 gap-2">
                <Button variant="secondary" className="rounded-2xl" onClick={() => zoomBy(1.25)}>
                  <ZoomIn className="w-4 h-4" />
                </Button>
                <Button variant="secondary" className="rounded-2xl" onClick={() => zoomBy(0.8)}>
                  <ZoomOut className="w-4 h-4" />
                </Button>
                <Button variant="secondary" className="rounded-2xl" onClick={resetView}>
                  <RotateCcw className="w-4 h-4" />
                </Button>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-slate-900/80 border-slate-800 rounded-2xl shadow-2xl">
            <CardHeader>
              <CardTitle className="text-lg">Inspection</CardTitle>
            </CardHeader>
            <CardContent>
              {infoHex ? (
                <div className="space-y-3 text-sm">
                  <div>
                    <div className="text-slate-400">Hex ID</div>
                    <div className="font-medium break-all">{infoHex.id}</div>
                  </div>
                  <div className="flex flex-wrap gap-2">
                    <Badge variant="secondary" className="rounded-xl">{infoHex.area}</Badge>
                    <Badge variant="secondary" className="rounded-xl">{infoHex.family}</Badge>
                    <Badge variant="secondary" className="rounded-xl">q {infoHex.q}</Badge>
                    <Badge variant="secondary" className="rounded-xl">r {infoHex.r}</Badge>
                  </div>
                  <div className="grid grid-cols-2 gap-2">
                    <div className="p-3 rounded-2xl bg-slate-800/70">
                      <div className="text-slate-400">Value</div>
                      <div className="font-semibold">{infoHex.value.toFixed(3)}</div>
                    </div>
                    <div className="p-3 rounded-2xl bg-slate-800/70">
                      <div className="text-slate-400">Dominance</div>
                      <div className="font-semibold">{infoHex.dominance.toFixed(3)}</div>
                    </div>
                    <div className="p-3 rounded-2xl bg-slate-800/70">
                      <div className="text-slate-400">Signal</div>
                      <div className="font-semibold">{infoHex.metrics.signal.toFixed(3)}</div>
                    </div>
                    <div className="p-3 rounded-2xl bg-slate-800/70">
                      <div className="text-slate-400">Stability</div>
                      <div className="font-semibold">{infoHex.stability.toFixed(3)}</div>
                    </div>
                  </div>
                </div>
              ) : (
                <div className="text-sm text-slate-400">Hover or click a hex to inspect it.</div>
              )}
            </CardContent>
          </Card>

          <Card className="bg-slate-900/80 border-slate-800 rounded-2xl shadow-2xl">
            <CardHeader>
              <CardTitle className="text-lg">Area load</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-2">
                {byArea.map(([name, value]) => (
                  <div key={name} className="space-y-1">
                    <div className="flex justify-between text-xs text-slate-300">
                      <span>{name}</span>
                      <span>{value.toFixed(1)}</span>
                    </div>
                    <div className="h-2 rounded-full bg-slate-800 overflow-hidden">
                      <div
                        className="h-full rounded-full"
                        style={{ width: `${(value / byArea[0][1]) * 100}%`, background: areaColor(parseInt(name.slice(1), 10) - 1, 0.85) }}
                      />
                    </div>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        </div>

        <Card className="bg-slate-900/80 border-slate-800 rounded-2xl shadow-2xl overflow-hidden">
          <CardContent className="p-0">
            <div className="relative h-[78vh] min-h-[680px]" ref={wrapRef}>
              <canvas
                ref={canvasRef}
                className="absolute inset-0 cursor-grab active:cursor-grabbing"
                onMouseDown={handleMouseDown}
                onMouseMove={handleMouseMove}
                onMouseUp={handleMouseUp}
                onMouseLeave={() => {
                  draggingRef.current = false;
                  setHoveredId(null);
                }}
                onWheel={handleWheel}
              />

              <div className="absolute top-4 left-4 flex flex-wrap gap-2 max-w-[70%]">
                <Badge className="rounded-xl bg-slate-950/80 text-slate-100 border border-slate-700">zoom {zoom.toFixed(2)}x</Badge>
                <Badge className="rounded-xl bg-slate-950/80 text-slate-100 border border-slate-700">mode {colorMode}</Badge>
                <Badge className="rounded-xl bg-slate-950/80 text-slate-100 border border-slate-700">frame {frameIndex + 1}</Badge>
                {hoveredHex && <Badge className="rounded-xl bg-slate-950/80 text-slate-100 border border-slate-700">hover {hoveredHex.id}</Badge>}
                {selectedHex && <Badge className="rounded-xl bg-slate-950/80 text-slate-100 border border-slate-700">selected {selectedHex.id}</Badge>}
              </div>
            </div>
          </CardContent>
        </Card>
      </motion.div>
    </div>
  );
}
