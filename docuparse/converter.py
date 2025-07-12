from pdfminer.high_level import extract_text


def convert_pdf_to_markdown(input_path: str, max_pages: int | None = None) -> str:
    """Extract text from a PDF and return it as Markdown string."""
    text = extract_text(input_path, maxpages=max_pages)
    return text


def save_markdown(text: str, output_path: str) -> None:
    """Write the Markdown text to the specified file."""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
