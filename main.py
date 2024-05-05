import json
from utils import get_filtered_and_sorted, prepare_user_msg


def main():
    with open("operations.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    items = get_filtered_and_sorted(data)

    for i in range(5):
        print(prepare_user_msg(items[i]))
        print()


if __name__ == "__main__":
    main()
