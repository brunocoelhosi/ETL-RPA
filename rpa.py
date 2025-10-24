import os
import pdfplumber
from openpyxl import Workbook
import re


# Lista de hard skills a procurar
HARD_SKILLS = [
    "Python", "Java", "JavaScript", "C#", "SQL", "Excel", "Power BI",
    "Django", "Flask", "React", "Node.js", "Git", "HTML", "CSS"
]

directory = 'pdf_files'
files = os.listdir(directory)
files_qtd = len(files)

if files_qtd == 0:
    raise Exception("No PDF files found in the specified directory.")

wb = Workbook() #Inicializa a planilha
ws = wb.active # Seleciona a planilha ativa
ws.title = "PDF Imports" # Define o título da planilha

# Adiciona os cabeçalhos na primeira linha
ws['A1'] = "Index"
ws['B1'] = "Name"
ws['C1'] = "File Name"
ws['D1'] = "Age"
ws['E1'] = "Degree"
ws['F1'] = "Hard Skills"

last_empty_row = 1

while ws['A' + str(last_empty_row)].value is not None:
    last_empty_row += 1

def extract_text(file):
    # Abre o PDF e retorna o texto da primeira página.
    path = os.path.join(directory, file)
    with pdfplumber.open(path) as pdf:
        first_page = pdf.pages[0]
        pdf_text = first_page.extract_text()
        # Garantir que sempre retornamos uma string (evita NoneType em chamadas posteriores)
        if pdf_text is None:
            pdf_text = ""

        return pdf_text

def extract_info(text):
    # Proteção caso seja passado None
    if text is None:
        text = ""

    
    name_match = re.search(r"^(.*)", text)
    name = name_match.group(1).strip() if name_match else "N/A"

    # Idade: procura por padrão "XX anos"
    idade_match = re.search(r"(\d{2})\s*anos", text)
    idade = idade_match.group(1) if idade_match else "N/A"

    # Hard skills: verifica quais da lista aparecem no texto
    skills = [skill for skill in HARD_SKILLS if re.search(fr"\b{skill}\b", text, re.IGNORECASE)]

    return {
        "Name": name,
        "Idade": idade,
        "Hard Skills": ", ".join(skills)
    }



def process_curriculum():
    for file in files:
        text = extract_text(file)

        info = extract_info(text)
        print(info)


process_curriculum()