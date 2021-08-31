# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 17:25:31 2021

@author: ankit
"""

import pandas as pd

df=pd.DataFrame({"country":['UK','Germany','USA','India']})
 
countries_to_keep=['UK', 'India']
print(df[df.country.isin(countries_to_keep)])
  
print(df[~df.country.isin(countries_to_keep)])
  