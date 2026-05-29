from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(my_string: str) -> str:
    """Функция обработки информацию о картах и счетах,
    и возвращает строку с замаскированным номером"""


    if "Счет" in my_string:
        numbers = my_string[-20:]
        card_account = get_mask_account(numbers)
        return f'Счет {card_account}'
    else:
        elements = my_string.split(" ")
        card_number = get_mask_card_number(elements[-1])
        if len(elements) == 3:
            name_card = " ".join(elements[0:2])
        elif len(elements) == 2:
            name_card = elements[0]
    return f'{name_card} {card_number}'


def get_date(date: str) -> str:
    """Функция, которая форматирует дату в формате ДД.ММ.ГГГГ"""

    new_date = datetime.fromisoformat(date).strftime("%d.%m.%Y")
    return new_date