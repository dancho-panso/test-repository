from datetime import  datetime

from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(my_string: str) -> str:
    '''Функция обработки информацию о картах и счетах,
    и возвращает строку с замаскированным номером'''

    card_number = get_mask_card_number(my_string)

    card_account = get_mask_account(my_string)

    if "Счет" in my_string:
        return card_account
    else:
        return card_number

def get_date(date: str) -> str:
    '''Функция, которая форматирует дату в в формате ДД.ММ.ГГГГ'''

    new_date = datetime.fromisoformat(date).strftime('%d.%m.%Y')
    return new_date
