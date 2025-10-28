# RPA_PDF

Projeto simples em FastAPI para processar currículos em PDF, extrair texto da primeira página, identificar nome, idade e hard skills e salvar resultados em um Excel.

## Funcionalidades

- Endpoint POST /process — aceita múltiplos arquivos (multipart/form-data) e retorna informações extraídas de cada PDF.
- Gera `curriculos_processados.xlsx` com Name, File, Age e Hard Skills.

## Requisitos

- Python 3.8+
- Dependências (exemplo):
  - fastapi
  - uvicorn
  - pdfplumber
  - openpyxl
  - python-multipart

Instalação rápida:

```bash
py -3 -m pip install fastapi uvicorn pdfplumber openpyxl python-multipart
# ou
py -3 -m pip install -r requirements.txt
```

## Como rodar (desenvolvimento)

No terminal (pasta do projeto `c:\Users\Bruno\RPA_PDF`):

```bash
py -3 -m uvicorn api:app --reload --host 127.0.0.1 --port 8000
```

Abra:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Enviando múltiplos arquivos

Swagger UI:

- Em `/docs` clique em _Try it out_, depois em _Choose Files_.
- Para selecionar vários arquivos use Ctrl+clique / Shift+clique ou arraste vários arquivos para o campo.

Postman:

- Crie uma requisição POST para `http://127.0.0.1:8000/process`.
- Em Body → form-data adicione várias chaves `files` (uma entrada por arquivo), cada uma com tipo `File`.
- Não defina o Content-Type manualmente; o Postman ajusta para `multipart/form-data`.

Exemplo curl:

```bash
curl -X POST "http://127.0.0.1:8000/process" \
  -F "files=@C:/caminho/para/arquivo1.pdf" \
  -F "files=@C:/caminho/para/arquivo2.pdf"
```

Licença: MIT (defina conforme necessidade).
