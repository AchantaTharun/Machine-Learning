# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 19:26:33 2019

@author: Tharun Achanta
"""

import pandas as pd

melbourne_file_path = 'C:/Users/Tharun Achanta/Documents/GitHub/Machine-Learning/First model/Datasets/melb_data.csv'

melbourne_data = pd.read_csv(melbourne_file_path)

#print(melbourne_data)

melbourne_data = melbourne_data.dropna(axis=0)
print(melbourne_data)