#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:04:48 2017

@author: Young
"""


# Import modules
import os
import glob
import datetime

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Dependent utility function
import os
def ensure_directory(directory):
   if not os.path.exists(directory):
       os.makedirs(directory) 


# =============================================================================
# Architecture
# =============================================================================
# Architecture create
class architecture():
    # Initialise
    def __init__(self, name, project_directory, description = None):
        # Properties
        self.architecture_name = name
        self.project_directory = project_directory
        self.description = description
        self.create_date = datetime.datetime.now()
        
        # Inferred properties
        self.architecture_path = os.path.join(project_directory, 'Architecture')
        self.architecture_file_path = os.path.join(self.architecture_path, self.architecture_name + '.parquet')

        # Allocate variables
        self.architecture_pdf = ''
        self.overwrite_flag = ''
        
    # Create
    def create(self):
        # Create project directory
        ensure_directory(self.project_directory)
        
        # Create architecture directory
        ensure_directory(self.architecture_path)
        
        # Create empty architecture
        self.architecture_pdf = pd.DataFrame([])
        architecture_file_table = pa.Table.from_pandas(self.architecture_pdf)
        
        # Check if architecture exists and create
        while os.path.exists(self.architecture_file_path):
            overwrite_text = 'Architecture ' + str(self.architecture_name) + ' exists already.\nDo you want to overwrite? [y/n] : \t\n\n'
            self.overwrite_flag = input(overwrite_text)
            if self.overwrite_flag in ['y', 'n']:
                break
        if self.overwrite_flag == 'y':
            pq.write_table(architecture_file_table, self.architecture_file_path)
            print('\nArchitecture overwritten.')
        elif self.overwrite_flag == 'no':
            print('\nArchitecture not created.')
        else:
            pq.write_table(architecture_file_table, self.architecture_file_path)
            print('\nArchitecture created.')

    # Open
    def open(self):
        # Check if architecture exists
        if not os.path.exists(self.architecture_file_path):
            print('\nArchitecture', self.architecture_name,'does not exist!\n')
        else:
            self.architecture_pdf = pd.read_parquet(self.architecture_file_path, engine='pyarrow')
            print('\nArchitecture', self.architecture_name,'loaded.\n')
          
    # Delete
    def delete(self):
        os.remove(self.architecture_file_path)
        print('Deleted architecture', self.architecture_name)
        try: 
            os.rmdir(self.architecture_path)
            print('Deleted architecture folder')
        except OSError:
            print('Cannot delete architecture folder - directory not empty.')
        
#    # Execute architecture
#    def run(self, execute_from_process_number):

# =============================================================================
# Test
# =============================================================================
a = architecture(name = 'hi1', 
                 description = 'bye',
                 project_directory = '/Users/Young/Documents/Capgemini/Learning/Python Development/Project_Test')

a.create()
a.open()
a.delete()
a.architecture_pdf


b = architecture(name = 'hi3', 
                 project_directory = '/Users/Young/Documents/Capgemini/Learning/Python Development/Project_Test')
b.open()
a.create_date
b.create_date

a.create()
b.create()

