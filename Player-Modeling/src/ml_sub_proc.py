'''
Created on May 15, 2017

@author: rezakhoshkangini
'''


import subprocess, os

class Sub_Machine(object):

    content = []
    name = ''

    def __init__(self):
        self.classification()
        
        
    def classification(self): 
        
        for counter in range(0,5):
            cmd = ['java', '-cp', '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Python_Code/weka.jar', 'weka.classifiers.bayes.NaiveBayes', '-t' , '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/NewCSV/BindedData/Section'+str(counter)+'.arff']
            print (' '.join(cmd))
            data = subprocess.check_output(cmd)
            data = [line.strip().split(b'\t') for line in bytes.splitlines(data)][0:-1]
           # for row in data:
           #     print(*row)
              

        
