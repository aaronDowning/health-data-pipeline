"""The end to end pipeline: extract, transform, load."""
from extract import read_json
from transform import clean_records
from deidentify import de_identify
from load import write_json


def run(source_path, target_path):
    """Read raw records, clean them, de identify PHI, and write the result.

    Extract, then Transform (clean and dedupe, then de identify), then Load.
    Returns the processed records.
    """
    raw = read_json(source_path)                 # Extract
    cleaned = clean_records(raw)                  # Transform: clean + dedupe
    safe = [de_identify(record) for record in cleaned]  # Transform: de identify
    write_json(safe, target_path)                # Load
    return safe
