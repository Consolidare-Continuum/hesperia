"""Generate HESPERIA Business Model Canvas PPTX aligned with Upcelerator template."""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

DARK = RGBColor(0x1A, 0x1A, 0x2E)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
ACCENT = RGBColor(0x00, 0x7A, 0xCC)
LIGHT_BG = RGBColor(0xF5, 0xF7, 0xFA)
GRID_BG = RGBColor(0xFF, 0xFF, 0xFF)
BORDER_COLOR = RGBColor(0xCC, 0xCC, 0xCC)
HEADER_BG = RGBColor(0x00, 0x7A, 0xCC)
SECTION_BG = RGBColor(0xF0, 0xF4, 0xF8)

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)


def add_text_box(slide, left, top, width, height, text, font_size=10,
                 bold=False, color=DARK, alignment=PP_ALIGN.LEFT,
                 font_name="Calibri", bg_color=None, anchor=MSO_ANCHOR.TOP):
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
            if i == 0:
                p = tf.paragraphs[0]
            else:
                p = tf.add_paragraph()
            p.text = line
            p.font.size = Pt(font_size)
            p.font.bold = bold
            p.font.color.rgb = color
            p.font.name = font_name
            p.alignment = alignment
            p.space_after = Pt(2)
    else:
        p = tf.paragraphs[0]
        p.text = text
        p.font.size = Pt(font_size)
        p.font.bold = bold
        p.font.color.rgb = color
        p.font.name = font_name
        p.alignment = alignment

    return txBox


def add_rect(slide, left, top, width, height, fill_color=GRID_BG,
             border_color=BORDER_COLOR, border_width=Pt(0.75)):
    shape = slide.shapes.add_shape(1, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.color.rgb = border_color
    shape.line.width = border_width
    return shape


def build_pptx(output_path):
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H

    # ── Slide 1: Title ──
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank
    add_rect(slide, Inches(0), Inches(0), SLIDE_W, SLIDE_H, fill_color=DARK)

    add_text_box(slide, Inches(1), Inches(1.5), Inches(11), Inches(1.2),
                 "HESPERIA", font_size=48, bold=True, color=WHITE,
                 alignment=PP_ALIGN.CENTER)
    add_text_box(slide, Inches(1), Inches(2.7), Inches(11), Inches(0.8),
                 "Business Model Canvas", font_size=28, color=ACCENT,
                 alignment=PP_ALIGN.CENTER)
    add_text_box(slide, Inches(1), Inches(3.8), Inches(11), Inches(0.6),
                 "Deterministic Semantic Measurement & Governance for AI Pipelines",
                 font_size=16, color=WHITE, alignment=PP_ALIGN.CENTER)
    add_text_box(slide, Inches(1), Inches(5.2), Inches(11), Inches(0.8),
                 ["Upcelerator Phase 1 · Assignment N.2 · March 2026",
                  "Author: Igor Platonov · igareosh.com · prichindel.com"],
                 font_size=12, color=RGBColor(0xAA, 0xAA, 0xAA),
                 alignment=PP_ALIGN.CENTER)
    add_text_box(slide, Inches(1), Inches(6.2), Inches(11), Inches(0.5),
                 "Framework: Osterwalder & Pigneur (2009), Business Model Generation",
                 font_size=10, color=RGBColor(0x88, 0x88, 0x88),
                 alignment=PP_ALIGN.CENTER)

    # ── Slide 2: BMC Grid ──
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_rect(slide, Inches(0), Inches(0), SLIDE_W, SLIDE_H, fill_color=LIGHT_BG)

    add_text_box(slide, Inches(0.3), Inches(0.15), Inches(12.7), Inches(0.45),
                 "HESPERIA — Business Model Canvas", font_size=18, bold=True,
                 color=DARK, alignment=PP_ALIGN.LEFT)

    margin = Inches(0.3)
    grid_w = SLIDE_W - 2 * margin
    grid_h = Inches(6.5)
    grid_top = Inches(0.65)
    col_w = grid_w / 5
    row_top_h = Inches(3.25)
    row_bot_h = Inches(3.25)

    bmc_data = {
        "KEY PARTNERS": [
            "• LLM providers (OpenAI,",
            "  Anthropic, Google)",
            "• Cloud infra (Hetzner →",
            "  AWS/GCP at scale)",
            "• Moldova IT Park (7% tax,",
            "  2,725 companies)",
            "• Academic (UTM)",
            "• Accelerators (Upcelerator,",
            "  Tekwill, Startup Moldova)",
            "• Regional SI partners (future)",
        ],
        "KEY ACTIVITIES": [
            "• Engine development &",
            "  determinism maintenance",
            "• API operations (FastAPI,",
            "  Docker, schema versioning)",
            "• Customer pilots (6-10 wk)",
            "• Research & calibration",
            "• B2B direct sales",
            "• EU AI Act compliance",
        ],
        "KEY RESOURCES": [
            "• IP: sealed engine v0.5.1,",
            "  lexicon (Dict A/B), topology",
            "• Founder: full-stack engineer",
            "  + product architect",
            "• Dev infrastructure (CI/CD)",
            "• Bootstrap capital",
            "• Gold evaluation corpora",
        ],
        "VALUE PROPOSITION": [
            "Deterministic semantic",
            "measurement & governance",
            "for AI pipelines",
            "",
            "• Makes AI auditable,",
            "  traceable, accountable",
            "• Same input = same output",
            "• Evidence traces + trust tiers",
            "• 7 product lines, 14 metrics",
            "",
            "Niche: between symbolic AI,",
            "semantic search, & knowledge",
            "graphs — none deliver the",
            "full deterministic package",
        ],
        "CUSTOMER RELATIONSHIPS": [
            "• API self-service (primary)",
            "• Structured pilots (6-10 wk",
            "  with gold-set evaluation)",
            "• Enterprise contracts + SLA",
            "• Community & content",
            "",
            "Path: trial → API → pilot →",
            "  enterprise → upsell (TRIZ)",
        ],
        "CHANNELS": [
            "• Direct sales (founder-led,",
            "  Chisinau IT network)",
            "• API / developer portal",
            "• Content & thought leadership",
            "  (LinkedIn, conferences)",
            "• Partner channel (SI, future)",
            "• Enterprise outbound (scale)",
        ],
        "CUSTOMER SEGMENTS": [
            "B2B · 50-5,000+ employees",
            "€1M-€500M+ revenue",
            "",
            "BEACHHEAD (Yr 1-2):",
            "  Moldova: FinTech, banking,",
            "  AI-driven SaaS (50-100 cos)",
            "EXPANSION (Yr 2-3):",
            "  Romania → EU compliance",
            "  markets (~20K cos)",
            "REGIONAL (Yr 3-5):",
            "  Full EU enterprise",
            "",
            "Buyers: CTO, Head of AI/ML,",
            "Risk/Compliance Officers,",
            "Product Owners (AI systems)",
        ],
        "COST STRUCTURE": [
            "Value-driven (differentiation) · No GPU costs (deterministic, CPU-only)",
            "• Fixed: ~€2,000-2,500/mo (server, tools, founder opportunity cost)",
            "• Variable: pilot support time, compute scaling with customers",
            "• Year 1 burn: €24,000-36,000 (bootstrapped solo founder)",
            "• Break-even: 8-12 contracts @ €5,000-10,000/yr each",
        ],
        "REVENUE STREAMS": [
            "• Usage-based API: €0.05-0.20/document (tiered by volume)",
            "• Enterprise subscription: ACV €5,000-€20,000/yr (midpoint €10K)",
            "• TRIZ extension: +50-100% premium add-on (future)",
            "• On-premise license: €10,000-30,000/yr (regulated environments)",
            "• Yr 1: €25-100K → Yr 3: €0.8-1.5M → Yr 5: €2-4M",
        ],
    }

    # Row 1: 5 columns [Partners | Activities/Resources | Value Prop | Relationships/Channels | Segments]
    cells_row1 = [
        ("KEY PARTNERS", 0, 0, 1, 1),
        ("KEY ACTIVITIES", 1, 0, 1, 0.5),
        ("KEY RESOURCES", 1, 0.5, 1, 0.5),
        ("VALUE PROPOSITION", 2, 0, 1, 1),
        ("CUSTOMER RELATIONSHIPS", 3, 0, 1, 0.5),
        ("CHANNELS", 3, 0.5, 1, 0.5),
        ("CUSTOMER SEGMENTS", 4, 0, 1, 1),
    ]

    for label, col_idx, row_frac, col_span, row_span in cells_row1:
        left = margin + col_w * col_idx
        top = grid_top + row_top_h * row_frac
        w = col_w * col_span
        h = row_top_h * row_span

        add_rect(slide, left, top, w, h, fill_color=GRID_BG)

        add_rect(slide, left, top, w, Inches(0.3), fill_color=HEADER_BG)
        add_text_box(slide, left, top, w, Inches(0.3),
                     label, font_size=8, bold=True, color=WHITE,
                     alignment=PP_ALIGN.CENTER)

        content = bmc_data.get(label, [])
        fs = 7 if len(content) > 10 else 8
        add_text_box(slide, left + Pt(2), top + Inches(0.32),
                     w - Pt(4), h - Inches(0.35),
                     content, font_size=fs, color=DARK)

    # Row 2: Cost Structure (left half) + Revenue Streams (right half)
    bot_top = grid_top + row_top_h
    half_w = grid_w / 2

    for i, label in enumerate(["COST STRUCTURE", "REVENUE STREAMS"]):
        left = margin + half_w * i
        add_rect(slide, left, bot_top, half_w, row_bot_h,
                 fill_color=GRID_BG)
        add_rect(slide, left, bot_top, half_w, Inches(0.3),
                 fill_color=HEADER_BG)
        add_text_box(slide, left, bot_top, half_w, Inches(0.3),
                     label, font_size=8, bold=True, color=WHITE,
                     alignment=PP_ALIGN.CENTER)
        content = bmc_data[label]
        add_text_box(slide, left + Pt(4), bot_top + Inches(0.32),
                     half_w - Pt(8), row_bot_h - Inches(0.35),
                     content, font_size=8, color=DARK)

    add_text_box(slide, margin, SLIDE_H - Inches(0.3), grid_w, Inches(0.25),
                 "Osterwalder & Pigneur (2009) · businessmodelgeneration.com · Hesperia Engine Dynamics v0.5 · igareosh.com",
                 font_size=7, color=RGBColor(0x99, 0x99, 0x99),
                 alignment=PP_ALIGN.CENTER)

    # ── Slide 3: Value Proposition Deep Dive ──
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_rect(slide, Inches(0), Inches(0), SLIDE_W, SLIDE_H, fill_color=WHITE)

    add_text_box(slide, Inches(0.5), Inches(0.3), Inches(12), Inches(0.5),
                 "Value Proposition — What Hesperia Solves", font_size=24,
                 bold=True, color=DARK)

    problems = [
        ("Black-Box AI Outputs",
         "LLM outputs are non-deterministic. Specialists cannot verify or audit what AI produces. "
         "Hesperia maps text into stable structural classes (10 macro domains, 240 policy families) "
         "with evidence traces and trust tiers. Same input + config = same output. Every time."),
        ("Semantic Drift in AI Pipelines",
         "AI outputs drift silently over time (model updates, prompt changes, context shifts). "
         "Hesperia stores structural vectors over time, tracks divergence from baselines, "
         "and triggers alerts when drift exceeds thresholds."),
        ("Compliance & Audit Requirements",
         "EU AI Act and enterprise governance require traceability of AI-assisted decisions. "
         "Hesperia provides sealed runtime with public audit manifests — version, checksum, "
         "evidence count — for every output."),
        ("Text Measurement Before Human Review",
         "Specialists spend excessive time on documents that could be pre-screened. "
         "Structural measurement (density, coherence, complexity, contradiction detection) "
         "enables automated triage before human review."),
    ]

    y = Inches(1.1)
    for title, desc in problems:
        add_rect(slide, Inches(0.5), y, Inches(12.3), Inches(1.3),
                 fill_color=SECTION_BG, border_color=ACCENT)
        add_text_box(slide, Inches(0.7), y + Inches(0.05), Inches(11.8), Inches(0.35),
                     title, font_size=13, bold=True, color=ACCENT)
        add_text_box(slide, Inches(0.7), y + Inches(0.4), Inches(11.8), Inches(0.85),
                     desc, font_size=10, color=DARK)
        y += Inches(1.45)

    add_text_box(slide, Inches(0.5), Inches(6.9), Inches(12), Inches(0.4),
                 "Position: between symbolic AI (Expert.ai), semantic search (Sinequa), knowledge graphs (Diffbot, RelationalAI). None deliver the full deterministic package.",
                 font_size=10, bold=True, color=RGBColor(0x55, 0x55, 0x55),
                 alignment=PP_ALIGN.CENTER)

    # ── Slide 4: Customer Segments & Market Sizing ──
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_rect(slide, Inches(0), Inches(0), SLIDE_W, SLIDE_H, fill_color=WHITE)

    add_text_box(slide, Inches(0.5), Inches(0.3), Inches(12), Inches(0.5),
                 "Customer Segments & Market Sizing", font_size=24,
                 bold=True, color=DARK)

    segments = [
        ("BEACHHEAD — Moldova (Year 1-2)",
         "50-100 IT Park companies deploying AI in production. "
         "Verticals: FinTech, banking, AI-driven SaaS. "
         "Buyer: CTO, Head of AI/ML. ACV: €5-10K. Target: €1M ARR at 100.",
         ACCENT),
        ("EXPANSION — Romania → EU (Year 2-3)",
         "EU markets with strict compliance (Romania, DACH, Nordics). "
         "~20,000 relevant companies with regulatory/financial AI risk. "
         "Buyer: CTO, Risk/Compliance Officers. ACV: €10-20K.",
         RGBColor(0x00, 0x96, 0x88)),
        ("REGIONAL — Full EU / Enterprise (Year 3-5)",
         "FinTech, insurance, healthcare, legal, public sector. "
         "Part of €5B+ addressable market (industry: $10-15B+). "
         "Target: €2-4M revenue, 200+ customers.",
         RGBColor(0x7B, 0x1F, 0xA2)),
    ]

    y = Inches(1.1)
    for title, desc, clr in segments:
        add_rect(slide, Inches(0.5), y, Inches(5.8), Inches(1.6),
                 fill_color=SECTION_BG, border_color=clr)
        add_text_box(slide, Inches(0.7), y + Inches(0.05), Inches(5.4), Inches(0.35),
                     title, font_size=12, bold=True, color=clr)
        add_text_box(slide, Inches(0.7), y + Inches(0.4), Inches(5.4), Inches(1.1),
                     desc, font_size=9, color=DARK)
        y += Inches(1.75)

    # Market sizing box (right side)
    add_rect(slide, Inches(6.8), Inches(1.1), Inches(6), Inches(5.7),
             fill_color=DARK)
    market_lines = [
        "MARKET SIZING (bottom-up)",
        "",
        "TAM (bottom-up: 500K cos × €10K):",
        "  €5B",
        "  Industry context: $10-15B+",
        "  AI governance sub-segment: $2.5-3.4B",
        "",
        "SAM (EU + Eastern Europe, compliance):",
        "  ~20,000 companies × €10K ACV",
        "  = €200M",
        "",
        "SOM (Year 1-3, 50-200 companies):",
        "  100 × €10,000 = €1M ARR",
        "",
        "TAM is irrelevant for execution.",
        "SOM defines strategy.",
        "",
        "─────────────────────────────",
        "",
        "Moldova IT Park (2025):",
        "  2,725 cos · $1B turnover · 25K+ staff",
        "",
        "Romania (2025):",
        "  IT = 7% GDP · 5.2% AI adoption",
        "  Budgets shifting to AI + compliance",
    ]
    add_text_box(slide, Inches(7.0), Inches(1.2), Inches(5.5), Inches(5.4),
                 market_lines, font_size=10, color=WHITE)

    # ── Slide 5: Competitive Positioning ──
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_rect(slide, Inches(0), Inches(0), SLIDE_W, SLIDE_H, fill_color=WHITE)

    add_text_box(slide, Inches(0.5), Inches(0.3), Inches(12), Inches(0.5),
                 "Competitive Positioning — Reality Check", font_size=24,
                 bold=True, color=DARK)

    add_text_box(slide, Inches(0.5), Inches(0.9), Inches(12), Inches(0.5),
                 "No clean direct competitors. Hesperia sits at the intersection of three established categories:",
                 font_size=12, color=RGBColor(0x55, 0x55, 0x55))

    competitors = [
        ("Sinequa", "Semantic search + NLP engine",
         "Meaning extraction, enterprise reliability, ontology structures",
         "Not deterministic; probabilistic + heuristic-heavy",
         ACCENT),
        ("Expert.ai", "Symbolic / rule-based NLP",
         "Closest philosophy: structured meaning > generation, explainability",
         "Legacy architecture, less strict determinism",
         RGBColor(0x00, 0x96, 0x88)),
        ("Cogito Tech", "Semantic annotation + meaning layers",
         "Text → structured representation, data labeling",
         "Service-heavy (not engine), no unified deterministic system",
         RGBColor(0x7B, 0x1F, 0xA2)),
        ("RelationalAI", "Structured reasoning over data",
         "Deterministic reasoning layer, logic + relationships",
         "Not text-native; requires structured inputs first",
         RGBColor(0xE6, 0x5C, 0x00)),
        ("Diffbot", "Text → structured knowledge graph",
         "Entity + relationship extraction at scale",
         "Extraction-focused, no semantic dynamics or governance",
         RGBColor(0xC6, 0x28, 0x28)),
    ]

    y = Inches(1.5)
    for name, desc, overlap, diff, clr in competitors:
        add_rect(slide, Inches(0.5), y, Inches(7.5), Inches(0.95),
                 fill_color=SECTION_BG, border_color=clr)
        add_text_box(slide, Inches(0.65), y + Inches(0.02), Inches(1.8), Inches(0.25),
                     name, font_size=10, bold=True, color=clr)
        add_text_box(slide, Inches(2.5), y + Inches(0.02), Inches(5.3), Inches(0.25),
                     desc, font_size=9, color=RGBColor(0x55, 0x55, 0x55))
        add_text_box(slide, Inches(0.65), y + Inches(0.3), Inches(7.1), Inches(0.25),
                     "Overlap: " + overlap, font_size=8, color=DARK)
        add_text_box(slide, Inches(0.65), y + Inches(0.58), Inches(7.1), Inches(0.35),
                     "Gap: " + diff, font_size=8, bold=True, color=clr)
        y += Inches(1.05)

    add_rect(slide, Inches(8.5), Inches(1.5), Inches(4.5), Inches(5.3),
             fill_color=DARK)
    wedge_lines = [
        "HESPERIA'S WEDGE",
        "",
        "What none of them deliver:",
        "",
        "✓ Deterministic structural",
        "  placement (hash-verifiable)",
        "",
        "✓ Sealed projection +",
        "  public-safe output gate",
        "",
        "✓ Topology-aware propagation",
        "  (icosahedral 12-node graph)",
        "",
        "✓ Evidence traces with",
        "  confidence bands",
        "",
        "✓ Trust tiers for automated",
        "  vs. human-review routing",
        "",
        "✓ 7 product lines from",
        "  one deterministic engine",
        "",
        "Position: enhancer / middleware",
        "Not a competitor to any of them",
    ]
    add_text_box(slide, Inches(8.7), Inches(1.6), Inches(4.1), Inches(5.0),
                 wedge_lines, font_size=9, color=WHITE)

    # ── Slide 6: Full Competitive Landscape Map ──
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_rect(slide, Inches(0), Inches(0), SLIDE_W, SLIDE_H, fill_color=WHITE)

    add_text_box(slide, Inches(0.3), Inches(0.2), Inches(8), Inches(0.45),
                 "Competitive Landscape — Full Map", font_size=22,
                 bold=True, color=DARK)
    add_text_box(slide, Inches(0.3), Inches(0.6), Inches(9), Inches(0.35),
                 "JTBD: Convert text into stable, auditable, structured meaning for decision-making and automation.",
                 font_size=9, bold=True, color=ACCENT)

    TEAL = RGBColor(0x00, 0x96, 0x88)
    PURPLE = RGBColor(0x7B, 0x1F, 0xA2)
    ORANGE = RGBColor(0xE6, 0x5C, 0x00)
    SLATE = RGBColor(0x54, 0x6E, 0x7A)

    layer_colors = [ACCENT, TEAL, PURPLE, ORANGE]
    layers = [
        ("DIRECT — same job, similar approach", ACCENT, [
            ("Expert.ai", "Rule-based NLP + knowledge graphs. Gap: weaker stability, less strict aggregation"),
            ("Sinequa", "Deep semantic indexing + enterprise reasoning. Gap: heuristic/probabilistic core"),
            ("Diffbot", "Text → entities → knowledge graph. Gap: extraction-focused, no dynamics engine"),
            ("RelationalAI", "Deterministic reasoning over structured data. Gap: not text-native"),
            ("spaCy / CoreNLP", "Components for custom pipelines. Gap: not a governed semantic system"),
        ]),
        ("INDIRECT — same job, probabilistic paradigm", TEAL, [
            ("OpenAI (GPT)", "General reasoning. Tradeoff: non-deterministic, drift, hallucinations"),
            ("Anthropic (Claude)", "Safety-tuned LLMs. Tradeoff: still probabilistic"),
            ("Google (Gemini)", "Multimodal reasoning. Tradeoff: no auditability guarantees"),
            ("Cohere", "Enterprise NLP APIs. Tradeoff: output variability remains"),
            ("Pinecone / Weaviate", "RAG retrieval layer. Tradeoff: similarity ≠ meaning"),
        ]),
        ("SUBSTITUTES — same pain, post-hoc solution", PURPLE, [
            ("Arize AI", "Drift detection, LLM evals — monitor after the fact"),
            ("Arthur AI", "Bias, explainability, compliance — control, not structure"),
            ("Patronus AI", "Hallucination detection, guardrails — patch instability"),
            ("LangSmith", "Prompt tracing, debugging — observability layer"),
            ("Weights & Biases", "Evaluation / monitoring workflows — experiment tracking"),
        ]),
        ("STATUS QUO — strongest real competitor", ORANGE, [
            ("Human workflows", "Analysts reading docs manually, compliance review, domain expert judgment"),
            ("Simple tooling", "Excel tagging, keyword search (Elastic), internal taxonomies"),
            ("\"Good enough\" LLM", "ChatGPT + prompts, basic RAG pipelines, accepting occasional errors"),
        ]),
    ]

    col_w = Inches(3.1)
    col_gap = Inches(0.1)
    start_x = Inches(0.3)
    start_y = Inches(1.0)
    col_h = Inches(4.65)
    header_h = Inches(0.55)

    for i, (title, clr, entries) in enumerate(layers):
        x = start_x + i * (col_w + col_gap)

        add_rect(slide, x, start_y, col_w, header_h, fill_color=clr)
        short_title = title.split("—")[0].strip()
        subtitle = title.split("—")[1].strip() if "—" in title else ""
        add_text_box(slide, x, start_y + Pt(1), col_w, Inches(0.25),
                     short_title, font_size=9, bold=True, color=WHITE,
                     alignment=PP_ALIGN.CENTER)
        add_text_box(slide, x, start_y + Inches(0.22), col_w, Inches(0.3),
                     subtitle, font_size=7, color=WHITE,
                     alignment=PP_ALIGN.CENTER)

        body_top = start_y + header_h + Pt(2)
        entry_h = (col_h - header_h) / max(len(entries), 1)

        for j, (name, desc) in enumerate(entries):
            ey = body_top + entry_h * j
            add_rect(slide, x, ey, col_w, entry_h - Pt(2),
                     fill_color=SECTION_BG, border_color=clr,
                     border_width=Pt(0.5))
            add_text_box(slide, x + Pt(4), ey + Pt(1), col_w - Pt(8), Inches(0.2),
                         name, font_size=8, bold=True, color=clr)
            add_text_box(slide, x + Pt(4), ey + Inches(0.2), col_w - Pt(8),
                         entry_h - Inches(0.22),
                         desc, font_size=7, color=DARK)

    # Strategic interpretation — bottom bar
    strat_top = Inches(5.75)
    add_rect(slide, Inches(0.3), strat_top, Inches(12.7), Inches(1.55),
             fill_color=DARK)

    left_lines = [
        "STRATEGIC READ",
        "",
        "Not a crowded same-product market.",
        "Split market: symbolic fragments vs probabilistic stack.",
        "Real fight is paradigm, not feature.",
        "",
        "  Them:  generate → evaluate → patch",
        "  You:   structure → stabilize → audit",
    ]
    add_text_box(slide, Inches(0.5), strat_top + Pt(4), Inches(5.5), Inches(1.4),
                 left_lines, font_size=8, color=WHITE)

    right_lines = [
        "WEDGE STRATEGY",
        "",
        "Start where auditability is non-negotiable",
        "(compliance, legal, finance).",
        "Replace a single decision workflow end-to-end.",
        "Prove: lower error + traceability + repeatability.",
        "",
        "Main risk: adoption friction.",
        "Substitutes are easier to bolt onto existing stacks.",
    ]
    add_text_box(slide, Inches(6.3), strat_top + Pt(4), Inches(3.7), Inches(1.4),
                 right_lines, font_size=8, color=WHITE)

    # Positioning line — right edge
    pos_lines = [
        "",
        "\"Others monitor unstable",
        " AI outputs.",
        "",
        " HESPERIA produces stable,",
        " auditable meaning",
        " by design.\"",
    ]
    add_text_box(slide, Inches(10.2), strat_top + Pt(2), Inches(2.7), Inches(1.45),
                 pos_lines, font_size=10, bold=True, color=ACCENT,
                 alignment=PP_ALIGN.CENTER)

    # ── Slide 7: Competitive Grading Matrix ──
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_rect(slide, Inches(0), Inches(0), SLIDE_W, SLIDE_H, fill_color=WHITE)

    add_text_box(slide, Inches(0.3), Inches(0.15), Inches(9), Inches(0.4),
                 "Competitive Grading Matrix (scale 1–4, per assignment)",
                 font_size=20, bold=True, color=DARK)

    GRAY = RGBColor(0x88, 0x88, 0x88)
    RED_ACCENT = RGBColor(0xC6, 0x28, 0x28)
    GREEN_ACC = RGBColor(0x2E, 0x7D, 0x32)

    matrix_data = [
        #  Criteria                       HESP  Arize Arthur Patron SQ
        ("Product (Quality / Depth)",       4,    3,    2,     2,    1),
        ("Price (Value for money)",         2,    2,    2,     3,    4),
        ("Ease of Use",                     2,    3,    2,     3,    4),
        ("Explainability / Auditability",   4,    2,    2,     1,    2),
        ("Brand",                           1,    3,    2,     2,    1),
        ("Distribution / Sales",            1,    3,    2,     2,    4),
        ("Resources (Capital / Team)",      1,    4,    3,     2,    1),
        ("Integration Capability",          1,    4,    3,     2,    3),
        ("Compliance Readiness",            3,    2,    3,     2,    2),
        ("Differentiation Strength",        4,    2,    2,     2,    1),
        ("Customer Trust Potential",        2,    3,    2,     2,    4),
        ("Deterministic Output",            4,    1,    1,     1,    1),
    ]

    totals = [0, 0, 0, 0, 0]
    for row in matrix_data:
        for c in range(5):
            totals[c] += row[c + 1]

    col_names = ["Criteria", "HESPERIA", "Arize AI\n$131M Ser.C", "Arthur AI\n$63M Ser.B",
                 "Patronus AI\n$17M Ser.A", "Status Quo\n(Manual)"]

    tbl_left = Inches(0.3)
    tbl_top = Inches(0.6)
    col_widths = [Inches(2.8), Inches(1.4), Inches(1.6), Inches(1.6), Inches(1.6), Inches(1.6)]
    row_h = Inches(0.32)
    header_row_h = Inches(0.45)

    header_top = tbl_top
    x = tbl_left
    for ci, name in enumerate(col_names):
        w = col_widths[ci]
        add_rect(slide, x, header_top, w, header_row_h, fill_color=DARK)
        add_text_box(slide, x, header_top + Pt(1), w, header_row_h,
                     name, font_size=7, bold=True, color=WHITE,
                     alignment=PP_ALIGN.CENTER if ci > 0 else PP_ALIGN.LEFT)
        x += w

    y = header_top + header_row_h
    for ri, row in enumerate(matrix_data):
        x = tbl_left
        bg = SECTION_BG if ri % 2 == 0 else WHITE
        for ci in range(6):
            w = col_widths[ci]
            add_rect(slide, x, y, w, row_h, fill_color=bg,
                     border_color=BORDER_COLOR, border_width=Pt(0.3))
            if ci == 0:
                add_text_box(slide, x + Pt(3), y, w - Pt(6), row_h,
                             row[0], font_size=7, color=DARK)
            else:
                val = row[ci]
                if ci == 1:
                    clr = GREEN_ACC if val >= 4 else (RED_ACCENT if val <= 2 else DARK)
                else:
                    clr = DARK
                add_text_box(slide, x, y, w, row_h,
                             str(val), font_size=8, bold=(ci == 1),
                             color=clr, alignment=PP_ALIGN.CENTER)
            x += w
        y += row_h

    # Totals row
    x = tbl_left
    total_labels = ["TOTAL"] + [str(t) for t in totals]
    for ci in range(6):
        w = col_widths[ci]
        add_rect(slide, x, y, w, Inches(0.35), fill_color=DARK)
        txt = total_labels[ci] if ci <= 5 else ""
        add_text_box(slide, x, y + Pt(1), w, Inches(0.35),
                     txt, font_size=9, bold=True, color=WHITE,
                     alignment=PP_ALIGN.CENTER if ci > 0 else PP_ALIGN.LEFT)
        x += w

    # Strategic insights (right side)
    insights_top = tbl_top
    insights_left = tbl_left + sum(col_widths) + Inches(0.2)
    insights_w = SLIDE_W - insights_left - Inches(0.3)

    add_rect(slide, insights_left, insights_top, insights_w, Inches(3.2),
             fill_color=DARK)
    insight_lines = [
        "STRATEGIC READ",
        "",
        "HESPERIA wins on:",
        "  Product, Explainability,",
        "  Differentiation, Determinism",
        "  → Structural advantages",
        "",
        "HESPERIA loses on:",
        "  Brand, Distribution, Resources,",
        "  Integration",
        "  → Execution gaps (close w/ time)",
        "",
        "STATUS QUO = real competitor (28).",
        "Fight is \"us vs doing nothing,\"",
        "not \"us vs Arize.\"",
    ]
    add_text_box(slide, insights_left + Pt(6), insights_top + Pt(4),
                 insights_w - Pt(12), Inches(3.1),
                 insight_lines, font_size=8, color=WHITE)

    add_rect(slide, insights_left, insights_top + Inches(3.3), insights_w,
             Inches(1.5), fill_color=SECTION_BG, border_color=ACCENT)
    corrections_lines = [
        "KEY INSIGHT:",
        "",
        "Status Quo scores 28 — nearly tied",
        "with HESPERIA (29). Already everywhere,",
        "free, trusted, zero switching cost.",
        "",
        "HESPERIA is honest about gaps:",
        "  Resources = 1 (solo founder)",
        "  Integration = 1 (no pre-built)",
        "  Customer Trust = 2 (unproven)",
        "",
        "Wedge: start where status quo",
        "fails — compliance, legal, finance.",
    ]
    add_text_box(slide, insights_left + Pt(6), insights_top + Inches(3.35),
                 insights_w - Pt(12), Inches(1.4),
                 corrections_lines, font_size=7, color=DARK)

    # Bottom bar — funding context
    bar_top = Inches(6.2)
    add_rect(slide, Inches(0.3), bar_top, Inches(12.7), Inches(1.1), fill_color=DARK)
    funding_lines = [
        "Competitor funding context:  Arize AI = $131M (Series C, 2025)  ·  Arthur AI = $63M (Series B, 2022)  ·  Patronus AI = $17M (Series A, 2024)  ·  HESPERIA = bootstrapped (solo founder)",
        "",
        "All three substitutes validate the market. None produce deterministic meaning — they monitor probabilistic instability after the fact.",
        "Adoption friction is the main risk. Substitutes are easier to bolt on. Wedge: start where auditability is non-negotiable (compliance, legal, finance).",
    ]
    add_text_box(slide, Inches(0.5), bar_top + Pt(4), Inches(12.3), Inches(1.0),
                 funding_lines, font_size=8, color=WHITE)

    # ── Slide 8: Revenue Model & Financials ──
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_rect(slide, Inches(0), Inches(0), SLIDE_W, SLIDE_H, fill_color=WHITE)

    add_text_box(slide, Inches(0.5), Inches(0.3), Inches(12), Inches(0.5),
                 "Revenue Streams & Cost Structure", font_size=24,
                 bold=True, color=DARK)

    rev_items = [
        ("Usage-Based API", "€0.05-0.20/document, tiered by volume. Low barrier to entry."),
        ("Enterprise Subscription", "ACV €5,000-€20,000/yr (midpoint €10K). Compliance + SLA."),
        ("TRIZ Extension", "+50-100% premium. Contradiction intelligence, innovation radar. Future."),
        ("On-Premise License", "€10,000-30,000/yr. Air-gapped / regulated environments."),
    ]

    y = Inches(1.1)
    for title, desc in rev_items:
        add_rect(slide, Inches(0.5), y, Inches(6), Inches(0.7),
                 fill_color=SECTION_BG, border_color=ACCENT)
        add_text_box(slide, Inches(0.7), y + Inches(0.02), Inches(2.5), Inches(0.3),
                     title, font_size=11, bold=True, color=ACCENT)
        add_text_box(slide, Inches(3.3), y + Inches(0.02), Inches(3.0), Inches(0.65),
                     desc, font_size=9, color=DARK)
        y += Inches(0.8)

    # Projection
    add_text_box(slide, Inches(0.5), Inches(4.5), Inches(6), Inches(0.4),
                 "Revenue Projection (conservative, bottom-up):",
                 font_size=12, bold=True, color=DARK)

    proj_lines = [
        "Year 1:  €25,000-100,000     (5-10 customers, Moldova)",
        "Year 2:  €200,000-500,000    (30-60 customers, MD + RO)",
        "Year 3:  €800,000-1,500,000  (80-120 customers, €1M ARR target)",
        "Year 5:  €2,000,000-4,000,000 (200+ customers, CEE/EU)",
    ]
    add_text_box(slide, Inches(0.7), Inches(4.9), Inches(5.8), Inches(1.5),
                 proj_lines, font_size=10, color=DARK)

    # Cost structure (right)
    add_rect(slide, Inches(7), Inches(1.1), Inches(5.8), Inches(5.5),
             fill_color=SECTION_BG, border_color=BORDER_COLOR)
    cost_lines = [
        "COST STRUCTURE",
        "",
        "Value-driven · No GPU costs",
        "(deterministic, CPU-only engine)",
        "",
        "Fixed costs (~€2,000-2,500/mo):",
        "  • Server: €50-200/mo",
        "  • Domain, tools, GitHub: ~€50/mo",
        "  • Founder opportunity cost: ~€1,500-2,000/mo",
        "  • Legal / IT Park registration: ~€500 one-time",
        "",
        "Variable costs:",
        "  • Pilot support (founder time, ~40h each)",
        "  • API compute (linear, minimal per-doc)",
        "  • Marketing: zero initially (organic)",
        "",
        "Year 1 burn rate: €24,000-36,000",
        "Year 2 (with 1 hire): €60,000-80,000",
        "",
        "Break-even: 8-12 contracts",
        "  @ €5,000-10,000/yr each",
        "",
        "Economies of scope: same engine",
        "serves all 7 product lines.",
    ]
    add_text_box(slide, Inches(7.2), Inches(1.2), Inches(5.4), Inches(5.2),
                 cost_lines, font_size=10, color=DARK)

    # ── Slide 6: Assumptions & Next Steps ──
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_rect(slide, Inches(0), Inches(0), SLIDE_W, SLIDE_H, fill_color=WHITE)

    add_text_box(slide, Inches(0.5), Inches(0.3), Inches(12), Inches(0.5),
                 "Assumptions to Validate & Next Steps", font_size=24,
                 bold=True, color=DARK)

    assumptions = [
        "1. Moldova IT companies building AI products need output measurement tooling.",
        "2. ACV of €5,000-€20,000/yr is acceptable for target B2B (Sinequa/Expert.ai price significantly higher).",
        "3. Determinism and auditability are valued over \"smarter\" non-reproducible alternatives.",
        "4. Founder can sell directly to 20-50 companies in Year 1 via IT Park network.",
        "5. EU AI Act creates compliance pressure that drives governance tooling purchases.",
        "6. Behind-the-curtain positioning (middleware) is understood by B2B buyers.",
        "7. The niche between symbolic AI, semantic search, and knowledge graphs is commercially viable.",
    ]
    add_text_box(slide, Inches(0.5), Inches(1.0), Inches(6), Inches(0.35),
                 "Key Assumptions (hypotheses, not forecasts):",
                 font_size=13, bold=True, color=ACCENT)
    add_text_box(slide, Inches(0.7), Inches(1.4), Inches(5.8), Inches(3.5),
                 assumptions, font_size=10, color=DARK)

    next_steps = [
        "→ Customer Development: 10-20 interviews with Moldova",
        "  IT company CTOs / lead developers (Assignment N.3).",
        "",
        "→ Validate willingness-to-pay: present pricing to",
        "  3-5 potential pilot customers.",
        "",
        "→ First pilot: structured 6-10 week deployment",
        "  with gold-set evaluation at 1 company.",
        "",
        "→ Refine BMC: return with validated data after",
        "  customer development interviews.",
        "",
        "→ Competitor deep dive: Sinequa, Expert.ai, Cogito",
        "  Tech, RelationalAI, Diffbot (Assignment N.2 §C).",
        "",
        "→ Validate niche positioning: confirm buyers see the",
        "  gap between symbolic AI / semantic search / KGs.",
    ]
    add_text_box(slide, Inches(7), Inches(1.0), Inches(5.8), Inches(0.35),
                 "Next Steps:", font_size=13, bold=True, color=ACCENT)
    add_text_box(slide, Inches(7.2), Inches(1.4), Inches(5.5), Inches(4),
                 next_steps, font_size=10, color=DARK)

    quote = (
        "\"The main difference between a startup and a traditional business is that a startup "
        "is in the process of discovering its business model, while a traditional business "
        "is executing and scaling the business model it has discovered.\""
    )
    add_rect(slide, Inches(0.5), Inches(5.5), Inches(12.3), Inches(1.2),
             fill_color=DARK)
    add_text_box(slide, Inches(1), Inches(5.6), Inches(11.3), Inches(1),
                 [quote, "", "— Osterwalder & Pigneur, Business Model Generation (2009)"],
                 font_size=11, color=WHITE, alignment=PP_ALIGN.CENTER)

    prs.save(output_path)
    print(f"DONE: {output_path}")


if __name__ == "__main__":
    build_pptx("/data/hesperia/Upcelerator2026/Assignment-2A_Business-Model-Canvas.pptx")
