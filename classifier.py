# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import os 

dir_path=os.path.dirname(os.path.abspath(__file__))
reviews_path = dir_path+r'/resources/Amazon reviews'

def createdf(path,sentiment):        
  
        
    titles=[]
    with open(path) as fp:
        lines= [line.strip() for line in fp]
        for i, line in enumerate(fp):
            if '<title>' in line:
                print(lines[i+1])
                titles.append(lines[i+1])
                
                
    body=[]
    with open(path) as fp:
        lines=[line.strip() for line in fp]
        for i, line in enumerate(fp):
            if '<review_text>' in line:
                print(lines[i+1])
                body.append(lines[i+1])
                
    
    truth=[sentiment for i in range(len(titles))]
  
    return titles,truth

filenames=[reviews_path+r'/books/negative.review',reviews_path+ r'/books/positive.review',reviews_path+r'/dvd/negative.review',
          reviews_path+r'/dvd/positive.review',reviews_path+r'/electronics/negative.review',reviews_path+r'/electronics/positive.review',
          reviews_path+r'/kitchen_&_housewares/negative.review',reviews_path+r'/kitchen_&_housewares/positive.review']

text=[]
truth=[]
for i in range(len(filenames)):
    if i%2==0:
        sentiment='negative'
    else:
        sentiment='positive'
    run=createdf(filenames[i],sentiment)
    text+=run[0]
    truth+=run[1]

len(text)


titles=[]
with open(reviews_path+r'/books/negative.review') as fp:
    #lines= [line.strip() for line in fp]
    for i, line in enumerate(fp):
        if '<title>' in line:
            print(lines[i+1])
            titles.append(lines[i+1])
titles
            
body=[]
with open(reviews_path) as fp:
    lines=[line.strip() for line in fp]
    for i, line in enumerate(fp):
        if '<review_text>' in line:
            print(lines[i+1])
            body.append(lines[i+1])


