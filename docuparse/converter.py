"""Utility functions for converting PDFs."""

try:  # pragma: no cover - optional dependency
    from pdfminer.high_level import extract_text as _extract_text
except ModuleNotFoundError:  # pragma: no cover - handled at runtime
    _extract_text = None


def convert_pdf_to_markdown(input_path: str, max_pages: int | None = None) -> str:
    """Extract text from a PDF and return it as Markdown string."""
    if _extract_text is None:
        raise ModuleNotFoundError(
            "pdfminer.six is required for PDF conversion. Install it with 'pip install pdfminer.six'"
        )
    text = _extract_text(input_path, maxpages=max_pages)
    return text


def save_markdown(text: str, output_path: str) -> None:
    """Write the Markdown text to the specified file."""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
