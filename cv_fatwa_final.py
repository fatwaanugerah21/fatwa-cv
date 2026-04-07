from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle, KeepTogether
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUTPUT = "./Fatwa_Anugerah_CV_Final.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    leftMargin=18*mm,
    rightMargin=18*mm,
    topMargin=14*mm,
    bottomMargin=14*mm,
)

DARK   = colors.HexColor("#1A1A2E")
ACCENT = colors.HexColor("#0F3460")
MUTED  = colors.HexColor("#4A5568")

def s(name, **kw):
    base = getSampleStyleSheet()[name]
    return ParagraphStyle(name + "_custom", parent=base, **kw)

name_style        = s("Normal", fontName="Helvetica-Bold", fontSize=22, textColor=DARK, leading=26, spaceAfter=1)
title_style       = s("Normal", fontName="Helvetica", fontSize=11, textColor=ACCENT, leading=14, spaceAfter=2)
contact_style     = s("Normal", fontName="Helvetica", fontSize=8.5, textColor=MUTED, leading=12, spaceAfter=0)
section_hdr       = s("Normal", fontName="Helvetica-Bold", fontSize=10, textColor=ACCENT, leading=14, spaceBefore=10, spaceAfter=2)
body_style        = s("Normal", fontName="Helvetica", fontSize=9, textColor=DARK, leading=13, spaceAfter=2)
bullet_style      = s("Normal", fontName="Helvetica", fontSize=9, textColor=DARK, leading=13, leftIndent=10, spaceAfter=1.5)
job_title_style   = s("Normal", fontName="Helvetica-Bold", fontSize=9.5, textColor=DARK, leading=13, spaceAfter=0)
job_meta_style    = s("Normal", fontName="Helvetica-Oblique", fontSize=8.5, textColor=MUTED, leading=12, spaceAfter=3)
skills_label      = s("Normal", fontName="Helvetica-Bold", fontSize=8.5, textColor=DARK, leading=13)
skills_value      = s("Normal", fontName="Helvetica", fontSize=8.5, textColor=DARK, leading=13)
project_title     = s("Normal", fontName="Helvetica-Bold", fontSize=9, textColor=ACCENT, leading=13, spaceAfter=0)

def section(title):
    return [
        Paragraph(title.upper(), section_hdr),
        HRFlowable(width="100%", thickness=0.8, color=ACCENT, spaceAfter=4)
    ]

def bullet(text):
    return Paragraph(f"• {text}", bullet_style)

def skill_row(label, value):
    return Table(
        [[Paragraph(label, skills_label), Paragraph(value, skills_value)]],
        colWidths=[42*mm, 128*mm],
        style=TableStyle([
            ("VALIGN", (0,0), (-1,-1), "TOP"),
            ("LEFTPADDING", (0,0), (-1,-1), 0),
            ("RIGHTPADDING", (0,0), (-1,-1), 0),
            ("TOPPADDING", (0,0), (-1,-1), 1),
            ("BOTTOMPADDING", (0,0), (-1,-1), 1),
        ])
    )

story = []

# ── HEADER ───────────────────────────────────────────────────────
story.append(Paragraph("FATWA ANUGERAH NASIR", name_style))
story.append(Paragraph("Senior Software Engineer · Remote (APAC, EU &amp; Global)", title_style))
story.append(Paragraph(
    "Indonesia &nbsp;|&nbsp; fatwaanugerah0421@gmail.com",
    contact_style))
story.append(Paragraph(
    "https://fatwa.ftsdigihouse.com &nbsp;|&nbsp; https://linkedin.com/in/fatwa-anugerah &nbsp;|&nbsp; https://github.com/fatwaanugerah21",
    contact_style))
story.append(Spacer(1, 6))
story.append(HRFlowable(width="100%", thickness=1.2, color=DARK, spaceAfter=6))

# ── PROFESSIONAL SUMMARY ─────────────────────────────────────────
story += section("Professional Summary")
story.append(Paragraph(
    "Senior Software Engineer with 5 years of experience designing and delivering end-to-end software systems "
    "— from scalable backend services and real-time architectures to production web and mobile applications "
    "— for global remote teams. Core strength in <b>backend engineering</b>: distributed systems, real-time data "
    "pipelines, API design, and cloud-native deployments across AWS, Azure, and GCP using <b>Go, TypeScript, "
    "and Node.js</b>. Complemented by hands-on delivery of full-stack products with "
    "<b>React.js, Next.js, React Native, and Flutter</b>. Proven track record of:",
    body_style))
story += section("Experience")

block1 = [
    Paragraph("Senior Software Engineer — AVASO Technology Solutions", job_title_style),
    Paragraph("Sep 2022 – Feb 2026 &nbsp;|&nbsp; Remote", job_meta_style),
    bullet("Designed, deployed, and maintained <b>15+ automated trading bots</b> performing real-time market data ingestion and automated order execution across multiple exchanges, processing <b>$2M+ in monthly trading volume</b>."),
    bullet("Engineered <b>WebSocket-based real-time infrastructure</b> supporting high concurrent connections with sub-100ms latency, enabling high-frequency data delivery."),
    bullet("Architected a concurrent backtesting engine leveraging <b>Node.js worker_threads</b> to parallelize strategy simulation across all available CPU cores, processing multi-year OHLCV datasets in a fraction of single-threaded time."),
    bullet("Designed and developed scalable backend services in <b>TypeScript</b> and <b>Go</b>, handling real-time data streams, order execution, and risk management logic."),
    bullet("Delivered end-to-end features across the stack — from API design and backend logic to web and mobile interfaces built with <b>React.js, Next.js, React Native, and Flutter</b>."),
    bullet("Optimised <b>SQL database</b> schemas and query execution plans for performance and integrity across high-throughput production environments."),
    bullet("Containerised and deployed production workloads on <b>Azure</b> using Docker Compose and automated <b>CI/CD pipelines</b>, ensuring zero-downtime releases."),
    bullet("Led and mentored a team of engineers, shaping architecture decisions, enforcing code quality standards, and accelerating team delivery velocity."),
    Spacer(1, 5),
]
story.append(KeepTogether(block1))

# Job 2 — SDConnect.VN — reorder: backend/infra bullets first
block2 = [
    Paragraph("Full Stack Developer — SDConnect.VN", job_title_style),
    Paragraph("Jan 2022 – Sep 2022 &nbsp;|&nbsp; Remote", job_meta_style),
    bullet("Architected <b>Redis-backed caching and query optimisation pipelines</b>, reducing average API response latency by <b>40%</b> and database response time by <b>55%</b> under production load on GCP."),
    bullet("Replaced REST polling with <b>WebSocket-driven communication</b>, enabling sub-100ms real-time data exchange between client and server and eliminating latency bottlenecks."),
    bullet("Owned features end-to-end — from API contracts and backend logic to frontend delivery — reducing feature delivery time by <b>35%</b> through standardised reusable component libraries."),
    bullet("Accelerated frontend rendering performance by <b>60%</b>, reducing initial load time from 4s to under 1.5s via code splitting, lazy loading, and asset optimisation."),
    Spacer(1, 5),
]
story.append(KeepTogether(block2))

# Job 3 — Emolyze.Tech — backend bullets first
block3 = [
    Paragraph("Junior Full Stack Engineer — Emolyze.Tech", job_title_style),
    Paragraph("Feb 2021 – Jan 2022 &nbsp;|&nbsp; Remote", job_meta_style),
    bullet("Engineered a <b>REST API integration layer from zero</b> to unify third-party data sources into existing client systems, improving data consistency and access speed."),
    bullet("Constructed an <b>internal analytics dashboard from scratch</b>, delivering real-time visibility into client KPIs and eliminating manual reporting workflows."),
    bullet("Built backend services with <b>Express.js, Redis, and MySQL</b>, and developed responsive web applications using <b>Next.js</b> and TailwindCSS."),
    bullet("Deployed and managed containerized applications on <b>AWS</b> using Docker, while establishing foundational <b>CI/CD pipelines</b> to streamline the engineering team's deployment workflow."),
    Spacer(1, 5),
]
story.append(KeepTogether(block3))

# ── CORE TECHNICAL SKILLS ────────────────────────────────────────
story += section("Core Technical Skills")
story.append(skill_row("Languages:",        "Go, TypeScript, JavaScript, Java, Python, Dart"))
story.append(skill_row("Backend & APIs:",   "Gin, Gorm, Node.js, Express.js, Fastify, REST, GraphQL, WebSocket, WebRTC, API Contracts"))
story.append(skill_row("Frontend & Mobile:","React.js, Next.js, React Native, Flutter, TailwindCSS"))
story.append(skill_row("Databases:",        "PostgreSQL, MySQL, Redis, NoSQL, Query Optimisation"))
story.append(skill_row("Architecture:",     "Distributed Systems, Event-Driven, Microservices, Real-time Systems, Concurrent Processing"))
story.append(skill_row("Cloud & DevOps:",   "AWS, GCP, Azure, Docker, Kubernetes, GitHub Actions, CI/CD, NGINX, Linux"))
story.append(skill_row("Tools & Process:",  "Git, Bun, Agile / Scrum, Figma"))

# ── KEY PROJECTS ─────────────────────────────────────────────────
story += section("Key Projects")

story.append(Paragraph("Automated Trading Bot Platform &nbsp;|&nbsp; <i>Go, TypeScript, Node.js, WebSocket, PostgreSQL</i>", project_title))
story.append(bullet("Designed and maintained a fleet of <b>15+ trading bots</b> with real-time market data ingestion, order execution, and risk management logic across multiple crypto exchanges."))
story.append(bullet("Built monitoring dashboards and alerting systems to ensure uptime and trading accuracy, processing <b>$2M+ in monthly trading volume</b>."))
story.append(Spacer(1, 4))

story.append(Paragraph("Backtesting Platform &nbsp;|&nbsp; <i>Node.js, worker_threads, WebSocket, TypeScript, React.js</i>", project_title))
story.append(bullet("Architected a high-performance backtesting engine utilizing <b>Node.js worker_threads</b> to parallelize strategy simulation across all available CPU cores, processing multi-year OHLCV candle data in a fraction of single-threaded time."))
story.append(bullet("Built the full-stack platform end-to-end — from the concurrent backend engine to a <b>React.js dashboard</b> with real-time <b>WebSocket</b> streaming of key trading metrics (Sharpe ratio, max drawdown, win rate)."))
story.append(Spacer(1, 4))

story.append(Paragraph("Privacy Chat App &nbsp;|&nbsp; <i>TypeScript, WebSocket, End-to-End Encryption, Flutter</i>", project_title))
story.append(Paragraph("github.com/fatwaanugerah21/privacy-chat-app", job_meta_style))
story.append(bullet("Architected a secure, privacy-first cross-platform chat application (Android &amp; iOS) with end-to-end encrypted messaging."))
story.append(bullet("Implemented real-time 1-to-1 messaging via <b>WebSocket</b> with <b>FCM push-notification fallback</b> for offline delivery reliability."))
story.append(Spacer(1, 3))

# ── EDUCATION ────────────────────────────────────────────────────
story += section("Education")
story.append(Paragraph("Bachelor of Computer Science — Hasanuddin University", job_title_style))
story.append(Paragraph("2019 – 2023 &nbsp;|&nbsp; GPA: 3.54 / 4.00", job_meta_style))
story.append(bullet("Relevant Coursework: Algorithms &amp; Data Structures, Distributed Systems, Database Systems, Software Engineering, Computer Networks"))

# ── LANGUAGES ────────────────────────────────────────────────────
story += section("Languages")
story.append(skill_row("Indonesian:", "Native"))
story.append(skill_row("English:",    "Fluent (Professional Working Proficiency)"))

# ── WORK PREFERENCES ─────────────────────────────────────────────
story += section("Work Preferences")
story.append(bullet("Fully Remote — APAC, EU &amp; Global startups preferred"))
story.append(bullet("Open to async &amp; cross-timezone collaboration (APAC, EU, US timezones)"))
story.append(bullet("Fluent English communication — experienced with international distributed teams"))
story.append(bullet("Immediately available"))

doc.build(story)
print("Done:", OUTPUT)
