import os
from dotenv import load_dotenv
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import Image, Table, TableStyle
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER


load_dotenv()

def add_detailed_section(title, content):
    if content.strip():
        elements.append(Paragraph(title, styles["SectionHeading"]))
        entries = [item.strip() for item in content.split("||") if item.strip()]
        for entry in entries:
            parts = entry.split("::")
            main_title = parts[0].strip()
            desc = parts[1].strip() if len(parts) > 1 else ""

            elements.append(Paragraph(f"• {main_title}", styles["CustomBullet"]))
            if desc:
                elements.append(Paragraph(desc, styles["BodyText"]))
            elements.append(Spacer(1, 4))
        elements.append(HRFlowable(width="100%", color=colors.grey, thickness=0.7))
        elements.append(Spacer(1, 10))


# Load input values
name = os.getenv("INPUT_NAME", "Your Name")
email = os.getenv("INPUT_EMAIL", "you@example.com")
phone = os.getenv("INPUT_PHONE", "+00-0000000000")
summary = os.getenv("INPUT_SUMMARY", "")
education = os.getenv("INPUT_EDUCATION", "")
experience = os.getenv("INPUT_EXPERIENCE", "")
projects = os.getenv("INPUT_PROJECTS", "")
skills = os.getenv("INPUT_SKILLS", "")
profile_image = os.getenv("INPUT_PROFILE_IMAGE", "")
github_url = os.getenv("INPUT_GITHUB", "")
linkedin_url = os.getenv("INPUT_LINKEDIN", "")

filename =  "cv.pdf"


# Setup document
doc = SimpleDocTemplate(
    filename,
    pagesize=A4,
    rightMargin=25 * mm,
    leftMargin=25 * mm,
    topMargin=25 * mm,
    bottomMargin=20 * mm,
)

# Styles
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='SectionHeading', fontSize=13, leading=16, spaceAfter=6, textColor=colors.HexColor("#333333"), fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name='CustomBullet', fontSize=10.5, leading=14, leftIndent=12, bulletIndent=0, bulletFontSize=8, bulletOffsetY=1))

styles.add(ParagraphStyle(name='CustomBodyText', fontSize=11, leading=14, spaceAfter=6))

elements = []

# Header: Name, Email, Phone


# Custom header styles
styles.add(ParagraphStyle(name="HeaderName", fontSize=16, leading=18, spaceAfter=4, alignment=TA_LEFT, fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name="HeaderContact", fontSize=10.5, leading=12, alignment=TA_CENTER))
styles.add(ParagraphStyle(name="HeaderLink", fontSize=10.5, alignment=TA_RIGHT, textColor=colors.black))

# Load profile image if provided
if profile_image and os.path.exists(profile_image):
    profile_img = Image(profile_image, width=50, height=50)
else:
    profile_img = Spacer(1, 50)

# Name and contact blocks
name_paragraph = Paragraph(f"<b>{name}</b>", styles["HeaderName"])

# GitHub + LinkedIn with icons (optional update later)
social_links = []
if github_url:
    social_links.append(f"🐙 GitHub")
if linkedin_url:
    social_links.append(f"🔗 LinkedIn")
right_links = Paragraph(" &nbsp; ".join(social_links), styles["HeaderLink"])
contact_line = Paragraph(f"{email}", styles["HeaderContact"])

# Combine image + name/social into a nested table
text_table = Table(
    [[name_paragraph, right_links],
     [contact_line, ""]],
    colWidths=[200, 200]
)
text_table.setStyle(TableStyle([
    ('SPAN', (0, 1), (1, 1)),
    ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
    ('ALIGN', (0, 1), (1, 1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
]))

# Final header with image and text block
header_table = Table(
    [[profile_img, text_table]],
    colWidths=[60, 440]
)
header_table.setStyle(TableStyle([
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('LEFTPADDING', (0, 0), (-1, -1), 0),
    ('RIGHTPADDING', (0, 0), (-1, -1), 0),
]))

elements.append(header_table)
elements.append(Spacer(1, 10))
elements.append(HRFlowable(width="100%", color=colors.grey, thickness=1))
elements.append(Spacer(1, 10))




# Summary
if summary.strip():
    elements.append(Paragraph("Summary", styles["SectionHeading"]))
    elements.append(Paragraph(summary, styles["BodyText"]))
    elements.append(Spacer(1, 6))
    elements.append(HRFlowable(width="100%", color=colors.grey, thickness=0.7))
    elements.append(Spacer(1, 10))


add_detailed_section("Education", education)
add_detailed_section("Experience", experience)
add_detailed_section("Projects", projects)

# Skills section – flat list style
if skills.strip():
    elements.append(Paragraph("Skills", styles["SectionHeading"]))
    skill_items = [skill.strip() for skill in skills.split(",") if skill.strip()]
    for skill in skill_items:
        elements.append(Paragraph(f"• {skill}", styles["CustomBullet"]))
    elements.append(Spacer(1, 6))
    elements.append(HRFlowable(width="100%", color=colors.grey, thickness=0.7))
    elements.append(Spacer(1, 10))



# Footer
elements.append(Spacer(1, 10))
elements.append(Paragraph(f"<font size=8 color='grey'>Generated via Python on GitHub Actions</font>", styles["BodyText"]))

# Build PDF
doc.build(elements)
print(f"✅ Aesthetic PDF CV generated: {filename}")
