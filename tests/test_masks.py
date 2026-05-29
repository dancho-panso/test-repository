import pytest
from pyexpat.errors import messages

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number("4081700000000000") == "4081 70** **** 0000"

def test_get_mask_card_number_error():
    with pytest.raises(ValueError) as ex_info:
        get_mask_card_number("408208000")

def test_get_mask_account():
    assert get_mask_account("40817000000000001234") == "**1234"
    with pytest.raises(ValueError) as ex_info:
        get_mask_account("408")