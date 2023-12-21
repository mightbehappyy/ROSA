def translate(day):
    dict_days = {
        "Mon": "Segunda-feira",
        "Tue": "Terça-feira",
        "Wed": "Quarta-feira",
        "Thu": "Quinta-feira",
        "Fri": "Sexta-feira",
        "Sat": "Sábado",
        "Sun": "Domingo",
    }
    for key, value in dict_days.items():
        if key == day:
            return value
