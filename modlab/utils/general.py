# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 11:58:56 2017

@author: Young
"""


#==============================================================================
# General Utility Custom Module
#==============================================================================




#==============================================================================
# Set title
#==============================================================================
def set_title(string):
    # Check if string is too long
    string_size = len(string)
    max_length  = 57
    if string_size > max_length:
        print('TITLE TOO LONG')
    else:
        lr_buffer_len   = int((max_length - string_size) / 2)
        full_buffer_len = lr_buffer_len * 2 + string_size
        print('\n')
        print(full_buffer_len * '=')
        print(full_buffer_len * ' ')
        print(lr_buffer_len * ' ' + string + lr_buffer_len * ' ')
        print(full_buffer_len * ' ')
        print(full_buffer_len * '='+'\n\n')

#==============================================================================
# Find file names in folder
#==============================================================================
# Get file names from path
from os import listdir
def find_filenames( path_to_dir, suffix="" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) and filename.startswith('.') != True ]

# Get all folder names from path
import os
def find_folders(directory_name):
    return [os.path.join(directory_name,folders) for folders in os.listdir(directory_name) if os.path.isdir(os.path.join(directory_name,folders))]

# Get all files (not folders) from path
import os
def filter_folders(directory_name):
    return [f for f in os.listdir(directory_name) if os.path.isfile(os.path.join(directory_name, f))]

import pandas as pd
import os
def get_full_files(folders, suffix_string):
    file_names  = []
    files = []
    for folder in folders:
        for file_ in find_filenames(folder, suffix_string):
            file_names.append(os.path.join(folder, file_))
            files.append(file_)
    return pd.Series(file_names), pd.Series(files)

import os
# Ensure directory exists
def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


#==============================================================================
# Save feature matrix
#==============================================================================
import pickle
def save_data(feature_matrix, save_file):
    # Define output file
    pickle.dump(feature_matrix, open(save_file, 'wb')) 

import pickle
def load_data(file_path):
    return pickle.load(open(file_path, 'rb'))

#==============================================================================
# Flatten list of lists to a list
#==============================================================================
def flatten(x):
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, str):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result

#==============================================================================
# Timestamp
#==============================================================================
import time
import datetime
def get_timestamp():
    return datetime.datetime.fromtimestamp(
        int(time.time())
    ).strftime('%Y_%m_%d_%H_%M_%S')

import time
def print_time_dur(st):
    print('\nDone in', time.strftime('%H:%M:%S', time.gmtime(time.time() - st)), '.\n')

def time_dur(st):
    return time.strftime('%H:%M:%S', time.gmtime(time.time() - st))
    
