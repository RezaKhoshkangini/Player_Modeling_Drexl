'''
Created on May 31, 2017

@author: rezakhoshkangini

'''
import subprocess, os
import glob, os
from subprocess import call
from os import listdir
from os.path import isfile, join

def main():
    os.chdir("/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/taemile-aiide-notrim-arff")
    for filename in glob.glob("*.arff"):
        print(filename)
        file_out = open("/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/Time_based_Data/"+str(filename)+'.csv', "w")
        call(['java', '-cp', '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Python_Code/weka.jar', 'weka.core.converters.CSVSaver', '-i', '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/taemile-aiide-notrim-arff/'+str(filename), '-o', '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/Time_based_Data/'+str(filename)+'.csv'],
                        stdout=file_out)


if __name__ == '__main__':
    
    try:
        
        main()
    except Exception as ex:
        print(ex)

    print("Converting is Finished")