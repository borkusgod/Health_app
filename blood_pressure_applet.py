# this will be a specific module for blood pressure
# def input_patient_name():
#     f_n = input('Please enter the first name: ')
#     l_n = input('Please enter the last name: ')
#     names_combined = f_n + '_' + l_n
#     return names_combined
#
#
# def patient_bp_list():
#     list_loop = True
#     list_container = []
#     print('Making list for bp entries')
#     while True:
#         sys_entry = input('What is your systolic (The top number): ')
#         dia_entry = input('What is your diastolic (The bottom number): ')
#         combine_for_list = sys_entry + '/' + dia_entry
#         list_container.append(combine_for_list)
#         ask_again = input('Is there another entry?')
#         if not ask_again:
#             break
#     return list_container


def pat_data_2_dict():
    dict_empty = {}
    # while True:
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
    names_combined = f_n + '_' + l_n
    list_container = []
    while True:
        while True:
            sys_entry = input('What is your systolic (The top number): ')
            if not sys_entry.isnumeric():
                print('This is not a valid entry.')
            else:
                break
        while True:
            dia_entry = input('What is your diastolic (The bottom number): ')
            if not dia_entry.isnumeric():
                print('This is not a valid entry.')
            else:
                break
        combine_for_list = sys_entry + '/' + dia_entry
        list_container.append(combine_for_list)
        ask_again = input('Is there another entry?')
        if not ask_again:
            break
    dict_empty.update({names_combined: list_container})
    return dict_empty


# def making_list_with_mult():
#     func_state = True
#     list_container = []
#     print('this func will be for making lists with multiple entries')
#
#     def insert_into_list():
#         sys_input = input('Please enter your top number: ')
#         dia_input = input('Please enter your bottom number: ')
#         conv_for_list = sys_input + '/' + dia_input
#         list_container.append(conv_for_list)
#
#     while func_state:
#         insert_into_list()
#         ask_again = input('Is there another entry? ')
#         if not ask_again:
#             break
#     return list_container


def patient_count(patients):
    how_many_pats = len(patients)
    return f'There are {how_many_pats} patients in this list.'


def define_if_hypertensive(patients):
    # print(f'Printouut of patients in original format: \n{patients}')
    # print('\n')
    # set criteria for if considered hypertension
    # if sys >= 140 or dia >= 90, or sys >= 180 and dia >= 110
    labelled_hype = 0
    patient_num = 0
    for each in patients:
        sys_container = 0
        dia_contatiner = 0
        patient_num += 1
        # print(f'Patient number {patient_num} has the following readings: '
        #       f'{each}')
        # print(f'The length of each patients list: {len(each)}')
        for each_again in each:
            # print(f'Each reading for patient: {each_again}')
            top_bot = each_again.split('/')
            sys2int = int(top_bot[0])
            dia2int = int(top_bot[1])
            # print(f'The systolic for each reading is: {sys2int}\n'
            #       f'and the diastolic for each is: {dia2int}')
            sys_container += sys2int
            dia_contatiner += dia2int
        averaged_sys = sys_container / (len(each))
        averaged_sys = int(averaged_sys)
        averaged_dia = dia_contatiner / (len(each))
        averaged_dia = int(averaged_dia)
        # print(f'{averaged_sys}/{averaged_dia}')
        if averaged_sys >= 140 or averaged_dia >= 90:
            labelled_hype += 1
        if averaged_sys >= 180 and averaged_dia >= 110:
            labelled_hype += 1
        # print('\n')
    # print(f'Number of patients labelled with hypertension: {labelled_hype}')
    # print('\n')
    return labelled_hype


