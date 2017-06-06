
import subprocess, os
from subprocess import call

class convert(object):

    content = []
    name = ''

    def __init__(self):
        print ('\nStarted to Convert to arff.')
        self.convertToArff()
        
        

    #converting CSV to Arff
    def convertToArff(self):
        
        for counter in range(1,114):
            file_out = open("/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/NewCSV/BindedData/IndUsers/Arff/player"+str(counter)+".arff", "w")
            call(['java', '-cp', '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Python_Code/weka.jar', 'weka.core.converters.CSVLoader', '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/NewCSV/BindedData/IndUsers/CsV/playerLbl_comu_'+str(counter)+'.csv', '>', '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/NewCSV/BindedData/IndUsers/Arff/player_comu'+str(counter)+'.arff'],
                        stdout=file_out)
            
           
            
            
#            
       
    
    
    
    
    