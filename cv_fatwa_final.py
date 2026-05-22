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
story.append(Paragraph("Senior Software Engineer | Scalable Microservices & Real-Time Distributed Systems | TypeScript · Go · NestJS · React.js · Next.js · Flutter · WebSockets · Redis · Kafka | AI-Augmented Development | Open to Remote globally", title_style))
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
    "Someone who brings positive impact to the team through building, collaborating, leading, and architecting — a <b>Senior Software Engineer</b> with more than 5 years of experience designing and delivering end-to-end scalable software systems "
    "from scalable backend microservices and real-time architectures to production web and mobile applications "
    "for global remote teams. Core strength in <b>backend engineering</b>: experienced with special backend frameworks and tools such as "
    "<b>TypeScript, Go, NestJS, Node.js, Gin, Kafka, Redis, Sequelize, Prisma, Drizzle ORM, Gorm</b>. "
    "Complemented by hands-on delivery of full-stack products with frontend frameworks such as <b>React.js, Next.js, React Native, and Flutter</b>. ",
    body_style))
story += section("Experience")

block1 = [
    Paragraph("Senior Software Engineer — AVASO Technology Solutions (https://www.linkedin.com/company/avaso-technology-solutions/)", job_title_style),
    Paragraph("Sep 2022 – April 2026 &nbsp;|&nbsp; Remote", job_meta_style),
    bullet("Designed and developed scalable backend microservices in <b>TypeScript</b> <b>NestJS</b>, handling real-time data streams, built with full test coverage."),
    bullet("Designed, deployed, and maintained <b>5+ automated trading bots</b> with <b>Go</b> and <b>Gorm</b>, across 3 different trading exchanges, performing real-time market data ingestion and automated order execution, processing <b>$1M+ in monthly trading volume</b>."),
    bullet("Engineered WebSocket infrastructure for trading bot, enabling real-time trade signal delivery across each of the 5+ bots, with sub-second latency for market data ingestion"),
    bullet("Architected a concurrent backtesting engine leveraging <b>Node.js worker_threads</b> to parallelize strategy simulation across all available CPU cores, processing 4 years of OHLCV datasets smoothly."),
    bullet("Delivered end-to-end features across the stack — from API design and backend logic to web and mobile interfaces built with <b>React.js, Next.js, and Flutter</b>."),
    bullet("Designed and developed copy trading feature, powered by 2 streaming sources, RabbitMQ and Websocket, and handling race condition with idempotency."),
    bullet("Optimised <b>SQL database</b> schemas and query execution plans for performance and integrity across high-throughput production environments."),
    bullet("Containerised and deployed production workloads on <b>Azure</b> using Docker Compose and automated <b>CI/CD pipelines</b>, ensuring zero-downtime releases."),
    bullet("Led and mentored a team of 2 engineers, shaping architecture decisions, doing code reviews, enforcing code quality standards, and accelerating team delivery velocity."),
    Spacer(1, 5),
]
story.append(KeepTogether(block1))

# Job 2 — SDConnect.VN — reorder: backend/infra bullets first
block2 = [
    Paragraph("Full Stack Developer — SDConnect.VN (https://sdconnect.vn)", job_title_style),
    Paragraph("Jan 2022 – Sep 2022 &nbsp;|&nbsp; Remote", job_meta_style),
    bullet("Developed Full Stack product for SDConnect.VN, a B2B Ecommerce platform where users can buy and sell products to each other."),
    bullet("Built REST API with Typescript, Node.js, storing data with Sequelize ORM on MySQL dialect, and using Redis for caching"),
    bullet("Designed data structure and using AWS OpenSearch for fuzzy search improving user experience."),
    bullet("Designed and developed CI/CD pipeline with AWS Cloudformation, Dockerize the application and deploy to AWS ECS, and store attachments on AWS S3, using AWS SES for emailing service, and AWS Route 53 for domain routing."),
    bullet("Used lazy loading, and React Suspense as fallback for user waiting experience."),
    Spacer(1, 5),
]
story.append(KeepTogether(block2))

# Job 3 — Emolyze.Tech — backend bullets first
block3 = [
    Paragraph("Junior Full Stack Engineer — Emolyze.Tech (https://linkedin.com/company/emolyze-tech/)", job_title_style),
    Paragraph("Feb 2021 – Jan 2022 &nbsp;|&nbsp; Remote", job_meta_style),
    bullet("Engineered a full-stack product for Emolyze.Tech, with backend services with <b>Express.js, Redis, and MySQL</b>, and frontend using <b>React.js</b> and Styled components."),
    bullet("Built custom atomized modules for the product, with reusable components and services."),
    bullet("Learned and implemented CI/CD pipeline with AWS Cloudformation, Dockerize the application and deploy to AWS ECS, and store attachments on AWS S3, using AWS SES for emailing service, and AWS Route 53 for domain routing."),
    bullet("Used lazy loading, and React Suspense as fallback for user waiting experience."),
    Spacer(1, 5),
]
story.append(KeepTogether(block3))

# ── KEY PROJECTS ─────────────────────────────────────────────────
story += section("Key Projects")

story.append(Paragraph("Ai Recruiter &nbsp;|&nbsp; <i>TypeScript, NestJS, Microservices, WebSocket, Kafka, MongoDB, OpenAI, Puppeteer</i>", project_title))
story.append(bullet("Built an AI-powered recruiter, with microservices architecture, using Kafka and RabbitMQ for internal communication and notification, MongoDB for data storage, OpenAI for AI chat processing and response, and Puppeteer for web scraping."))
story.append(bullet("Built an internal dashboard for the HR Team to manage jobs and candidates, with React.js, Next.js, and TailwindCSS, and using WebSocket."))
story.append(Spacer(1, 4))

story.append(Paragraph("Automated Trading Bot Platform &nbsp;|&nbsp; <i>Go, TypeScript, Node.js, WebSocket, PostgreSQL</i>", project_title))
story.append(bullet("Designed and maintained a fleet of <b>5+ trading bots</b> with real-time market data ingestion, order execution, and risk management logic across multiple crypto exchanges."))
story.append(bullet("Built monitoring dashboards and alerting systems to ensure uptime and trading accuracy, processing <b>$1M+ in monthly trading volume</b>."))
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

# ── CORE TECHNICAL SKILLS ────────────────────────────────────────
story += section("Core Technical Skills")
story.append(skill_row("Languages:",        "Go, TypeScript, JavaScript, Java, Python, Dart"))
story.append(skill_row("Backend & APIs:",   "Gin, Gorm, Node.js, Express.js, Fastify, REST, WebSocket, RabbitMQ, Kafka, WebRTC, API Contracts"))
story.append(skill_row("Frontend & Mobile:","React.js, Next.js, React Native, Flutter, TailwindCSS"))
story.append(skill_row("Databases:",        "PostgreSQL, MySQL, Redis, NoSQL, Query Optimisation"))
story.append(skill_row("Architecture:",     "Distributed Systems, Event-Driven, Microservices, Real-time Systems, Concurrent Processing"))
story.append(skill_row("Cloud & DevOps:",   "AWS, GCP, Azure, Docker, Kubernetes, GitHub Actions, CI/CD, NGINX, Linux"))
story.append(skill_row("Tools & Process:",  "Git, Bun, Agile / Scrum, Figma"))

# ── EDUCATION ────────────────────────────────────────────────────
story += section("Education")
story.append(Paragraph("Bachelor of Computer Science — Hasanuddin University", job_title_style))
story.append(Paragraph("2019 – 2023 &nbsp;|&nbsp; GPA: 3.54 / 4.00", job_meta_style))
story.append(bullet("Relevant Coursework: Algorithms &amp; Data Structures, Distributed Systems, Software Engineering, Team Collaboration, and Team Leadership"))

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
