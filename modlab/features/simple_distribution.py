#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 17:44:55 2017

@author: Young
"""

import os
import sys

package_parent = '../..'
script_dir = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser("__file__"))))
model_building_lab_dir = os.path.normpath(os.path.join(script_dir, package_parent))
sys.path.append(model_building_lab_dir)

.
import numpy as np
from modlab.features.base import BaseFeature

from abc import ABCMeta, abstractmethod

class BaseFeature(metaclass = ABCMeta):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def describe(self):
        pass
    @abstractmethod
    def run(self):
        pass
    @abstractmethod
    def save(self):
        pass

class Histogram(BaseFeature):
    def __init__(self):
        #self.name='Histogram'
        self.description='Creates a histogram of N bins'
        #self.n=10
    def name(self):
        print(self.name)
    def describe(self):
        print(self.description)
    def run(self):
        pass
    def save(self):
        pass
    
if __name__ == "__main__":
    print('hi')
    
#
#x = Histogram()
#x = InClass()
#x.printHam()
#
#x.describe()