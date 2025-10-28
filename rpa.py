import os
import pdfplumber
from openpyxl import Workbook
import re

HARD_SKILLS = [
    "Python", "Java", "JavaScript", "C#", "SQL", "Excel", "Power BI",
    "Django", "Flask", "React", "Node.js", "Git", "HTML", "CSS"
]

def extract_text(file):
    file_object = file.file

    with pdfplumber.open(file_object) as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()
        return text or ""

def extract_info(text, filename):
    linhas = [l.strip() for l in text.split("\n") if l.strip()]
    name = linhas[0] if linhas else "Não identificado"

    idade_regex = re.search(r"(\d{2})\s*anos", text)
    idade = idade_regex.group(1) if idade_regex else "N/A"

    skills = [skill for skill in HARD_SKILLS if re.search(fr"\b{skill}\b", text, re.IGNORECASE)]

    return {
        "file": filename,
        "name": name,
        "age": idade,
        "skills": skills
    }

def process_curriculum(file):
    filename = getattr(file, "filename", os.path.basename(file) if isinstance(file, str) else "unknown")
    text = extract_text(file)
    info = extract_info(text, filename)
    return info
