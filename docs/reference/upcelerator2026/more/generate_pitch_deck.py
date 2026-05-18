"""Generate HESPERIA Pitch Deck PPTX — Upcelerator template structure."""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

# Palette
DARK = RGBColor(0x0F, 0x11, 0x1A)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
ACCENT = RGBColor(0x00, 0x7A, 0xCC)
TEAL = RGBColor(0x00, 0x96, 0x88)
ORANGE = RGBColor(0xE6, 0x5C, 0x00)
RED = RGBColor(0xC6, 0x28, 0x28)
PURPLE = RGBColor(0x7B, 0x1F, 0xA2)
LIGHT_BG = RGBColor(0xF5, 0xF7, 0xFA)
SECTION_BG = RGBColor(0xF0, 0xF4, 0xF8)
MUTED = RGBColor(0x88, 0x88, 0x88)
BORDER = RGBColor(0xCC, 0xCC, 0xCC)

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)


def tb(slide, left, top, width, height, text, size=10, bold=False,
       color=DARK, align=PP_ALIGN.LEFT, font="Calibri"):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    tf.margin_top = Pt(4)
    tf.margin_bottom = Pt(4)
    tf.margin_left = Pt(6)
    tf.margin_right = Pt(6)
    if isinstance(text, list):
        for i, line in enumerate(text):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.text = line
            p.font.size = Pt(size)
            p.font.bold = bold
            p.font.color.rgb = color
            p.font.name = font
            p.alignment = align
            p.space_after = Pt(3)
    else:
        p = tf.paragraphs[0]
        p.text = text
        p.font.size = Pt(size)
        p.font.bold = bold
        p.font.color.rgb = color
        p.font.name = font
        p.alignment = align
    return txBox


def rect(slide, left, top, width, height, fill=WHITE, border=BORDER, bw=Pt(0.5)):
    s = slide.shapes.add_shape(1, left, top, width, height)
    s.fill.solid()
    s.fill.fore_color.rgb = fill
    s.line.color.rgb = border
    s.line.width = bw
    return s


def build():
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # SLIDE 1 — TITLE / VISION
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    rect(sl, Inches(0), Inches(0), SLIDE_W, SLIDE_H, fill=DARK)

    tb(sl, Inches(1), Inches(1.2), Inches(11), Inches(1),
       "HESPERIA", size=56, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    tb(sl, Inches(1), Inches(2.3), Inches(11), Inches(0.7),
       "Deterministic Semantic Infrastructure for AI Systems",
       size=22, color=ACCENT, align=PP_ALIGN.CENTER)

    vision = (
        "Today's AI operates as a probabilistic black box — outputs that are difficult "
        "to audit, reproduce, or trust in high-stakes environments. HESPERIA replaces this "
        "uncertainty with structured, measurable, and repeatable representations of meaning. "
        "Instead of generating answers, it maps them."
    )
    tb(sl, Inches(1.5), Inches(3.5), Inches(10), Inches(1.5),
       vision, size=14, color=WHITE, align=PP_ALIGN.CENTER)

    tb(sl, Inches(1), Inches(5.5), Inches(11), Inches(0.5),
       "Make AI understandable, reliable, and usable where failure is not acceptable.",
       size=16, bold=True, color=ACCENT, align=PP_ALIGN.CENTER)

    tb(sl, Inches(1), Inches(6.5), Inches(11), Inches(0.6),
       ["Upcelerator · Phase 1 · Pitch Deck · March 2026",
        "Igor Platonov · igareosh.com · prichindel.com"],
       size=10, color=MUTED, align=PP_ALIGN.CENTER)

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # SLIDE 2 — PROBLEM
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    rect(sl, Inches(0), Inches(0), SLIDE_W, SLIDE_H, fill=WHITE)

    tb(sl, Inches(0.5), Inches(0.3), Inches(5), Inches(0.5),
       "The Problem", size=28, bold=True, color=DARK)

    problems = [
        ("Probabilistic, non-repeatable outputs",
         "AI systems produce different results for the same input. "
         "Specialists cannot verify or reproduce what AI decides.",
         RED),
        ("No auditability in critical environments",
         "Finance, healthcare, and legal sectors require traceability. "
         "Current AI tools cannot provide audit-grade evidence trails.",
         ORANGE),
        ("Monitoring ≠ solving",
         "Existing solutions (Arize, Arthur, Patronus) monitor and explain "
         "behavior after the fact. They manage uncertainty — they do not eliminate it.",
         PURPLE),
        ("Regulation is accelerating",
         "EU AI Act, GDPR, and sector-specific rules demand structured, "
         "explainable outputs. The gap between AI capability and trust is the bottleneck.",
         ACCENT),
    ]

    y = Inches(1.2)
    for title, desc, clr in problems:
        rect(sl, Inches(0.5), y, Inches(7.5), Inches(1.25),
             fill=SECTION_BG, border=clr, bw=Pt(1.5))
        tb(sl, Inches(0.8), y + Pt(4), Inches(7), Inches(0.3),
           title, size=13, bold=True, color=clr)
        tb(sl, Inches(0.8), y + Inches(0.4), Inches(7), Inches(0.8),
           desc, size=10, color=DARK)
        y += Inches(1.4)

    # Right panel — the core tension
    rect(sl, Inches(8.5), Inches(1.2), Inches(4.5), Inches(5.8), fill=DARK)
    tension_lines = [
        "",
        "THE CORE TENSION",
        "",
        "AI capability is growing.",
        "AI trust is not.",
        "",
        "Companies need systems",
        "that guarantee consistency,",
        "not tools that explain",
        "inconsistency.",
        "",
        "━━━━━━━━━━━━━━━━━━━",
        "",
        "Current paradigm:",
        "  generate → evaluate → patch",
        "",
        "What's needed:",
        "  structure → stabilize → audit",
    ]
    tb(sl, Inches(8.7), Inches(1.3), Inches(4.1), Inches(5.5),
       tension_lines, size=11, color=WHITE, align=PP_ALIGN.LEFT)

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # SLIDE 3 — SOLUTION
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    rect(sl, Inches(0), Inches(0), SLIDE_W, SLIDE_H, fill=WHITE)

    tb(sl, Inches(0.5), Inches(0.3), Inches(5), Inches(0.5),
       "The Solution", size=28, bold=True, color=DARK)

    tb(sl, Inches(0.5), Inches(1.0), Inches(12), Inches(0.5),
       "A deterministic semantic engine that converts text into structured, auditable meaning.",
       size=14, bold=True, color=ACCENT)

    features = [
        ("Deterministic by Design",
         "Same input, same structured output, every time. "
         "Hash-verifiable. No drift, no variance, no surprises."),
        ("Fixed Structural Topology",
         "Maps input into 10 macro domains, 240 policy families, "
         "with topology-aware propagation across a fixed graph."),
        ("Evidence Traces & Trust Tiers",
         "Every output includes evidence (span, label, confidence band) "
         "and a trust tier for automated vs. human-review routing."),
        ("7 Product Lines, One Engine",
         "Structural measurement, narrative propagation, contradiction "
         "intelligence, fingerprint, domain topology, semantic dashboard."),
        ("Integration-First",
         "API / CLI. Sits beneath existing AI as a foundational layer. "
         "Enhances LLMs — does not replace or compete with them."),
        ("Sealed Runtime",
         "Public audit manifests (version, checksum, evidence count). "
         "Projection layer prevents internal leakage. Compliance-ready."),
    ]

    col_w = Inches(4)
    gap = Inches(0.2)
    for i, (title, desc) in enumerate(features):
        col = i % 3
        row = i // 3
        x = Inches(0.5) + col * (col_w + gap)
        yy = Inches(1.8) + row * Inches(2.4)
        rect(sl, x, yy, col_w, Inches(2.1), fill=SECTION_BG, border=ACCENT)
        tb(sl, x + Pt(8), yy + Pt(6), col_w - Pt(16), Inches(0.35),
           title, size=12, bold=True, color=ACCENT)
        tb(sl, x + Pt(8), yy + Inches(0.45), col_w - Pt(16), Inches(1.5),
           desc, size=10, color=DARK)

    tb(sl, Inches(0.5), Inches(6.8), Inches(12), Inches(0.4),
       "\"Not a better tool — a different system. Competitors optimize uncertainty; HESPERIA eliminates it at the source.\"",
       size=10, bold=True, color=MUTED, align=PP_ALIGN.CENTER)

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # SLIDE 4 — HOW IT WORKS (persona)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    rect(sl, Inches(0), Inches(0), SLIDE_W, SLIDE_H, fill=WHITE)

    tb(sl, Inches(0.5), Inches(0.3), Inches(6), Inches(0.5),
       "How It Works", size=28, bold=True, color=DARK)

    tb(sl, Inches(0.5), Inches(0.85), Inches(8), Inches(0.4),
       "Meet a compliance officer at a financial institution.",
       size=14, bold=True, color=ACCENT)

    # Before / After
    rect(sl, Inches(0.5), Inches(1.5), Inches(5.8), Inches(4.5),
         fill=RGBColor(0xFD, 0xF0, 0xEF), border=RED)
    tb(sl, Inches(0.7), Inches(1.55), Inches(5.4), Inches(0.35),
       "TODAY (without HESPERIA)", size=12, bold=True, color=RED)
    before_lines = [
        "• Relies on AI tools that generate summaries",
        "  and risk assessments",
        "",
        "• Cannot explain or reproduce decisions reliably",
        "",
        "• Reviews unclear, inconsistent AI outputs manually",
        "",
        "• Spends hours on documents that could be pre-screened",
        "",
        "• Audit trail: incomplete or absent",
        "",
        "• Compliance: hope-based, not system-based",
    ]
    tb(sl, Inches(0.7), Inches(2.0), Inches(5.4), Inches(3.8),
       before_lines, size=10, color=DARK)

    rect(sl, Inches(6.8), Inches(1.5), Inches(6.2), Inches(4.5),
         fill=RGBColor(0xEF, 0xF8, 0xF0), border=TEAL)
    tb(sl, Inches(7.0), Inches(1.55), Inches(5.8), Inches(0.35),
       "WITH HESPERIA", size=12, bold=True, color=TEAL)
    after_lines = [
        "• Any input (document, report, communication) is mapped",
        "  into a structured semantic space",
        "",
        "• System identifies concepts, relationships, and",
        "  dominant areas — consistent output every time",
        "",
        "• Each result is fully traceable to source components",
        "",
        "• Officer works with a deterministic structure that",
        "  can be audited, compared, and validated",
        "",
        "• Risk reduced, decision quality improved,",
        "  compliance readiness by design",
    ]
    tb(sl, Inches(7.0), Inches(2.0), Inches(5.8), Inches(3.8),
       after_lines, size=10, color=DARK)

    # Pipeline flow (bottom)
    rect(sl, Inches(0.5), Inches(6.3), Inches(12.5), Inches(0.9), fill=DARK)
    flow = "Text Input  →  Lexicon Attribution  →  L1–L9 Execution Flow  →  Topology Propagation  →  Projection Gate  →  Public JSON + Evidence + Trust Tier"
    tb(sl, Inches(0.7), Inches(6.4), Inches(12.1), Inches(0.7),
       flow, size=11, bold=True, color=ACCENT, align=PP_ALIGN.CENTER)

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # SLIDE 5 — MARKET
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    rect(sl, Inches(0), Inches(0), SLIDE_W, SLIDE_H, fill=WHITE)

    tb(sl, Inches(0.5), Inches(0.3), Inches(5), Inches(0.5),
       "Market", size=28, bold=True, color=DARK)

    tb(sl, Inches(0.5), Inches(0.85), Inches(12), Inches(0.4),
       "AI infrastructure × compliance-driven enterprise software",
       size=14, bold=True, color=ACCENT)

    # TAM / SAM / SOM circles (left side)
    tam_data = [
        ("TAM", "€5B", "Bottom-up: 500K companies × €10K\nIndustry context: $10–15B+", ACCENT, Inches(0.5), Inches(1.7), Inches(3.8), Inches(2.4)),
        ("SAM", "€200M", "~20,000 EU companies\nwith compliance pressure\nACV €5–20K", TEAL, Inches(4.8), Inches(1.7), Inches(3.8), Inches(2.4)),
        ("SOM", "€1M ARR", "100 companies × €10K\nYr 1–3 realistic capture\nBottom-up: real × real", ORANGE, Inches(9.1), Inches(1.7), Inches(3.8), Inches(2.4)),
    ]

    for label, amount, desc, clr, x, y, w, h in tam_data:
        rect(sl, x, y, w, h, fill=SECTION_BG, border=clr, bw=Pt(2))
        tb(sl, x, y + Pt(6), w, Inches(0.3),
           label, size=11, bold=True, color=clr, align=PP_ALIGN.CENTER)
        tb(sl, x, y + Inches(0.4), w, Inches(0.5),
           amount, size=24, bold=True, color=clr, align=PP_ALIGN.CENTER)
        tb(sl, x, y + Inches(1.2), w, Inches(1),
           desc, size=9, color=DARK, align=PP_ALIGN.CENTER)

    # Industry + geography + segments (bottom)
    rect(sl, Inches(0.5), Inches(4.4), Inches(4), Inches(2.8),
         fill=DARK)
    ind_lines = [
        "INDUSTRIES",
        "",
        "• AI / ML Infrastructure",
        "• AI Observability & Monitoring",
        "• Enterprise Software (SaaS)",
        "• Risk & Compliance Tech (RegTech)",
        "• Data Analytics / Decision Systems",
    ]
    tb(sl, Inches(0.7), Inches(4.5), Inches(3.6), Inches(2.6),
       ind_lines, size=9, color=WHITE)

    rect(sl, Inches(4.8), Inches(4.4), Inches(4), Inches(2.8),
         fill=DARK)
    geo_lines = [
        "GEOGRAPHY (phased)",
        "",
        "Yr 1–2: Chișinău, Moldova (beachhead)",
        "  Moldova IT Park: 2,725 companies",
        "  $1B turnover, 25,000+ employees",
        "",
        "Yr 2–3: Romania → EU priority markets",
        "  (stricter compliance needs)",
        "",
        "Yr 3–5: Full EU / enterprise",
    ]
    tb(sl, Inches(5.0), Inches(4.5), Inches(3.6), Inches(2.6),
       geo_lines, size=9, color=WHITE)

    rect(sl, Inches(9.1), Inches(4.4), Inches(4), Inches(2.8),
         fill=DARK)
    seg_lines = [
        "TARGET BUYERS",
        "",
        "• CTO / Head of AI",
        "• Risk & Compliance Officers",
        "• Product Owners (AI systems)",
        "",
        "Company: 50–5,000+ employees",
        "Revenue: €1M – €500M+",
        "",
        "Key: deploying AI in production",
        "with regulatory or financial risk",
    ]
    tb(sl, Inches(9.3), Inches(4.5), Inches(3.6), Inches(2.6),
       seg_lines, size=9, color=WHITE)

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # SLIDE 6 — COMPETITION
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    rect(sl, Inches(0), Inches(0), SLIDE_W, SLIDE_H, fill=WHITE)

    tb(sl, Inches(0.5), Inches(0.3), Inches(5), Inches(0.5),
       "Competition", size=28, bold=True, color=DARK)

    # 4-layer map (compact)
    layers = [
        ("SUBSTITUTES\n(post-hoc monitoring)",
         ["Arize AI ($131M)", "Arthur AI ($63M)", "Patronus AI ($17M)", "LangSmith, W&B"],
         "Detect, explain, report. Reactive paradigm.",
         ACCENT),
        ("DIRECT\n(structured meaning)",
         ["Expert.ai", "Sinequa", "Diffbot", "RelationalAI, spaCy"],
         "Fragmented. None deliver full deterministic package.",
         TEAL),
        ("INDIRECT\n(probabilistic paradigm)",
         ["OpenAI, Anthropic", "Google, Cohere", "Pinecone / Weaviate"],
         "Dominant approach. Non-deterministic by nature.",
         PURPLE),
        ("STATUS QUO\n(strongest competitor)",
         ["Manual review", "Spreadsheets, keyword search", "\"Good enough\" ChatGPT"],
         "Free. Trusted. Already everywhere. Zero switching cost.",
         ORANGE),
    ]

    x = Inches(0.5)
    col_w = Inches(3.0)
    for title, players, note, clr in layers:
        rect(sl, x, Inches(1.0), col_w, Inches(0.55), fill=clr)
        tb(sl, x, Inches(1.02), col_w, Inches(0.5),
           title, size=8, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

        rect(sl, x, Inches(1.55), col_w, Inches(1.8),
             fill=SECTION_BG, border=clr)
        tb(sl, x + Pt(6), Inches(1.6), col_w - Pt(12), Inches(1.2),
           ["• " + p for p in players], size=9, color=DARK)
        tb(sl, x + Pt(6), Inches(2.85), col_w - Pt(12), Inches(0.4),
           note, size=7, bold=True, color=clr)
        x += col_w + Inches(0.15)

    # Competitive advantage block
    rect(sl, Inches(0.5), Inches(3.6), Inches(12.5), Inches(1.7), fill=DARK)
    adv_text = (
        "HESPERIA's advantage is structural, not incremental. While competitors monitor or explain "
        "probabilistic AI outputs after the fact, HESPERIA produces stable, auditable meaning by design. "
        "The engine is deterministic — same input, same output, every time — with evidence traces and "
        "trust tiers in every result. This shifts the paradigm from observing AI behavior to defining AI meaning. "
        "Competitors optimize uncertainty; HESPERIA eliminates it at the source."
    )
    tb(sl, Inches(0.7), Inches(3.7), Inches(12.1), Inches(0.3),
       "COMPETITIVE ADVANTAGE", size=11, bold=True, color=ACCENT)
    tb(sl, Inches(0.7), Inches(4.05), Inches(12.1), Inches(1.1),
       adv_text, size=10, color=WHITE)

    # Positioning line
    rect(sl, Inches(0.5), Inches(5.6), Inches(12.5), Inches(0.85), fill=ACCENT)
    tb(sl, Inches(1), Inches(5.7), Inches(11.5), Inches(0.6),
       "\"Others monitor unstable AI outputs.  HESPERIA produces stable, auditable meaning by design.\"",
       size=16, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

    # Grading matrix (compact, bottom) — 1-4 scale per assignment
    matrix_rows = [
        ("", "HESP", "Arize", "Arthur", "Patron.", "Status Q."),
        ("Product depth", "4", "3", "2", "2", "1"),
        ("Explainability", "4", "2", "2", "1", "2"),
        ("Differentiation", "4", "2", "2", "2", "1"),
        ("Deterministic", "4", "1", "1", "1", "1"),
        ("Compliance", "3", "2", "3", "2", "2"),
        ("Brand", "1", "3", "2", "2", "1"),
        ("Resources", "1", "4", "3", "2", "1"),
        ("TOTAL (12 criteria)", "29", "32", "26", "24", "28"),
    ]

    tbl_x = Inches(0.5)
    tbl_y = Inches(6.6)
    cw = [Inches(1.8), Inches(0.8), Inches(0.8), Inches(0.8), Inches(0.8), Inches(0.9)]
    rh = Inches(0.1)

    for ri, row in enumerate(matrix_rows):
        cx = tbl_x
        is_header = ri == 0
        is_total = ri == len(matrix_rows) - 1
        bg = DARK if (is_header or is_total) else (SECTION_BG if ri % 2 == 0 else WHITE)
        txt_color = WHITE if (is_header or is_total) else DARK
        for ci, val in enumerate(row):
            rect(sl, cx, tbl_y, cw[ci], Inches(0.11), fill=bg, border=BORDER, bw=Pt(0.2))
            bld = is_header or is_total or (ci == 1 and not is_header)
            tb(sl, cx, tbl_y - Pt(1), cw[ci], Inches(0.11),
               val, size=5, bold=bld, color=txt_color,
               align=PP_ALIGN.CENTER if ci > 0 else PP_ALIGN.LEFT)
            cx += cw[ci]
        tbl_y += Inches(0.1)

    prs.save("/data/hesperia/Upcelerator2026/Assignment-2D_Pitch-Deck.pptx")
    print("DONE: D.PitchDeck.pptx")


if __name__ == "__main__":
    build()
