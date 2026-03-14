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
story.append(Paragraph("Senior Full Stack Engineer · Remote (APAC, EU &amp; Global)", title_style))
story.append(Paragraph(
    "Indonesia &nbsp;|&nbsp; fatwaanugerah0421@gmail.com &nbsp;|&nbsp; "
    "linkedin.com/in/fatwa-anugerah &nbsp;|&nbsp; github.com/fatwaanugerah21",
    contact_style))
story.append(Spacer(1, 6))
story.append(HRFlowable(width="100%", thickness=1.2, color=DARK, spaceAfter=6))

# ── PROFESSIONAL SUMMARY ─────────────────────────────────────────
story += section("Professional Summary")
story.append(Paragraph(
    "Senior Full Stack Engineer with <b>5+ years of experience</b> architecting and delivering scalable web, "
    "mobile, and real-time systems for EU, APAC, and global companies. Specialised in <b>TypeScript, Javascript, "
    "Golang, Next.js, and Flutter</b>, with deep expertise in WebSocket-based architectures, automated trading systems, "
    "and cloud-native deployments across <b>AWS, GCP, and Azure</b>. Proven track record of:",
    body_style))
story.append(bullet("Leading full-stack platforms serving <b>100k+ users</b> with high availability and low latency"))
story.append(bullet("Architecting and maintaining <b>15+ automated trading bots</b> processing hundreds of thousands in monthly trading volume"))
story.append(bullet("Mentoring engineers and driving architecture decisions across distributed, remote-first teams"))
story.append(bullet("Delivering cloud-native solutions with <b>CI/CD pipelines</b> on Azure, GCP, and AWS for rapid, reliable deployment"))
story.append(Spacer(1, 3))

# ── PROFESSIONAL EXPERIENCE ──────────────────────────────────────
story += section("Professional Experience")

# Job 1 — Avasosoft
block1 = [
    Paragraph("Senior Software Engineer — Avasosoft Technology Solution", job_title_style),
    Paragraph("Sep 2022 – Feb 2026 &nbsp;|&nbsp; Remote", job_meta_style),
    bullet("Orchestrated full-stack development across multiple client platforms, architecting systems that scaled to serve <b>100k+ users</b> with high availability."),
    bullet("Designed, deployed, and maintained <b>15+ automated trading bots</b> processing hundreds of orders per month with hundreds of thousands in monthly trading volume."),
    bullet("Engineered <b>WebSocket-based real-time infrastructure</b> supporting high concurrent connections with sub-100ms latency, enabling mission-critical live data delivery."),
    bullet("Developed and scaled backend services using <b>TypeScript (Node.js)</b> and <b>Golang</b>; built modern frontend applications with <b>Next.js</b> and Shadcn UI."),
    bullet("Optimised <b>SQL database</b> schemas and query execution plans for performance and integrity across high-throughput production environments."),
    bullet("Containerised and deployed production workloads on <b>Azure</b> using Docker Compose and automated <b>CI/CD pipelines</b>, ensuring zero-downtime releases."),
    bullet("Lead and Mentored <b>smart fast learning engineers</b>, shaping architecture decisions, enforcing code quality standards, and accelerating team delivery velocity."),
    Spacer(1, 5),
]
story.append(KeepTogether(block1))

# Job 2 — SDConnect.VN
block2 = [
    Paragraph("Full Stack Developer — SDConnect.VN", job_title_style),
    Paragraph("Jan 2022 – Sep 2022 &nbsp;|&nbsp; Remote", job_meta_style),
    bullet("Accelerated frontend rendering performance by <b>60%</b>, reducing initial load time from 4s to under 1.5s via code splitting, lazy loading, and asset optimisation using <b>Next.js</b> and React Native."),
    bullet("Engineered <b>Redis-backed caching layers</b> and query optimisation strategies, reducing average database response time by <b>55%</b> across high-traffic endpoints."),
    bullet("Streamlined development lifecycle by standardising reusable component libraries and API contracts, reducing feature delivery time by <b>35%</b>."),
    bullet("Replaced REST polling with <b>WebSocket-driven communication</b>, enabling sub-100ms real-time data exchange between client and server and eliminating latency bottlenecks."),
    bullet("Architected <b>Redis-backed caching and query optimisation pipelines</b>, achieving 40% reduction in API response latency under production load on GCP with Docker-based workflows."),
    Spacer(1, 5),
]
story.append(KeepTogether(block2))

# Job 3 — Emolyze.Tech
block3 = [
    Paragraph("Junior Full Stack Engineer — Emolyze.Tech", job_title_style),
    Paragraph("Feb 2021 – Jan 2022 &nbsp;|&nbsp; On-site", job_meta_style),
    bullet("Constructed an <b>internal analytics dashboard from scratch</b>, delivering real-time visibility into client KPIs and eliminating manual reporting workflows."),
    bullet("Engineered a <b>REST API integration layer from zero</b> to unify third-party data sources into existing client systems, improving data consistency and access speed."),
    bullet("Developed responsive web applications using <b>Next.js</b> and TailwindCSS; built backend services with Express.js, Redis, and MySQL."),
    bullet("Deployed and managed applications on <b>AWS</b> using Docker, establishing foundational CI/CD practices for the engineering team."),
    Spacer(1, 5),
]
story.append(KeepTogether(block3))

# ── CORE TECHNICAL SKILLS ────────────────────────────────────────
story += section("Core Technical Skills")
story.append(skill_row("Languages:",      "TypeScript, JavaScript, Golang, Dart"))
story.append(skill_row("Frontend:",       "React.js, Next.js, React Native, Flutter, TailwindCSS, Shadcn UI"))
story.append(skill_row("Backend:",        "Node.js, Express.js, Fastify, REST API, GraphQL, WebSocket, WebRTC"))
story.append(skill_row("Databases:",      "PostgreSQL, MySQL, Redis, NoSQL, Query Optimisation"))
story.append(skill_row("Realtime:",       "WebSocket, WebRTC, Concurrent Connections, Background Services, Event-Driven Architecture"))
story.append(skill_row("Cloud & DevOps:", "AWS, GCP, Azure, Docker, Docker Compose, Kubernetes, GitHub Actions, CI/CD"))
story.append(skill_row("Infrastructure:", "NGINX, Linux, Container Orchestration, Distributed Systems"))
story.append(skill_row("API Design:",     "REST, GraphQL, API Contracts, Versioning, Rate Limiting"))
story.append(skill_row("Tools:",          "Git, Bun, Agile / Scrum, System Architecture"))

# ── KEY PROJECTS ─────────────────────────────────────────────────
story += section("Key Projects")

story.append(Paragraph("Privacy Chat App &nbsp;|&nbsp; <i>TypeScript, WebSocket, End-to-End Encryption, Flutter</i>", project_title))
story.append(Paragraph("github.com/fatwaanugerah21/privacy-chat-app", job_meta_style))
story.append(bullet("Architected a secure, privacy-first cross-platform chat application (Android &amp; iOS) with end-to-end encrypted messaging."))
story.append(bullet("Implemented real-time 1-to-1 messaging via <b>WebSocket</b> with <b>FCM push-notification fallback</b> for offline delivery reliability."))
story.append(Spacer(1, 4))

story.append(Paragraph("Automated Trading Bot Platform &nbsp;|&nbsp; <i>TypeScript, Node.js, Golang, WebSocket</i>", project_title))
story.append(bullet("Designed and maintained a fleet of <b>15+ trading bots</b> with real-time market data ingestion, order execution, and risk management logic."))
story.append(bullet("Built monitoring dashboards and alerting systems to ensure uptime and trading accuracy across all active bots."))
story.append(Spacer(1, 3))

# ── EDUCATION ────────────────────────────────────────────────────
story += section("Education")
story.append(Paragraph("Bachelor of Computer Science — Hasanuddin University", job_title_style))
story.append(Paragraph("2019 – 2023 &nbsp;|&nbsp; GPA: 3.65 / 4.00", job_meta_style))
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
