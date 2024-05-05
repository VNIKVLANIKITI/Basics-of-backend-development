from typing import Any


def get_filtered_and_sorted(data):
    """Выводит последние 5 операций 'EXECUTED' разделены пустой строкой """

    items = [payment for payment in data if payment.get("state") == "EXECUTED"]
    items.sort(key=lambda x: x.get("date"), reverse=True)
    return items


def prepare_user_msg(item: dict[str, Any]):
    """Получает операцию и Строктурирует """

    date = get_date(item.get("date"))
    desc = item.get("description")
    from_ = mask_from_to(item.get("from"))
    to_ = mask_from_to(item.get("to"))
    amount = item.get("operationAmount").get("amount")
    currency = item.get("operationAmount").get("currency").get("name")

    if from_:
        from_ += " -> "
    else:
        from_ = ""

    return f"{date} {desc}\n{from_}{to_}\n{amount} {currency}"


def get_date(date):
    """Получает дату и приводит к виду как в ТЗ '14.10.2018' """

    date_raw = date[0:10].split(sep="-")  # ["2019", "04", "02"]
    return f"{date_raw[2]}.{date_raw[1]}.{date_raw[0]}"


def mask_from_to(number):
    """Получает данные карты или счёта и решат что шифровать а что нет"""

    if number is None:
        return ""

    msg = number.split()

    if msg[0] == "Счет":
        number_hidden = mask_account(msg[-1])
    else:
        number_hidden = mask_card_number(msg[-1])

    return " ".join(msg[:-1]) + " " + number_hidden


def mask_account(number):
    """Получает номер Счёта оставляет
    только последние 4 цифры номера счета остольные скрывает
    Если неверная длина номера счёта вернёт ошибку."""

    if number.isdigit() and len(number) > 4:
        return f"**{number[-4:]}"
    else:
        raise ValueError("Номер счёта не валидный")


def mask_card_number(number: str):
    """Получает номер Карты оставляет
        XXXX XX** **** XXXX (видны первые 6 цифр и последние 4,
        разбито по блокам по 4 цифры, разделенных пробелом)
        Если неверная длина номера карты вернёт ошибку."""

    if number.isdigit() and len(number) == 16:
        return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
    else:
        raise ValueError("Номер карты не валидный")
