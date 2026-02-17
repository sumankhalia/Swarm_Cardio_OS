from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from datetime import datetime


def generate_pdf_report(report):

    filename = f"Swarm_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "Title",
        fontSize=18,
        spaceAfter=20,
        textColor=colors.black
    )

    heading_style = ParagraphStyle(
        "Heading",
        fontSize=12,
        spaceAfter=6,
        textColor=colors.black
    )

    body_style = ParagraphStyle(
        "Body",
        fontSize=10,
        spaceAfter=4,
        textColor=colors.black
    )

    story = []

    # --------------------------------------------------
    # TITLE
    # --------------------------------------------------

    story.append(Paragraph("CardioSphere Intelligence Report", title_style))
    story.append(Spacer(1, 12))

    # --------------------------------------------------
    # CORE DECISION DATA (DEFENSIVE)
    # --------------------------------------------------

    decision = report.get("Decision", "Unavailable")
    composite_score = report.get("CompositeScore", 0)
    risk_probability = report.get("RiskProbability", 0)

    story.append(Paragraph("Decision Overview", heading_style))
    story.append(Paragraph(f"Decision: {decision}", body_style))
    story.append(Paragraph(f"Composite Score: {round(composite_score, 2)}", body_style))
    story.append(Paragraph(f"Risk Probability: {round(risk_probability, 3)}", body_style))

    story.append(Spacer(1, 12))

    # --------------------------------------------------
    # CONSENSUS (FULLY DEFENSIVE)
    # --------------------------------------------------

    consensus = report.get("Consensus", {})

    story.append(Paragraph("Consensus Analysis", heading_style))
    story.append(Paragraph(
        consensus.get("summary", "Consensus unavailable"),
        body_style
    ))

    story.append(Paragraph(
        f"Confidence Level: {round(consensus.get('confidence', 0), 2)}",
        body_style
    ))

    story.append(Spacer(1, 12))

    # --------------------------------------------------
    # AGENT INTERPRETATIONS (DEFENSIVE LOOP)
    # --------------------------------------------------

    agents = report.get("Agents", {})

    story.append(Paragraph("Agent Interpretations", heading_style))
    story.append(Spacer(1, 6))

    for agent_name, agent_data in agents.items():

        signal_assessment = agent_data.get("signal_assessment", "Unavailable")
        risk_interpretation = agent_data.get("risk_interpretation", "Unavailable")
        confidence = agent_data.get("confidence", 0)

        story.append(Paragraph(agent_name, heading_style))
        story.append(Paragraph(signal_assessment, body_style))
        story.append(Paragraph(risk_interpretation, body_style))
        story.append(Paragraph(f"Confidence: {confidence}", body_style))

        story.append(Spacer(1, 8))

    # --------------------------------------------------
    # META ANALYSIS (DEFENSIVE)
    # --------------------------------------------------

    meta = report.get("MetaAnalysis", {})

    story.append(Spacer(1, 12))
    story.append(Paragraph("Meta Analysis", heading_style))
    story.append(Paragraph(
        f"Cognitive Dispersion: {round(meta.get('dispersion', 0), 2)}",
        body_style
    ))

    # --------------------------------------------------
    # BUILD PDF
    # --------------------------------------------------

    doc.build(story)

    print(f"\nPDF Report Generated → {filename}")
