#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 17:44:55 2017

@author: Young
"""

#from .base import BaseFeature
import numpy as np
from abc import ABCMeta, abstractmethod

class BaseFeature(metaclass = ABCMeta):
    @abstractmethod
    def __init__(self):
        self.name
        self.description
    @abstractmethod
    def name(self):
        print(self.name)
    @abstractmethod
    def describe(self):
        print(self.description)
    @abstractmethod
    def run(self):
        pass
    @abstractmethod
    def save(self):
        pass

class Histogram(BaseFeature):
    def __init__(self, params):
        self.name='Histogram'
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

x = Histogram()
x = InClass()
x.printHam()