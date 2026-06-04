"""Load: write processed records to a target."""
import json
import os


def write_json(records, path):
    """Write records to a JSON file, replacing any existing contents.

    Replace (not append) is what makes this idempotent: running the pipeline
    twice produces the same output file, never duplicated rows. Creates the
    target directory if it does not exist.
    """
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w") as f:
        json.dump(records, f, indent=2)
    return path
