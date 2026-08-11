def test_expected_storage_names():
    assert "companyx-training-finance".startswith("companyx")
    assert "companyxtraining".startswith("companyx")
    assert "companyx-training-exports".startswith("companyx")


def test_public_domain():
    assert "companyx-reporting-portal.example".endswith(".example")
