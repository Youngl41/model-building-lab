#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 17:26:21 2017

@author: Young
"""

from abc import ABCMeta, abstractmethod

class BaseFeature(metaclass = ABCMeta):
    @abstractmethod
    def __init__(self):
        self.name
        self.description
    @abstractmethod
    def name(self):
        print('self.name')
    @abstractmethod
    def describe(self):
        print('self.description')
    @abstractmethod
    def run(self):
        pass
    @abstractmethod
    def save(self):
        pass
