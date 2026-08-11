def test_expected_training_names():
    assert "companyx-training-finance".startswith("companyx")
    assert "companyxtraining".startswith("companyx")
    assert "companyx-training-exports".startswith("companyx")
