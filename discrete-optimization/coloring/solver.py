#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    # print("creat tmp file")
    tmp_file_name = 'tmp.data'
    tmp_file = open(tmp_file_name, 'w')
    tmp_file.write(input_data)
    tmp_file.close()

    sys.path.append('..')
    import helper

    ans =  helper.cpp_runner('gc.cpp',tmp_file_name)
    os.remove(tmp_file_name)

    return ans

import sys

sys.path.append('..')
import helper
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        # with open(file_location, 'r') as input_data_file:
        #     input_data = input_data_file.read()
        print(helper.cpp_runner('gc.cpp',file_location))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')

