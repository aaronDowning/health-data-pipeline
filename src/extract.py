"""Extract: read raw source data into memory."""
import json


def read_json(path):
    """Read a JSON file and return the parsed data (a list of patient dicts)."""
    with open(path) as f:
        return json.load(f)
