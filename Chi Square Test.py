# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 11:14:36 2020

@author: Devil
"""
import numpy as np
from scipy.stats import chi2_contingency 
  
# defining the table 
a1= [262]
a2= [234]
a3= [204]
a4= [190]
a5= [210]
data = np.array([a1, a2, a3, a4, a5])
stat, p, dof, expected = chi2_contingency(data) 
  
# interpret p-value 
alpha = 0.05
print("p value is " + str(p)) 
if p <= alpha: 
    print('Dependent (reject H0)') 
else: 
    print('Independent (H0 holds true)') 
    
    
Output:
p value is 1.0
Independent (H0 holds true)
