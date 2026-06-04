from deidentify import mask_ssn, to_birth_year, de_identify


def test_mask_ssn_keeps_last_four():
    assert mask_ssn("111-22-3333") == "***-**-3333"


def test_mask_ssn_handles_missing():
    assert mask_ssn(None) == ""


def test_to_birth_year_generalizes():
    assert to_birth_year("1980-04-12") == "1980"


def test_de_identify_masks_and_generalizes():
    rec = {"id": "p1", "first_name": "Ann", "ssn": "111-22-3333", "birth_date": "1980-04-12"}
    safe = de_identify(rec)
    assert safe["ssn"] == "***-**-3333"
    assert safe["birth_year"] == "1980"
    assert "birth_date" not in safe
    # the raw record is untouched
    assert rec["ssn"] == "111-22-3333"
