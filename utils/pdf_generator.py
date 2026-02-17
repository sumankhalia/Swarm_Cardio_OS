from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


class PDFGenerator:

    @staticmethod
    def generate(report_data, filename="Swarm_Report.pdf"):

        doc = SimpleDocTemplate(filename, pagesize=A4)
        styles = getSampleStyleSheet()

        title_style = ParagraphStyle('Title', fontSize=18, spaceAfter=20)
        heading = ParagraphStyle('Heading', fontSize=12, spaceAfter=6)
        body = ParagraphStyle('Body', fontSize=10, spaceAfter=12)

        elements = []

        elements.append(Paragraph("CardioSphere Intelligence Report", title_style))

        for key, value in report_data.items():
            elements.append(Paragraph(f"<b>{key}</b>", heading))
            elements.append(Paragraph(str(value), body))

        doc.build(elements)

        print(f"\n📄 PDF Report Generated → {filename}")
