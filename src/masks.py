def get_mask_card_number(card_number: str) -> str:
    '''Функция маскировки карты'''
    # Проверяем длину номера карты
    if len(card_number) < 16:
        raise ValueError("Номер карты должен содержать 16 цифр.")
    # Форматируем номер карты
    masked_card = f"{card_number[:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"
    return masked_card


def get_mask_account(account_number: str) -> str:
    '''Функция маскировки счета'''
    # Проверяем длину номера счета
    if len(account_number) < 4:
        raise ValueError("Номер счета должен содержать как минимум 4 цифры.")
    # Форматируем номер счета
    masked_account = f"Счет **{account_number[-4:]}"
    return masked_account

