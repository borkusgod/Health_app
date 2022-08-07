This will be an app that will have a number of functions built in to 
monitor your health and also keep the data stored in a database. 

Currently scheduled is to rewrite the individual modules as to perform 
function and then write or append to main .json file that houses all data. 
Will leave blank where applicable. This will have to be a re-write of json 
output because it's just like a dictionary where you can only have a key 
and value

json format:

patient_fdata = {
    'John Doe' : [
        {
            'bp_data_date_entered' : '['130/85', '120/85', '110/85']',
            # numerous entries separated by dates
        },
        {
            'bs_data_date_entered' : '['125', '118', '119']',
        }],
     'Jane Doe' : [
        {
            'bp_data_date_entered' : '['120/85', '120/85', '120/85']',
            # numerous entries separated by dates
        },
        {
            'bs_data_date_entered' : '['125', '118', '119']',
        }],
}

# format to read above would be:
# (remember to be mindful of the difference between lists and dicts. Lists 
# are reference by index and dicts by keys aka 'names' etc)

# pat_dict_for_testing = {'doe_jon': ['125/85', '130/85', '135/85'],
#                        'doe_jane': ['135/85', '140/85', '150/85']}
# pat_list_for_testing = (('doe_jon',  ['125/85', '130/85', '135/85']),
#                        ('doe_jane',  ['125/85', '130/85', '135/85']))

# print(create_dict)
# print(create_dict['doe_jon'][1]) -> 130/85
# print(create_list)
# print(create_list[0][1][1]) -> 130/85

# print(patient_fdata['John Doe']['bp_data_date_entered'][1]) -> 120/85
# print(patient_fdata['John Doe']['bs_data_date_entered'][1]) -> 118

Another alternative would be: 

patient_records_time_stamp = {
    {'patient_a': [['120/85', '120/85', '120/85'],['125', '118', '119']]},
    {'patient_b': [['120/85', '120/85', '120/85'],['125', '118', '119']]}
}

