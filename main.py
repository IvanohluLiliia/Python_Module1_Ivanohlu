import os
from mymodule import is_triangle, triangle_area, translate

FILE_NAME = "MyData.txt"

def read_data():
    if not os.path.exists(FILE_NAME):
        return None

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            lines = f.readlines()

        a1, b1, c1 = map(float, lines[0].strip().split())
        a2, b2, c2 = map(float, lines[1].strip().split())
        lang = lines[2].strip()

        return a1, b1, c1, a2, b2, c2, lang
    except:
        return None


def write_data():
    a1, b1, c1 = map(float, input("Введіть a1, b1, c1: ").split(","))
    a2, b2, c2 = map(float, input("Введіть a2, b2, c2: ").split(","))
    lang = input("Введіть мову (uk/en): ")

    with open(FILE_NAME, "w", encoding="utf-8") as f:
        f.write(f"{a1} {b1} {c1}\n")
        f.write(f"{a2} {b2} {c2}\n")
        f.write(lang)

    print("Дані збережено в файл")
    return None


def main():
    data = read_data()

    if data is None:
        write_data()
        return

    a1, b1, c1, a2, b2, c2, lang = data

    print(f"Мова: {lang}")

    if not is_triangle(a1, b1, c1) or not is_triangle(a2, b2, c2):
        print(translate("not_triangle", lang))
        return

    s1 = triangle_area(a1, b1, c1)
    s2 = triangle_area(a2, b2, c2)

    print(f"Площа першого трикутника: {s1:.2f}")
    print(f"Площа другого трикутника: {s2:.2f}")

    if s1 > s2:
        print(translate("first_bigger", lang))
    elif s2 > s1:
        print(translate("second_bigger", lang))
    else:
        print(translate("equal", lang))


if __name__ == "__main__":
    main()