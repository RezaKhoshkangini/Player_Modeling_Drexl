'''
Created on Sep 26, 2017

@author: rezakhoshkangini
'''
import subprocess, os
from subprocess import call

class Class_Order_Extration(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        print ('\nStarted to find the order.')
        self.orderextarction()
        
        
    def orderextraction(self):
        
        print('hello reza')
        
        for counter in range(0,4):
            file_out = open("/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/newExperiment_Trento/Sections/Sections_new_features/TestforOrders/Arff_for_AttributeSelection/out"+str(counter+1)+".txt", "w")
            cmd =['java', '-Xmx1024M', '-cp', '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Python_Code/weka.jar', 'weka.attributeSelection.GainRatioAttributeEval', '-s' + " weka.attributeSelection.Ranker -T -1.7976931348623157E308 -N, -1" + '-i', '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/newExperiment_Trento/Sections/Sections_new_features/TestforOrders/Arff_for_AttributeSelection/section'+str(counter)+'.arff']
            call(['java', '-Xmx1024M', '-cp', '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Python_Code/weka.jar', 'weka.attributeSelection.GainRatioAttributeEval', '-s' , + " weka.attributeSelection.Ranker -T -1.7976931348623157E308 -1 " + , '-i' , '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/newExperiment_Trento/Sections/Sections_new_features/TestforOrders/Arff_for_AttributeSelection/section1.arff'], stdout=file_out)


 