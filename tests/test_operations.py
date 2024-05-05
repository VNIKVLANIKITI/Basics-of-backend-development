import json
import pytest

from files_for_tests.right_answer import right1
from utils import get_date, mask_from_to, get_filtered_and_sorted, prepare_user_msg


def test_get_date():
    assert get_date("2019-07-03T18:35:29.512364") == "03.07.2019"
    assert get_date("2018-10-14T08:21:33.419441") == "14.10.2018"


def test_mask_from_to():
    """Тест проверяет как и правильные значения так и неправильные"""
    assert mask_from_to("Счет 35383033474447895560") == "Счет **5560"
    with pytest.raises(ValueError):
        mask_from_to("Счет 353")
    assert mask_from_to("Visa Platinum 1246377376343588") == "Visa Platinum 1246 37** **** 3588"
    with pytest.raises(ValueError):
        mask_from_to("Visa Platinum 1246")
    with pytest.raises(ValueError):
        mask_from_to("hsdgfjhb 848y9oy9349883494563464653456")


def test_get_filtered_and_sorted():
    with open("../files_for_tests/for_test_operations.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    assert get_filtered_and_sorted(data) == right1


def test_prepare_user_msg():
    assert prepare_user_msg(right1[0]) == "08.12.2019 Открытие вклада\nСчет **5907\n41096.24 USD"
