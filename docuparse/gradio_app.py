from typing import Any

import requests
import gradio as gr

API_URL = "http://localhost:8000/convert"


def convert_pdf(file: Any, max_pages: int | None) -> str:
    """Send PDF to the API and return Markdown text."""
    if max_pages is not None:
        max_pages = int(max_pages)
    with open(file.name, "rb") as f:
        files = {"file": (file.name, f, "application/pdf")}
        data = {"max_pages": max_pages} if max_pages is not None else {}
        try:
            resp = requests.post(API_URL, files=files, data=data)
            resp.raise_for_status()
        except requests.RequestException as e:  # pragma: no cover - network errors
            if e.response is not None:
                return f"API error {e.response.status_code}: {e.response.text}"
            return f"Request failed: {e}"
    return resp.text

iface = gr.Interface(
    fn=convert_pdf,
    inputs=[gr.File(label="PDF"), gr.Number(label="Max pages", precision=0)],
    outputs="text",
    title="DocuParse UI",
)

if __name__ == "__main__":
    iface.launch()
