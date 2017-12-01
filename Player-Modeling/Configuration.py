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
import time

def config(sec):
    
        if sec==0:
             play_feature_dic_new={'items_visited_total':{'Achiever':'low','Explorer':'low','Careless':'high','other':'low'},
                          'questions_right_ratio':{'Achiever':'high','Explorer':'high','Careless':'low','other':'low'},
                          'questions_visited_total':{'Achiever':'high','Explorer':'high','Careless':'high','other':'high'},
                          'questions_wrong_ratio':{'Achiever':'low','Explorer':'low','Careless':'high','other':'high'},
                          'time_read_time_total':{'Achiever':'high','Explorer':'low','Careless':'high','other':'low'},
                          'time_nav_time_total':{'Achiever':'high','Explorer':'high','Careless':'low','other':'low'},
                          'time_map/time_total':{'Achiever':'low','Explorer':'low','Careless':'low','other':'low'},
                          'reading_min':{'Achiever':'low','Explorer':'low','Careless':'low','other':'low'},
                          'reading_max':{'Achiever':'low','Explorer':'low','Careless':'low','other':'low'},
                          'item_visited_new':{'Achiever':'low','Explorer':'low','Careless':'low','other':'high'},
                          'items_revisits':{'Achiever':'low','Explorer':'low','Careless':'low','other':'low'},
                          'questions_revisits':{'Achiever':'low','Explorer':'low','Careless':'low','other':'low'}
                        }
        elif sec==1:
            play_feature_dic_new={'items_visited_total':{'Achiever':'low','Explorer':'high','Careless':'high','other':'low'},
                          'questions_right_ratio':{'Achiever':'high','Explorer':'high','Careless':'low','other':'low'},
                          'questions_visited_total':{'Achiever':'low','Explorer':'low','Careless':'low','other':'low'},
                          'questions_wrong_ratio':{'Achiever':'low','Explorer':'low','Careless':'high','other':'high'},
                          'time_read_time_total':{'Achiever':'low','Explorer':'high','Careless':'low','other':'low'},
                          'time_nav_time_total':{'Achiever':'low','Explorer':'low','Careless':'low','other':'low'},
                          'time_map/time_total':{'Achiever':'high','Explorer':'low','Careless':'low','other':'low'},
                          'reading_min':{'Achiever':'low','Explorer':'low','Careless':'high','other':'low'},
                          'reading_max':{'Achiever':'low','Explorer':'low','Careless':'low','other':'low'},
                          'item_visited_new':{'Achiever':'low','Explorer':'low','Careless':'low','other':'high'},
                          'items_revisits':{'Achiever':'low','Explorer':'low','Careless':'low','other':'low'},
                          'questions_revisits':{'Achiever':'low','Explorer':'low','Careless':'low','other':'low'}
                        }
        
        
        elif sec==3:
            play_feature_dic_new={'items_visited_total':{'Achiever':'low','Explorer':'low','Careless':'low','other':'low'},
                          'questions_right_ratio':{'Achiever':'high','Explorer':'high','Careless':'low','other':'low'},
                          'questions_visited_total':{'Achiever':'low','Explorer':'low','Careless':'low','other':'low'},
                          'questions_wrong_ratio':{'Achiever':'low','Explorer':'low','Careless':'high','other':'low'},
                          'time_read_time_total':{'Achiever':'low','Explorer':'low','Careless':'low','other':'low'},
                          'time_nav_time_total':{'Achiever':'low','Explorer':'high','Careless':'high','other':'low'},
                          'time_map/time_total':{'Achiever':'low','Explorer':'low','Careless':'low','other':'low'},
                          'reading_min':{'Achiever':'low','Explorer':'low','Careless':'low','other':'low'},
                          'reading_max':{'Achiever':'low','Explorer':'high','Careless':'low','other':'high'},
                          'item_visited_new':{'Achiever':'low','Explorer':'high','Careless':'high','other':'low'},
                          'items_revisits':{'Achiever':'low','Explorer':'high','Careless':'low','other':'low'},
                          'questions_revisits':{'Achiever':'high','Explorer':'low','Careless':'low','other':'low'}
                        }
            
        
        else:
            play_feature_dic_new={'items_visited_total':{'Achiever':'low','Explorer':'high','Careless':'high','other':'low'},
                          'questions_right_ratio':{'Achiever':'high','Explorer':'high','Careless':'low','other':'low'},
                          'questions_visited_total':{'Achiever':'low','Explorer':'low','Careless':'high','other':'low'},
                          'questions_wrong_ratio':{'Achiever':'low','Explorer':'low','Careless':'high','other':'high'},
                          'time_read_time_total':{'Achiever':'low','Explorer':'high','Careless':'high','other':'low'},
                          'time_nav_time_total':{'Achiever':'low','Explorer':'low','Careless':'low','other':'low'},
                          'time_map/time_total':{'Achiever':'high','Explorer':'low','Careless':'low','other':'low'},
                          'reading_min':{'Achiever':'low','Explorer':'low','Careless':'low','other':'low'},
                          'reading_max':{'Achiever':'low','Explorer':'low','Careless':'low','other':'low'},
                          'item_visited_new':{'Achiever':'low','Explorer':'low','Careless':'low','other':'high'},
                          'items_revisits':{'Achiever':'low','Explorer':'low','Careless':'low','other':'low'},
                          'questions_revisits':{'Achiever':'low','Explorer':'low','Careless':'low','other':'low'}
                        }
        
            

   
   # Manulay insert the weights
#     feature_weights={'items_visited_total':10,
#                  'questions_right_ratio':10,
#                  'questions_visited_total':5,
#                  'questions_wrong_ratio':10,
#                  'time_read_time_total':10,
#                  'time_nav_time_total':4,
#                  'time_map/time_total':1,
#                  'reading_min':4,
#                  'reading_max':4,
#                  'item_visited_new':3,
#                  'items_revisits':3,
#                  'questions_revisits':3,
#                  }
       
        
        
        
        
        
        my_path="/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/newExperiment_Trento/Sections/Sections_new_features/Labeled/congic"
        my_path=str(my_path+str(time.strftime("%d-%m-%Y")+str(time.strftime("-%I:%M:%S")))+'.csv')
        styles=['Achiever','Explorer','Careless','other']
        
        df=pd.DataFrame(play_feature_dic_new)
        df.to_csv(my_path) 
            #writer = df.to_csv(csv_file,index = False)
        #print("writing is Finished")
        
        return play_feature_dic_new