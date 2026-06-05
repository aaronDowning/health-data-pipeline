"""Edge case hardening: empty input, missing fields, missing PHI."""
from transform import clean_records, clean_record
from deidentify import de_identify


def test_clean_records_handles_empty():
    assert clean_records([]) == []


def test_clean_record_handles_missing_names():
    out = clean_record({"id": "x"})
    assert out["first_name"] == ""
    assert out["last_name"] == ""


def test_de_identify_handles_missing_phi():
    out = de_identify({"id": "x"})
    assert out["ssn"] == ""
    assert out["birth_year"] == ""
    assert "birth_date" not in out
