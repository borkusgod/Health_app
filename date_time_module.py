from datetime import datetime


def format_cur_4_sav():
    x = datetime.now()
    formatted = x.strftime("%Y_%m_%d@%Hhrs%Mmins")
    return formatted

