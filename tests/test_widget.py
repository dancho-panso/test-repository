import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "num, result",
    [("dfdk 4081700000000000", "dfdk 4081 70** **** 0000"), ("Счет 40817000000000001234", "Счет **1234")],
)
def test_mask_account_card(num: str, result: str) -> None:
    """Тестирование функции mask_account_card"""
    assert mask_account_card(num) == result


def test_get_date() -> None:
    """Тестирование функции get_date"""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
