"""De identify: mask or generalize PHI before the data leaves the pipeline."""


def mask_ssn(ssn):
    """Mask all but the last 4 digits of an SSN. "111-22-3333" becomes "***-**-3333"."""
    if not ssn:
        return ""
    last4 = ssn[-4:]
    return f"***-**-{last4}"


def to_birth_year(birth_date):
    """Generalize a full birth date down to the year. "1980-04-12" becomes "1980"."""
    if not birth_date:
        return ""
    return birth_date[:4]


def de_identify(record):
    """Return a copy with direct identifiers masked or generalized.

    Masks the SSN and generalizes the birth date to a year: two common HIPAA
    Safe Harbor techniques (masking and date generalization). Operates on a copy,
    so the raw record is never mutated.
    """
    safe = dict(record)
    safe["ssn"] = mask_ssn(record.get("ssn"))
    safe["birth_year"] = to_birth_year(record.get("birth_date"))
    safe.pop("birth_date", None)
    return safe
