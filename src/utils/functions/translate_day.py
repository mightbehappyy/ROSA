def translate_day(day):
    dict_days = {
        "seg.": "Segunda-feira",
        "ter.": "Terça-feira",
        "qua.": "Quarta-feira",
        "qui.": "Quinta-feira",
        "sex.": "Sexta-feira",
        "sab.": "Sábado",
        "dom.": "Domingo",
    }
    for key, value in dict_days.items():
        if key == day:
            return value
