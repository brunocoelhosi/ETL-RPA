import os
from openpyxl import Workbook

directory = 'pdf_files'
files = os.listdir(directory)
files_qtd = len(files)

if files_qtd == 0:
    raise Exception("No PDF files found in the specified directory.")

wb = Workbook() #Inicializa a planilha
ws = wb.active # Seleciona a planilha ativa
ws.title = "PDF Imports" # Define o título da planilha
