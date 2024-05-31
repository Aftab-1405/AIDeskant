from datetime import datetime, date
# This function returns current time from an importing datetime library


def get_time():
    now = datetime.now()

    current_time = now.strftime("%H hours %M minutes ")
    return current_time

# This function will return the current hour in the form of string.


def get_hours():
    now = datetime.now()
    return now.strftime("%H")


def get_date():
    return str(date.today())
