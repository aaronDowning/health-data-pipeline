from transform import clean_name, clean_records


def test_clean_name_trims_and_cases():
    assert clean_name("  john ") == "John"
    assert clean_name("SMITH") == "Smith"
    assert clean_name("mary jane") == "Mary Jane"


def test_clean_name_keeps_digits_intact():
    # The 0.3 finding: str.title() turned "Aar0n" into "Aar0N". capitalize() does not.
    assert clean_name("Aar0n") == "Aar0n"


def test_clean_name_handles_missing():
    assert clean_name(None) == ""
    assert clean_name("") == ""


def test_clean_records_dedupes_by_id():
    rows = [
        {"id": "p1", "first_name": "ann", "last_name": "lee"},
        {"id": "p1", "first_name": "ann", "last_name": "lee"},
        {"id": "p2", "first_name": "bo", "last_name": "fox"},
    ]
    result = clean_records(rows)
    assert len(result) == 2
    assert result[0]["first_name"] == "Ann"
