"""DocuParse package."""

__all__ = ["convert_pdf_to_markdown", "save_markdown"]

# Importing converter functions lazily to avoid unnecessary ImportError when
# optional dependencies like pdfminer.six are missing at package import time.
def __getattr__(name: str):
    if name in __all__:
        from . import converter
        return getattr(converter, name)
    raise AttributeError(f"module 'docuparse' has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(list(globals().keys()) + __all__)