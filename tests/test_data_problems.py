"""
Tests that cover common real-world data problems.
Each test is tied to a specific record in sample_data/patients.json.
"""
import json
from transform import clean_name, clean_records
from deidentify import mask_ssn, to_birth_year, de_identify
from pipeline import run


SOURCE = "sample_data/patients.json"


# ── clean_name edge cases ─────────────────────────────────────────────────────

def test_whitespace_only_name_becomes_empty():
    """A name that is only spaces should clean to an empty string, not a space."""
    assert clean_name("   ") == ""


def test_digit_in_name_preserved():
    """str.capitalize() must not corrupt a digit-boundary name the way str.title() does."""
    assert clean_name("Aar0n") == "Aar0n"
    assert clean_name("  Aar0n") == "Aar0n"


def test_null_name_becomes_empty():
    assert clean_name(None) == ""


def test_already_clean_name_unchanged():
    assert clean_name("John Smith") == "John Smith"


def test_apostrophe_name_does_not_crash():
    """O'Brien is a known capitalization edge case; at minimum it must not crash."""
    result = clean_name("O'Brien")
    assert isinstance(result, str)
    assert len(result) > 0


def test_hyphenated_name_does_not_crash():
    result = clean_name("Johnson-Williams")
    assert isinstance(result, str)
    assert len(result) > 0


# ── duplicate deduplication ───────────────────────────────────────────────────

def test_duplicate_id_drops_second_occurrence():
    """When two records share an id, first occurrence wins and second is dropped."""
    rows = [
        {"id": "p001", "first_name": "  john ", "last_name": "SMITH", "birth_date": "1980-04-12", "ssn": "111-22-3333"},
        {"id": "p001", "first_name": "Jonathan", "last_name": "Smith", "birth_date": "1980-04-12", "ssn": "111-22-3333"},
    ]
    result = clean_records(rows)
    assert len(result) == 1
    assert result[0]["first_name"] == "John"


# ── null PHI fields ───────────────────────────────────────────────────────────

def test_null_ssn_masks_to_empty():
    assert mask_ssn(None) == ""


def test_null_birth_date_generalizes_to_empty():
    assert to_birth_year(None) == ""


def test_de_identify_with_all_null_phi():
    rec = {"id": "p006", "first_name": "Marcus", "last_name": "Chen", "birth_date": None, "ssn": None}
    safe = de_identify(rec)
    assert safe["ssn"] == ""
    assert safe["birth_year"] == ""
    assert "birth_date" not in safe


# ── extra unexpected fields ───────────────────────────────────────────────────

def test_extra_fields_pass_through():
    """A record with an unexpected field (like insurance_id) must not crash the pipeline."""
    rec = {"id": "p010", "first_name": "Robert", "last_name": "Taylor",
           "birth_date": "1955-08-07", "ssn": "999-00-1111", "insurance_id": "BCB-12345"}
    from transform import clean_record
    result = clean_record(rec)
    assert result["first_name"] == "Robert"
    assert "insurance_id" in result


# ── full pipeline on the complete sample dataset ──────────────────────────────

def test_full_pipeline_on_sample_data(tmp_path):
    out = tmp_path / "out.json"
    result = run(SOURCE, str(out))

    ids = [r["id"] for r in result]

    # duplicate p001 was deduped: only one p001
    assert ids.count("p001") == 1

    # all 10 unique records survive (11 raw minus 1 duplicate)
    assert len(result) == 10

    # no raw SSNs survived de-identification
    for rec in result:
        ssn = rec.get("ssn", "")
        assert not any(c.isdigit() for c in ssn[:3]), f"raw SSN digits found in {rec['id']}"

    # no raw birth_date fields survived
    for rec in result:
        assert "birth_date" not in rec

    # output file matches the returned data
    written = json.loads(out.read_text())
    assert written == result
