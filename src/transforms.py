"""Tiny data transforms. The first real code in the pipeline."""


def clean_name(name: str) -> str:
    """Trim surrounding whitespace and title-case a name.

    Example: "  john SMITH " becomes "John Smith".
    """
    return name.strip().title()
