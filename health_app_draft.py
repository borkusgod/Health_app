import os
from file_related_module import bp_json_file
from time import sleep
from blood_pressure_applet import *

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


bp_values2dict = {
                  'doe_jon': ['125/85', '130/85', '135/85'],
                  'doe_jane': ['135/85', '140/85', '150/85'],
                  'doe_jim': ['135/85', '140/85', '150/85'],
                  'doe_josh': ['135/85', '140/85', '150/85'],
                  'doe_tom': ['135/85', '140/85', '150/85']
                  }

bp_values2dict1 = {
                    'doe_jon': [
                                [{'bp': ['125/80', '115/80', '125/81']}],
                                [{'bs': ['115', '110', '100']}]
                                ],
                    'doe_jane': [
                                [{'bp': ['125/80', '115/80', '125/81']}],
                                [{'bs': ['115', '110', '100']}]
                    ]
                    }

# bp_values2list = (('doe_jon',  ['125/85', '130/85', '135/85']),
#                   ('doe_jane',  ['125/85', '130/85', '135/85']))

# create_pat_bp_records = enter_multi_pats()
create_dict = bp_values2dict1
# create_list = bp_values2list
# print(create_list)
# print(create_dict)
# this will ask for pat info


# bp_json_file(create_pat_bp_records)
bp_json_file(create_dict)
# this will take above func and save it to json with current date and time
# and display how many files are in directory
