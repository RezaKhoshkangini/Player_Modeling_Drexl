'''
Created on May 16, 2017

@author: rezakhoshkangini
'''
import subprocess, os

class Ind_Classification(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.classification() 
        
    def classification(self): 
        
                
        for counter in range(1,114):
            cmd = ['java', '-cp', '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Python_Code/weka.jar','weka.classifiers.bayes.NaiveBayes' , '-t' , '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/NewCSV/BindedData/IndUsers/Arff/player'+str(counter)+'.arff', '-x', '6', '-o']
            print (' '.join(cmd))
            data = subprocess.check_output(cmd)
            data = [line.strip().split(b'\t') for line in bytes.splitlines(data)][0:-1] 
            for row in data:
                print(*row)
                
             