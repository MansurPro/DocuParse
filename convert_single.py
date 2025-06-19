import argparse
from pdfminer.high_level import extract_text


def convert_pdf_to_markdown(input_path: str, output_path: str, max_pages: int | None = None) -> None:
    """Extract text from a PDF and write it to a Markdown file.

    Parameters
    ----------
    input_path : str
        Path to the input PDF file.
    output_path : str
        Path to the output Markdown file.
    max_pages : int | None, optional
        Maximum number of pages to process from the PDF. ``None`` processes all pages.
    """
    text = extract_text(input_path, maxpages=max_pages)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a PDF to Markdown text.")
    parser.add_argument("input_pdf", help="Path to the PDF file")
    parser.add_argument("output_md", help="Path for the output Markdown file")
    parser.add_argument(
        "--parallel_factor",
        type=int,
        default=1,
        help="Reserved for future parallel processing; unused in this script",
    )
    parser.add_argument(
        "--max_pages", type=int, default=None, help="Maximum number of pages to process"
    )
    args = parser.parse_args()

    convert_pdf_to_markdown(args.input_pdf, args.output_md, args.max_pages)
