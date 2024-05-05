import json


def main():
    with open("operations.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    items = [payment for payment in data if payment.get("state") == "EXECUTED"]
    items.sort(key=lambda x: x.get("date"), reverse=True)

    print(items)


if __name__ == "__main__":
    main()
