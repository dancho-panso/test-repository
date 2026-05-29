from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(list_dict, dict_executed, dict_canceled):
    assert filter_by_state(list_dict) == dict_executed
    assert filter_by_state(list_dict, "CANCELED") == dict_canceled

def test_sort_by_date(list_dict, sort_1, sort_reverse):
    assert sort_by_date(list_dict) == sort_1
    assert sort_by_date(list_dict, parameter=False) == sort_reverse