import glob
import json
from date_time_module import *


def bp_json_file(from_input):
    json_object = json.dumps(from_input, indent=4)

    # save func output to json
    with open(('patient_records' + (format_cur_4_sav()) + '.json'), "w") \
            as outfile:
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
    return data

