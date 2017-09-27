'''
Created on Jun 12, 2017

@author: rezakhoshkangini
'''
import subprocess, os
import glob, os
from subprocess import call
from os import listdir
from os.path import isfile, join

def main():
    #listing the name of the csv files
    os.chdir("/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/newExperiment_Trento/Sections/Sections_new_features/TestforOrders/csv_for_Atribute_selection")
    for filename in glob.glob("*.csv"):
        print(filename)
        # creating an empty ARFF file 
        file_out = open("/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/newExperiment_Trento/Sections/Sections_new_features/TestforOrders/Arff_for_AttributeSelection"+str(filename)+'.arff', "w")
        call(['java', '-cp', '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Python_Code/weka.jar', 'weka.core.converters.CSVLoader', '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/newExperiment_Trento/Sections/Sections_new_features/TestforOrders/csv_for_Atribute_selection/'+str(filename), '>', '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/newExperiment_Trento/Sections/Sections_new_features/TestforOrders/Arff_for_AttributeSelection/'+str(filename)+'.arff'],
                        stdout=file_out)


if __name__ == '__main__':
    
    try:
        
        main()
    except Exception as ex:
        print(ex)

    print("Converting is Finished")