#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 23:49:26 2017

@author: Young
"""


# Import modules
import os
import glob
import copy
import datetime
import dill as pickle
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Dependent utility function
import os
def ensure_directory(directory):
   if not os.path.exists(directory):
       print('Directory has been created:\n', directory)
       os.makedirs(directory) 

import dill as pickle
def save_data(data, file_path):
    # Define output file
    pickle.dump(data, open(file_path, 'wb')) 

import dill as pickle
def load_data(file_path):
    return pickle.load(open(file_path, 'rb'))

class class1():
    test_class_var = 'a'
    def __init__(self):
        self.test_attibute = 1
        pass
    def do_stuff(self):
        print ('hi')
        

# =============================================================================
# Architecture
# =============================================================================
# Architecture create
class architecture():
    # Initialise
    def __init__(self, project_directory):
        # Project directory
        self.project_directory = project_directory

        # Create project directory
        ensure_directory(self.project_directory)
        
        # Allocate variables
        self.overwrite_flag = ''
    

    def get_latest_architecture_version(self): # requires self.architecture_pdf
        latest_architecture = self.architecture_pdf.sort_values('version_date', ascending=False).iloc[0]
        
        # Metadata
        self.architecture_name = latest_architecture['name']
        self.description = latest_architecture['description']
        self.version = latest_architecture['version']
        self.version_date = latest_architecture['version_date']
        
        # Inferred properties
        self.architecture_dir = latest_architecture['architecture_dir']
        self.architecture_file_path = latest_architecture['architecture_file_path']
        
        # Process network
        self.process_network = latest_architecture['process_network']
        
    # Create
    def create(self, name, description = None):
        # Inferred properties
        self.architecture_dir = os.path.join(self.project_directory, 'Architecture')
        self.architecture_file_path = os.path.join(self.architecture_dir, name + '.pkl')
        
        # Define starting architecture
        starting_architecture_dict = {'name': name,
                                     'description': description,
                                     'version': '0.1',
                                     'version_date': datetime.datetime.now(),
                                     'architecture_dir': self.architecture_dir,
                                     'architecture_file_path': self.architecture_file_path,
                                     'process_network': []}
        
        # Create architecture
        self.architecture_pdf = pd.DataFrame.from_dict([starting_architecture_dict])
        
        # Create architecture directory
        ensure_directory(self.architecture_dir)
        
        # Retrieve the architecture
        self.get_latest_architecture_version()
        
        # Check if architecture exists and create
        while os.path.exists(self.architecture_file_path):
            overwrite_text = 'Architecture ' + str(self.architecture_name) + ' exists already.\nDo you want to overwrite? [y/n] : \t\n\n'
            self.overwrite_flag = input(overwrite_text)
            if self.overwrite_flag in ['y', 'n']:
                break
        if self.overwrite_flag == 'y':
            save_data(self.architecture_pdf, self.architecture_file_path)
            print('\nArchitecture overwritten.')
        elif self.overwrite_flag == 'n':
            print('\nArchitecture not created.')
        else:
            save_data(self.architecture_pdf, self.architecture_file_path)
            print('\nArchitecture created.')
    
    # Load
    def load(self, name):
        # Check if architecture exists
        self.architecture_name = name
        
        # Inferred properties
        self.architecture_dir = os.path.join(self.project_directory, 'Architecture')
        self.architecture_file_path = os.path.join(self.architecture_dir, self.architecture_name + '.pkl')
        
        if not os.path.exists(self.architecture_file_path):
            print('\nArchitecture', self.architecture_name,'does not exist!\n')
        else:
            self.architecture_pdf = load_data(self.architecture_file_path)
            
            # Retrieve the architecture
            self.get_latest_architecture_version()
            
            print('\nArchitecture', self.architecture_name,'loaded.\n')
    
    # Delete
    def delete(self):
        try:
            os.remove(self.architecture_file_path)
            print('Deleted architecture', self.architecture_name)
        except AttributeError:
            pass
        try:
            os.rmdir(self.architecture_dir)
            print('Deleted architecture folder')
        except OSError:
            print('Cannot delete architecture folder - directory not empty.')
        
#    def update_process(self, new_process_network):
    # RESTRICT ACCESS TO PDF
    def save(self, version_number = None):
        # Get old architecture
        old_architecture_pdf = copy.deepcopy(self.architecture_pdf)
        previous_version_pdf = old_architecture_pdf.sort_values('version_date', ascending=False).iloc[0]
        previous_version = previous_version_pdf['version']
        
        # Define new architecture
        if version_number:
            if not isinstance(version_number, str):
                raise Exception('Version number must be a string')
            else:
                dummy_v_num = version_number
        elif not isinstance(self.version, str):
            raise Exception('Version number must be a string')
        elif previous_version == self.version:
            dummy_v_num = '%.2f' % (float(self.version)+0.01)
        else:
            dummy_v_num = self.version
            
        updated_architecture_dict = {'name': self.architecture_name,
                                     'description': self.description,
                                     'version': dummy_v_num,
                                     'version_date': datetime.datetime.now(),
                                     'architecture_dir': self.architecture_dir,
                                     'architecture_file_path': self.architecture_file_path,
                                     'process_network': self.process_network}
        
        # Create architecture
        old_architecture_pdf = copy.deepcopy(self.architecture_pdf)
        self.architecture_pdf = pd.DataFrame.from_dict([updated_architecture_dict])
        self.architecture_pdf = pd.concat([old_architecture_pdf, self.architecture_pdf])
        
        # Update parameters
        self.get_latest_architecture_version()
        
        # Save
        save_data(self.architecture_pdf, self.architecture_file_path)
        print('\nArchitecture updated.')

    #
    def plot_process_flow(self):
        


#    # Execute architecture
#    def run(self, execute_from_process_number):

#    # Save dependencies
#    def save_dependencies


# =============================================================================
# Test
# =============================================================================
# Test save
a = architecture(project_directory = '/Users/Young/Documents/Capgemini/Learning/Python Development/Project_Test')
a.create(name = 'archi_test')
a.__dict__


a.version = '0.2'
a.description = 'nothing special'
a.save()
a.__dict__

# Test version load
b = architecture(project_directory = '/Users/Young/Documents/Capgemini/Learning/Python Development/Project_Test')
b.create(name = 'archi_test2')

c = architecture(project_directory = '/Users/Young/Documents/Capgemini/Learning/Python Development/Project_Test')
c.load('archi_test')
c.__dict__


# Create first architecture







