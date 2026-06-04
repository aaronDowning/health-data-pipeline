"""Transform: clean raw records into a consistent, validated shape."""


def clean_name(name):
    """Trim and capitalize each word, without the digit boundary bug of str.title().

    Uses str.capitalize() per word, which capitalizes the first character and
    lowercases the rest, and does NOT treat digits as word boundaries. So
    "Aar0n" stays "Aar0n" rather than becoming "Aar0N". Returns "" for a missing
    or empty name.

    Known limitation: apostrophe and hyphen names (O'Brien, Mary-Jane) are not
    fully cased; that needs a locale aware pass later.
    """
    if not name:
        return ""
    return " ".join(word.capitalize() for word in name.split())


def clean_record(record):
    """Return a cleaned copy of one patient record."""
    cleaned = dict(record)
    cleaned["first_name"] = clean_name(record.get("first_name"))
    cleaned["last_name"] = clean_name(record.get("last_name"))
    return cleaned


def clean_records(records):
    """Clean a list of records and drop duplicates by id (first occurrence wins)."""
    seen = set()
    out = []
    for record in records:
        cleaned = clean_record(record)
        key = cleaned.get("id")
        if key in seen:
            continue
        seen.add(key)
        out.append(cleaned)
    return out
