'''
Created on Sep 28, 2017

@author: rezakhoshkangini
'''
import sys
import csv 
#import weka.core.jvm as jvm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def config():
    
        play_feature_dic_new={'items_visited_total':{'Achiever':'low','Explorer':'high','Careless':'high','other':'low'},
                          'questions_right_ratio':{'Achiever':'high','Explorer':'high','Careless':'low','other':'low'},
                          'questions_visited_total':{'Achiever':'low','Explorer':'high','Careless':'high','other':'low'},
                          'questions_wrong_ratio':{'Achiever':'low','Explorer':'low','Careless':'high','other':'high'},
                          'time_read_time_total':{'Achiever':'low','Explorer':'low','Careless':'high','other':'low'},
                          'time_nav_time_total':{'Achiever':'low','Explorer':'high','Careless':'low','other':'low'},
                          'time_map/time_total':{'Achiever':'high','Explorer':'low','Careless':'low','other':'low'},
                          'reading_min':{'Achiever':'low','Explorer':'low','Careless':'low','other':'low'},
                          'reading_max':{'Achiever':'low','Explorer':'low','Careless':'low','other':'low'},
                          'item_visited_new':{'Achiever':'low','Explorer':'low','Careless':'low','other':'high'},
                          'items_revisits':{'Achiever':'low','Explorer':'high','Careless':'low','other':'low'},
                          'questions_revisits':{'Achiever':'low','Explorer':'low','Careless':'low','other':'low'}
                        }
        
        my_path="/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/newExperiment_Trento/Sections/Sections_new_features/Labeled/congic.csv"
        styles=['Achiever','Explorer','Careless','other']
        
        df=pd.DataFrame(play_feature_dic_new)
        df.to_csv(my_path) 
            #writer = df.to_csv(csv_file,index = False)
        #print("writing is Finished")
        
        return play_feature_dic_new