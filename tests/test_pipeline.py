import json
from pipeline import run

SOURCE = "sample_data/patients.json"


def test_pipeline_end_to_end(tmp_path):
    out = tmp_path / "patients.json"
    result = run(SOURCE, str(out))

    # cleaned: first record name trimmed and cased
    assert result[0]["first_name"] == "John"
    # de identified: ssn masked, exact birth date removed
    assert result[0]["ssn"] == "***-**-3333"
    assert "birth_date" not in result[0]

    # the output actually landed in the target
    written = json.loads(out.read_text())
    assert written == result


def test_pipeline_is_idempotent(tmp_path):
    out = tmp_path / "patients.json"
    first = run(SOURCE, str(out))
    second = run(SOURCE, str(out))

    assert first == second
    # running twice did not duplicate rows in the file
    written = json.loads(out.read_text())
    assert len(written) == len(first)
