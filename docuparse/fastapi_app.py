from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import PlainTextResponse
import os
import tempfile

from .converter import convert_pdf_to_markdown

app = FastAPI(title="DocuParse API")


@app.post("/convert", response_class=PlainTextResponse)
async def convert_endpoint(
    file: UploadFile = File(...), max_pages: int | None = Form(None)
) -> str:
    """Convert an uploaded PDF and return Markdown."""
    tmp_name: str | None = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp_name = tmp.name
            contents = await file.read()
            tmp.write(contents)
            tmp.flush()
        text = convert_pdf_to_markdown(tmp_name, max_pages=max_pages)
        return text
    except ModuleNotFoundError as e:
        # Dependency for PDF conversion is missing
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:  # pragma: no cover - runtime errors
        raise HTTPException(status_code=500, detail=f"Failed to convert PDF: {e}")
    finally:
        if tmp_name and os.path.exists(tmp_name):
            os.unlink(tmp_name)
