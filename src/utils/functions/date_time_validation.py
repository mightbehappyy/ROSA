import re
from datetime import datetime


async def validate_date_time_format(date_value, start_time_value, ending_time_value):
    date_pattern = r"\d{2}-\d{2}-\d{4}"
    time_pattern = r"\d{2}:\d{2}"

    invalid_part = None

    if not re.match(date_pattern, date_value):
        invalid_part = "data"

    if not (re.match(time_pattern, start_time_value) and re.match(time_pattern, ending_time_value)):
        invalid_part = "hora"

    try:

        datetime.strptime(date_value, "%d-%m-%Y")
        datetime.strptime(start_time_value, "%H:%M")
        datetime.strptime(ending_time_value, "%H:%M")
    except ValueError as e:
        if "day is out of range" in str(e):
            invalid_part = "data"
        else:
            invalid_part = "hora"

    return invalid_part if invalid_part else "formato válido"
