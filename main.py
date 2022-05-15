from pprint import pprint
from list_adt import CustomizedPythonList


def main():
    list_adt = CustomizedPythonList()

    for k in range(100):
        list_adt.append(k)

    output = pprint({
        "items": list_adt.items,
        "number_of_items": list_adt.number_of_items,
        "length": len(list_adt.items)
    })

    return output


if __name__ == "__main__":
    main()
