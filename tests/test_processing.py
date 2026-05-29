from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(list_dict: list[dict], dict_executed: list[dict], dict_canceled: list[dict]) -> None:
    """Тестирование функции filter_by_state"""
    assert filter_by_state(list_dict) == dict_executed
    assert filter_by_state(list_dict, "CANCELED") == dict_canceled


def test_sort_by_date(list_dict: list[dict], sort_1: list[dict], sort_reverse: list[dict]) -> None:
    """Тестирование функции sort_by_date"""
    assert sort_by_date(list_dict) == sort_1
    assert sort_by_date(list_dict, parameter=False) == sort_reverse
