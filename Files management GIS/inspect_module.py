# -*- coding: utf-8 -*-
"""
Created on Wed May 09 20:26:20 2018

@author: ASUS
"""

import inspect

import anydbm as module

functions = inspect.getmembers(module, inspect.isfunction)