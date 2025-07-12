import requests
import gradio as gr

API_URL = "http://localhost:8000/convert"

def convert_pdf(file: gr.files.FileData, max_pages: int | None) -> str:
    """Send PDF to the API and return Markdown text."""
    with open(file.name, "rb") as f:
        files = {"file": (file.name, f, "application/pdf")}
        data = {"max_pages": max_pages} if max_pages is not None else {}
        resp = requests.post(API_URL, files=files, data=data)
        resp.raise_for_status()
    return resp.text

iface = gr.Interface(
    fn=convert_pdf,
    inputs=[gr.File(label="PDF"), gr.Number(label="Max pages", precision=0)],
    outputs="text",
    title="DocuParse UI",
)

if __name__ == "__main__":
    iface.launch()
