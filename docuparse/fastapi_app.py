from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import PlainTextResponse
import tempfile

from .converter import convert_pdf_to_markdown

app = FastAPI(title="DocuParse API")


@app.post("/convert", response_class=PlainTextResponse)
async def convert_endpoint(
    file: UploadFile = File(...), max_pages: int | None = Form(None)
) -> str:
    """Convert an uploaded PDF and return Markdown."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        contents = await file.read()
        tmp.write(contents)
        tmp.flush()
        text = convert_pdf_to_markdown(tmp.name, max_pages=max_pages)
    return text
