from datetime import datetime


def current_day():
    x = datetime.now()
    formatted = x.strftime("%Y_%m_%d@%Hhrs%Mmins")
    return formatted

