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

# print(patient_fdata['John Doe']['bp_data_date_entered'][1]) -> 120/85
# print(patient_fdata['John Doe']['bs_data_date_entered'][1]) -> 118

Another alternative would be: 

patient_records_time_stamp = {
    {'patient_a': [['120/85', '120/85', '120/85'],['125', '118', '119']]},
    {'patient_b': [['120/85', '120/85', '120/85'],['125', '118', '119']]}
}

