#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Sep 7, 2015

@author: davood akbari
'''

from datetime import *
from DAConvertDate import *
from DAClassLibrary import *
import sys


#print ConvertToGregorian(parsiDate()) == ConvertToGregorian(parsiDate())

#pdate = ConvertToParsiDate(datetime.now() + timedelta(hours=-1))

#print parsiDate().DayOfWeekNumber

#print DAstrToParsiDate('1394/01/01 20:30');

out = 'no'
good = 'yes'
try : 
    str = ''
     
    arg = sys.argv[1:4]
    
    for s in arg:
       str += ' ' + s
     
    str = str[1:len(str) - 1]    
         
    title, rule = str.split('=')
    title = title.upper()
    
    if title == 'between'.upper(): 
        bt = rule.split('-')
        
        if (len(bt) > 1):
            if ((datetime.now() >= ConvertToGregorian(DAstrToParsiDate(bt[0]))) and ((datetime.now() <= ConvertToGregorian(DAstrToParsiDate(bt[1]))))):
                out = good
        else:
            if datetime.now() >= ConvertToGregorian(DAstrToParsiDate(bt[0])):
                out = good
                
    if title == 'week'.upper():
        dayN = parsiDate().DayOfWeekNumber
        
        daysN = rule.split(',')
        
        for num in daysN:
            if int(num) == dayN:
                out = good
                break;
                
        
    print out    
        
except:
    print out




