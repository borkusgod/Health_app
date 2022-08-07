from datetime import datetime


def format_cur_4_sav():
    x = datetime.now()
    # formatted = x.strftime("%B_%d_%Y@%Hhrs%Mmins")
    formatted = x.strftime("%B_%d_%Y_%H_%M")
    # print(type(formatted))
    return formatted


print(format_cur_4_sav())