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


print  parsiDate()
print convertToGregorian(parsiDate())
print convertToGregorian(parsiDate())

print convertToGregorian(parsiDate()) == convertToGregorian(parsiDate())

pdate = convertToParsiDate(datetime.now() + timedelta(hours=-1))

print pdate

print parsiDate().DayOfWeekNumber

print convertToGregorian(strToParsiDate('1396/07/12 12:51'));

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
            if ((datetime.now() >= convertToGregorian(strToParsiDate(bt[0]))) and ((datetime.now() <= convertToGregorian(strToParsiDate(bt[1]))))):
                out = good
        else:
            if datetime.now() >= convertToGregorian(strToParsiDate(bt[0])):
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




