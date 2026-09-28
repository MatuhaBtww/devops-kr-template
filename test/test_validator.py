# tests/test_validator.py
from validator import validate_email, validate_phone


def test_validate_email():
    assert validate_email("test@example.com") == True
    assert validate_email("invalid") == False


def test_validate_phone():
    assert validate_phone("+79991234567") is True
    assert validate_phone("89991234567") is False
    assert validate_phone("+7999123") is False


def test_validate_phone_formatting():
    assert validate_phone("7 999 123-45-67") is True
    assert validate_phone("+7 999 123-45-67") is True
    assert validate_phone("+799912345678") is False
    assert validate_phone("phone") is False
    assert validate_phone("") is False
