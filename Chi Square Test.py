# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 11:14:36 2020

@author: Devil
"""
import numpy as np
from scipy.stats import chi2_contingency 
  
# defining the table 
data = [[ 262,234,204,190,210], [220,220,220,220,220]]
stat, p, dof, expected = chi2_contingency(data) 
  
# interpret p-value 
alpha = 0.05
print("p value is " + str(p)) 
if p <= alpha: 
    print('Dependent (reject H0)') 
else: 
    print('Independent (H0 holds true)') 
    
    
Output:
p value is 0.12953316432236356
Independent (H0 holds true)
