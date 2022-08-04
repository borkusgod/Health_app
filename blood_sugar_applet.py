# this will be a module handling functions related to blood sugar
# standards for diabetes (american)
# norm = <= 100, 100 >= pre-dia <= 125, dia = > 125
# standards for dia (canuck)
# norm = <= 6.1, 6.1 >= pre-dia <= 6.9 , dia = >= 7.0

from patient_info_module import *


def bs_data():
    bs_dict_empty = {}
    names_combined = create_patient()
    list_container = []
    while True:
        while True:
            bs_entry = input('What was your recorded blood sugar level? ')
            if not bs_entry.isnumeric():
                print('This is not a valid entry.')
            else:
                break
        list_container.append(bs_entry)
        ask_again = input('Is there another entry?')
        if not ask_again:
            break
    bs_dict_empty.update({names_combined: list_container})
    return bs_dict_empty


print(bs_data())
