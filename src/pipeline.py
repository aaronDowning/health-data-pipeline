"""The end to end pipeline: extract, transform, load."""
import logging

from extract import read_json
from transform import clean_records
from deidentify import de_identify
from load import write_json

logger = logging.getLogger(__name__)


def run(source_path, target_path):
    """Read raw records, clean them, de identify PHI, and write the result.

    Extract, then Transform (clean and dedupe, then de identify), then Load.
    Logs the record count at each stage so an unattended run is observable.
    Returns the processed records.
    """
    raw = read_json(source_path)                 # Extract
    logger.info("extracted %d records from %s", len(raw), source_path)

    cleaned = clean_records(raw)                  # Transform: clean + dedupe
    logger.info("cleaned and deduped to %d records", len(cleaned))

    safe = [de_identify(record) for record in cleaned]  # Transform: de identify
    logger.info("de identified %d records", len(safe))

    write_json(safe, target_path)                # Load
    logger.info("loaded %d records to %s", len(safe), target_path)

    return safe
