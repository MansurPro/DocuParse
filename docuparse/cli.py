import click
from .converter import convert_pdf_to_markdown, save_markdown


@click.group()
def cli() -> None:
    """DocuParse command line interface."""
    pass


@cli.command()
@click.argument("input_pdf")
@click.argument("output_md")
@click.option("--max-pages", type=int, default=None, help="Maximum pages to process")
def convert(input_pdf: str, output_md: str, max_pages: int | None) -> None:
    """Convert a PDF file to Markdown."""
    text = convert_pdf_to_markdown(input_pdf, max_pages=max_pages)
    save_markdown(text, output_md)
    click.echo(f"Markdown saved to {output_md}")


if __name__ == "__main__":
    cli()
