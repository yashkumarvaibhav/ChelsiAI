import datetime


def date(*args, **kwargs):
    """
    Just return date as string
    :return: date if success, False if fail
    """
    try:
        date = datetime.datetime.now().strftime("%b %d %Y")
    except Exception as e:
        print(e)
        date = False
    return date


def time(*args, **kwargs):
    """
    Just return date as string
    :return: time if success, False if fail
    """
    try:
        time = datetime.datetime.now().strftime("%H:%M")
    except Exception as e:
        print(e)
        time = False
    return time