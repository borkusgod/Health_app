import os
from date_time_module import *
from time import sleep
import json
# for saving information
import glob
# for dealing with file system
from blood_pressure_applet import *
# how to import functions from separate py file

# global variables
body_weight = None
body_height = None
smoker = False
drinker = False
blood_sugar = None
BP_upper = None
BP_lower = None


# Opening splash screen
def opening_screen():
    print('Welcome to the G Corporation Health Assistant')
    copyright_stamp = '(C) Copyright 1995'
    formatted_copy = copyright_stamp.rjust(55, ' ')
    # print(f"{copyright_stamp:>55}")
    # print(copyright_stamp.rjust(55, ' '))
    print(f'{formatted_copy} \n')

    print('This program was designed and developed by William Bourque')
    print('Running on Python 3.10')
    print('Designed and coded by William Bourque')
    print('This app is designed to monitor your health so\n'
          'you can be at your optimal performance for the hive.')
    # clear screen after 5 seconds
    sleep(5)

    os.system('cls')

# ----------program start\

# opening_screen()

# beginning of bp section


create_pat_bp_records = enter_multi_pats()
json_object = json.dumps(create_pat_bp_records, indent=4)

# save func output to json
with open(('patient_records' + (format_cur_4_sav()) + '.json'), "w") as outfile:
    outfile.write(json_object)

# use this to check file contents
glob_container = None
# counter for below
from_for = 0
for name in glob.glob('*.json'):
    from_for += 1
    glob_container = name
    # print(name)
print(f'There are {from_for} patient record files in this directory.')
f = open(glob_container)
data = json.load(f)
dict(data)
print(data)



