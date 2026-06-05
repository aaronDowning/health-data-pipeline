"""Entry point: run the pipeline on the sample dataset and print a summary."""
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from pipeline import run

SOURCE = "sample_data/patients.json"
TARGET = "output/patients.json"


def main():
    print("Running health-data-pipeline...\n")
    result = run(SOURCE, TARGET)
    print(f"Output: {len(result)} records written to {TARGET}\n")
    print(json.dumps(result, indent=2))
    print(f"\nDone. Raw input: {SOURCE}  Clean output: {TARGET}")


if __name__ == "__main__":
    main()
