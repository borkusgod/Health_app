# this is the module for creating the patient info

def create_patient():
    while True:
        f_n = input('Please enter the first name: ')
        if not f_n.isalpha():
            print('This is not a valid entry. Please try again.')
        else:
            break
    while True:
        l_n = input('Please enter the last name: ')
        if not l_n.isalpha():
            print('This is not a valid entry. Please try again.')
        else:
            break
    names_combined = l_n + '_' + f_n
    return names_combined


# print(create_patient())
