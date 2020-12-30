# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 10:58:37 2020

@author: lab
"""
import numpy as np
k = np.arange(0,370,10)
s = np.sin(np.deg2rad(k))
c = np.cos(np.deg2rad(k))
import csv
with open('plik.csv','w', newline='') as f:
    cf = csv.writer(f,delimiter=';')
    cf.writerow(['k','sin(k)','cos(k)', 'mam nadzieje ze to kurwa dziala'])
    for i in range(len(k)):
        cf.writerow([k[i],s[i],c[i]])
        
        
with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile,delimiter=';', fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
    
with open ('gawron.csv', 'w', newline='') as g:
    gw=csv.writer(g,delimiter=';')
    gw.writerow(['gawron','ty','jebany','pedale'])
    gw.writerow(['robili','cie','w','kanale'])
#cf.writerow([1,2,3])
#cf.writerow(l1)