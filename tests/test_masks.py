import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number() -> None:
    """Тестирование функции mask_card_number при корректных данных"""
    assert get_mask_card_number("4081700000000000") == "4081 70** **** 0000"


def test_get_mask_card_number_error() -> None:
    """Тестирование функции mask_card_number при неверных данных"""
    with pytest.raises(ValueError):
        get_mask_card_number("408208000")


def test_get_mask_account() -> None:
    """Тестирование функции get_mask_account"""
    assert get_mask_account("40817000000000001234") == "**1234"
    with pytest.raises(ValueError):
        get_mask_account("408")
