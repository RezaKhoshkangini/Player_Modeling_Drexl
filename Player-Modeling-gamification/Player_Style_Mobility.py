'''
Created on Jul 3, 2017

@author: rezakhoshkangini
'''

import sys
import csv 
#import weka.core.jvm as jvm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from builtins import len, list
import glob
import os
from itertools import chain
from pandas.core.frame import DataFrame
from numpy.distutils.fcompiler import none
from matplotlib.pyplot import axis
from unittest.mock import inplace





def readfile():
    
    #############################
    #path = csv.reader(open('/Users/rezakhoshkangini/Documents/CH/Player_Modeling/All/All.csv'))
    path = '/Users/rezakhoshkangini/Documents/CH/Player_Modeling/All'
    
    csvFiles = glob.glob(path + "/*.csv")
    listoflist={}
    for files in csvFiles:
        csvlist=pd.read_csv(files)
        listoflist[files]=csvlist
   
    
    #HisData(listoflist) # caculating the Histogram      
    df = pd.DataFrame(csvlist)
    return df
    
 
def Dif_Players(Mfile):
    #dividing the whole players into different dictionary based on their ID
    dict_of_players = {k: v for k, v in Mfile.groupby('PLAYER_ID')}
   
    return dict_of_players

def CalculateRatio(playerData,Ban):
    
    if Ban==0:
        playerData.drop(playerData.columns[[0,1,3,5,7,10,11,12,14,15,18]],axis=1,inplace=True)
        Totaltrips=playerData.sum().sum()
        resultSum=playerData.sum(axis=0)
    elif Ban==1:
        SumCol=pd.DataFrame(playerData)
        resultSum=SumCol.iloc[:,0:].apply(lambda x: x / x.sum())
   # print(PrcentageMode)
  
    
    return resultSum
    
    
    

    
def main():
    Csv_Dics=readfile()
    listofPlayers=Dif_Players(Csv_Dics)
    RatioPlayers={}
    DicPercentMode={}
    for key in listofPlayers.keys():
        RatioPlayers["Player{0}".format(key)]=CalculateRatio(listofPlayers[key],0)
        #RatioPlayers["Player{0}".format(key)]=[]
    for key in RatioPlayers.keys():
        DicPercentMode["Player{0}".format(key)]=CalculateRatio(RatioPlayers[key],1)
        
    print(RatioPlayers.keys())    
        
        
if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print(ex)
    print("Process is Finished")
    print("Clustering is finished")
    
    
    
    

#     LisTmp=['PLAYER_ID','BikeSharing_Km','BikeSharing_Trips','Bike_Km',
#             'Bike_Trips','Bus_Km','Bus_Trips','Car_Km','Car_Trips','NoCar_Trips','PandR_Trips',          
#             'Recommendations','Train_Km','Train_Trips','Transit_Trips','Walk_Km','Walk_Trips',            
#             'ZeroImpact_Trips','green leaves']
#     
#    
    