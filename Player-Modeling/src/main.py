'''
Created on May 11, 2017

@author: rezakhoshkangini
'''
import sys
import csv 
#import weka.core.jvm as jvm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from builtins import len
import glob
import os
from convertor import convert
#import ClassifierData
from ml_sub_proc import Sub_Machine
from pip._vendor.progress import counter
from Individual_Classification import Ind_Classification


def HisData(my_data):
    #for row in data:
    #    print(row)
    df=pd.DataFrame(my_data)
#     ReadingTime_total = df['x0_time_read_time_total']
#     NavigateTime_total = df['x0_time_nav_time_total']
#     VisitedItem_total = df['x0_items_visited_total']
#     Question_right_ratio = df['x0_questions_right_ratio']
    
    
    ReadingTime_total = df['time-read-per']
    NavigateTime_total = df['time-nav-perc']
    VisitedItem_total = df['visitd-Items']
    Question_right_ratio = df['Qution_right_perc']
    
    
    
    fig, axes = plt.subplots(nrows=4)

    axes[0].hist(ReadingTime_total, color='lightblue')
    axes[0].set(title='Total Reading Time')

    axes[1].hist(NavigateTime_total, color='salmon')
    axes[1].set(title='Total Navigatin Time')
    
    axes[2].hist(VisitedItem_total, color='green')
    axes[2].set(title='Vistited Items Total')
    
    axes[3].hist(Question_right_ratio, color='red')
    axes[3].set(title='Question_right_ratio total')

    #plot all the histofgram
    for ax in axes:
        ax.margins(0.05)
        ax.set_ylim(bottom=0)
    plt.show()
    
    return None  
    
def CategorizeData(my_data,cont):
    fd=pd.DataFrame(my_data)
    # HisData(my_data) 
    # print(data)
    
    # selecting the cutting points based on th distribution
    if cont==0:
        cut_points_Read = [0.38,0.5] ; cut_points_Nav=[0.3,0.35]; cut_points_QR= [0.65,0.75]; cut_points_visItem = [30,40]
    elif cont==1:
        cut_points_Read = [0.38,0.48] ; cut_points_Nav=[0.3,0.35]; cut_points_QR= [0.60,0.75]; cut_points_visItem = [55,75]
    elif cont==2:
        cut_points_Read = [0.38,0.45] ; cut_points_Nav=[0.25,0.32]; cut_points_QR= [0.60,0.75]; cut_points_visItem = [100,120]
    elif cont==3:
        cut_points_Read = [0.38,0.5] ; cut_points_Nav=[0.25,0.32]; cut_points_QR= [0.60,0.75]; cut_points_visItem = [130,160]
    else:
        cut_points_Read = [0.38,0.5] ; cut_points_Nav=[0.25,0.32]; cut_points_QR= [0.60,0.75]; cut_points_visItem = [180,210]

   
   
    labels = ["low","medium","high"]
    for i in range(4):
        col=my_data.iloc[:,i+2]
        #binds=pd.cut(col,3,right=True)
        #print(cut_points)
        #print(binds)
        #Define min and max values:
        minval = col.min()
        maxval = col.max()
        #cut_points=[(minval+maxval)/3,((minval+maxval)/3)*2]
        #breaking_points=minval+maxval/3,((minval+maxval)/3)*2
        if i==0 :
            #create list by adding min and max to cut_points
            break_points = [minval] + cut_points_Read + [maxval]
            if not labels:
                labels = range(len(cut_points_Read)+1)
        elif i==1:
            break_points = [minval] + cut_points_Nav + [maxval]
            if not labels:
                labels = range(len(cut_points_Nav)+1)
        elif i==2:   
            break_points = [minval] + cut_points_visItem + [maxval]
            if not labels:
                labels = range(len(cut_points_visItem)+1)
        else: 
            break_points = [minval] + cut_points_QR + [maxval]
            if not labels:
                labels = range(len(cut_points_QR)+1)
                
        #if no labels provided, use default labels 0 ... (n-1)
        #Binning using cut function of pandas
        #colBin = pd.cut(col,bins=break_points,labels=labels,include_lowest=True)
        colBin = pd.cut(col,3,labels=labels,include_lowest=True)
        if i==0:
            my_data["Read_time_Bin"]=colBin
        elif i==1:
            my_data["Nav_time_Bin"]=colBin
        elif i==2:       
            my_data["Vist_Item_Bin"]=colBin
        else:
            my_data["Qution_rightl_Bin"]=colBin
    #print (pd.value_counts(data["Read_time_Bin"], sort=False))
    df2=pd.DataFrame(my_data)
    print(df2)
    #selwcting columns for individual sections
    #categorical_data=df2.iloc[:,[1,8,9,10,11]]
    #selecting columns for comulative data
    categorical_data=df2.iloc[:,[1,7,8,9,10]]
    return categorical_data

def readfile():
    
    #############################
    path = '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/Time_Based/Five'
    df = pd.DataFrame()
    csvFiles = glob.glob(path + "/*.csv")
    listoflist={}
    for files in csvFiles:
        csvlist=pd.read_csv(files)
        listoflist[files]=csvlist
   
    
    #HisData(listoflist) # caculating the Histogram      
    
    return listoflist


def WritCsv(data,path):
    
    with open(path, "w") as csv_file:
        df=pd.DataFrame(data)
        writer = df.to_csv(csv_file,index = False)
        print("writing is Finished")
        
        
def Culstring_Players(My_data):
        #df=pd.DataFrame(data)
        #Defining Lables
        labels_Player_Style = ["Achiever","Explorer","CareLess","Lost"]
        BnData=My_data.iloc[:,1:5] # selecting categorical data from dataset
        df=pd.DataFrame(BnData)
        #Assigning players type
        My_data['Player_Type']='nan' # assignin nan as a defult type
        counter=0
        ThresholdValue=0.1
        while (counter<4):
            counter=counter+1
            if counter==1:
                My_data['Player_Type'] = np.where((df['Read_time_Bin'] =='low') & (df['Qution_rightl_Bin'] =='high'), 'Achiever', 
                                        np.where((df['Read_time_Bin'] =='high') & (df['Qution_rightl_Bin'] =='high'), 'Explorer',
                                                  np.where((df['Read_time_Bin'] =='high') & (df['Qution_rightl_Bin'] =='low'), 'Careless',
                                                            np.where((df['Read_time_Bin'] =='low') & (df['Qution_rightl_Bin'] =='low'), 'Lost',My_data['Player_Type']))))
               # dtfrm=pd.DataFrame(data=My_data)
               # print(My_data[My_data['Player_Type']=="nan"].shape[0]/My_data.shape[0])
                if My_data[My_data['Player_Type']=="nan"].shape[0]/My_data.shape[0] < ThresholdValue:
                    break
                
                
                
            elif counter==2:
                My_data['Player_Type'] = np.where((df['Nav_time_Bin'] =='low') & (df['Qution_rightl_Bin'] =='high'), 'Achiever', 
                                        np.where((df['Nav_time_Bin'] =='high') & (df['Qution_rightl_Bin'] =='high'), 'Explorer',
                                                  np.where((df['Nav_time_Bin'] =='high') & (df['Qution_rightl_Bin'] =='low'), 'Careless',
                                                            np.where((df['Nav_time_Bin'] =='low') & (df['Qution_rightl_Bin'] =='low'), 'Lost',My_data['Player_Type']))))
                #print(My_data[My_data['Player_Type']=="nan"].shape[0]/My_data.shape[0])
                #print(My_data['Player_Type'].value_counts(normalize=True).loc['nan'])
                if My_data[My_data['Player_Type']=="nan"].shape[0]/My_data.shape[0] < ThresholdValue:
                    break
                
            elif counter==3:
                My_data['Player_Type'] = np.where((df['Vist_Item_Bin'] =='low') & (df['Qution_rightl_Bin'] =='high'), 'Achiever', 
                                        np.where((df['Vist_Item_Bin'] =='high') & (df['Qution_rightl_Bin'] =='high'), 'Explorer',
                                                  np.where((df['Vist_Item_Bin'] =='high') & (df['Qution_rightl_Bin'] =='low'), 'Careless',
                                                            np.where((df['Vist_Item_Bin'] =='low') & (df['Qution_rightl_Bin'] =='low'), 'Lost',My_data['Player_Type']))))
               # print(My_data[My_data['Player_Type']=="nan"].shape[0]/My_data.shape[0])
                if My_data[My_data['Player_Type']=="nan"].shape[0]/My_data.shape[0] < ThresholdValue:
                    break
                
            elif counter==4:
                My_data['Player_Type'] = np.where((df['Vist_Item_Bin'] =='low') & (df['Qution_rightl_Bin'] =='medium'), 'Achiever', 
                                        np.where((df['Vist_Item_Bin'] =='high') & (df['Qution_rightl_Bin'] =='medium'), 'Explorer',
                                                  np.where((df['Vist_Item_Bin'] =='medium') & (df['Qution_rightl_Bin'] =='low'), 'Careless',
                                                            np.where((df['Vist_Item_Bin'] =='low') & (df['Qution_rightl_Bin'] =='low'), 'Lost',My_data['Player_Type']))))
                #print(My_data[My_data['Player_Type']=="nan"].shape[0]/My_data.shape[0])
                if My_data[My_data['Player_Type']=="nan"].shape[0]/My_data.shape[0] < ThresholdValue:
                    break
                
            
                
        print('Player Style Assigning is done')
        return My_data
            
        
def Difrentiate_Labled_Data(LstData):

        
    for key in LstData.keys():
        if key==0:
            list0=LstData[key]
            print(list0)
        elif key==1:
            list1=LstData[key]
        elif key==2:
            list2=LstData[key]   
        elif key==3:
            list3=LstData[key]   
        elif key==4:
            list4=LstData[key]
        else:
            list5=LstData[key]   
         
    Users_name={}
    TmpList=[]
    
    for x in range(0,113):
        Users_name["User{0}".format(x)]=[]
    counter=0     
    for key in Users_name.keys():
        Users_name.setdefault(key,[]).append(list0.iloc[counter,:])
        Users_name.setdefault(key,[]).append(list1.iloc[counter,:])
        Users_name.setdefault(key,[]).append(list2.iloc[counter,:])
        Users_name.setdefault(key,[]).append(list3.iloc[counter,:])
        Users_name.setdefault(key,[]).append(list4.iloc[counter,:])
       # Users_name.setdefault(key,[]).append(list5.iloc[counter,:])
        counter=counter+1
    print(Users_name.keys())
    
    i=1
    for key in Users_name.keys():
        path="/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/NewCSV/BindedData/IndUsers/CsV/playerLbl_comu_"+str(i)+".csv"
        playerData=Users_name[key]
        WritCsv(playerData,path)
        i=i+1
# 
#   
       
    return None
#  
 
# def class_data():
#     data_dir = "/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/NewCSV/BindedData/"
#     loader = Loader(classname="weka.core.converters.ArffLoader")
#     data = loader.load_file(data_dir + "Section0.arff")
#     data.class_is_last()
#     print(data)
     
        
def main():
    print("start to clean data")
    # load data file
    Csv_Dics=readfile()
    print(Csv_Dics.keys())
    Lists_Labeled_data={}
    i=0
    for key in Csv_Dics.keys():
    # data["Read_time_Bin"]=CategorizeData(data['x0_time_read_time_total'], cut_points, labels)
        data_binded=CategorizeData(Csv_Dics[key],0)
        #data_binded=CategorizeData(data)
    #Clustring
        data_labaled=Culstring_Players(data_binded)
        TmpContiner=pd.DataFrame(data_labaled)
        Lists_Labeled_data[i]=TmpContiner# adding all the labled data into a list
    #writing bindeded data to CSV file
       # path="/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/NewCSV/BindedData/Comulative_Data/Com0-"+str(i+1)+"_Labeled.csv"
        path="/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/Time_Based/Five/Binded/Five"+str(i+1)+"_Labeled.csv"
        WritCsv(data_labaled,path)
        i=i+1
    #
   
   #calling classification class 
    Sub_Machine()
    
    #Difrentiate_Labled_Data(Lists_Labeled_data)    
    #converting csv file into arff
    Converted_Data_arff = convert()
    reslut=Ind_Classification()

if __name__ == '__main__':
   try:
        
        main()
   except Exception as ex:
        print(ex)

   print("Process is Finished")
   print("Clustering is finished")
   
   