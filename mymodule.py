import math

def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def translate(text, lang):
    translations = {
        "uk": {
            "not_triangle": "Трикутник не існує",
            "first_bigger": "Площа першого трикутника більше другого",
            "second_bigger": "Площа другого трикутника більше першого",
            "equal": "Площі трикутників рівні"
        },
        "en": {
            "not_triangle": "Triangle does not exist",
            "first_bigger": "First triangle area is larger",
            "second_bigger": "Second triangle area is larger",
            "equal": "Areas are equal"
        }
    }

    if lang not in translations:
        lang = "uk"

    return translations[lang].get(text, text)