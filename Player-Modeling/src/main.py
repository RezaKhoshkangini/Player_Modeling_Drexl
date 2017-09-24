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
import ntpath
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
    Question_right_ratio = df['Qution_right_perc']
    VisitedItem_total = df['visitd-Items']
   
    
    
    
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
    for i in range(7):
        col=my_data.iloc[:,i+2]
        if len(set(col))!=1:
            minval = col.min()
            maxval = col.max()
            avgval= col.mean()
            cut_points_General=[(minval+avgval)/2,(maxval+avgval)/2] 
            break_points = [minval] + cut_points_General + [maxval]
            colBin = pd.cut(col,3,labels=labels,include_lowest=True)
        else:
            if col[1]<0.5:
                colBin = pd.cut(col,3,labels=labels,include_lowest=True)
                colBin[:]='low'
            elif col[1]>=0.5:
                colBin = pd.cut(col,3,labels=labels,include_lowest=True)
                colBin[:]='high'       
#             if i==0 :
#                 #create list by adding min and max to cut_points
#                 break_points = [minval] + cut_points_Read + [maxval]
#                 if not labels:
#                     labels = range(len(cut_points_Read)+1)
#             elif i==1:
#                 break_points = [minval] + cut_points_Nav + [maxval]
#                 if not labels:
#                     labels = range(len(cut_points_Nav)+1)
#             elif i==2:   
#                 break_points = [minval] + cut_points_visItem + [maxval]
#                 if not labels:
#                     labels = range(len(cut_points_visItem)+1)
#             else: 
#                 break_points = [minval] + cut_points_QR + [maxval]
#                 if not labels:
#                     labels = range(len(cut_points_QR)+1)
                
       
        
        #if no labels provided, use default labels 0 ... (n-1)
        #Binning using cut function of pandas
        #colBin = pd.cut(col,bins=break_points,labels=labels,include_lowest=True)
            
            
            
        if i==0:
            my_data["time_nav_time_total"]=colBin
        elif i==1:
            my_data["time_read_time_total"]=colBin
        elif i==2:       
            my_data["questions_right_ratio"]=colBin
        elif i==3:
            my_data["items_visited_total"]=colBin
        elif i==4:
            my_data["time_map/time_total"]=colBin
        elif i==5:
            my_data["questions_visited_total"]=colBin
        elif i==6:
            my_data["questions_wrong_ratio"]=colBin
            
    #print (pd.value_counts(data["Read_time_Bin"], sort=False))
    df2=pd.DataFrame(my_data)
    print(df2)
    #selwcting columns for individual sections
    #categorical_data=df2.iloc[:,[1,8,9,10,11]]
    #selecting columns for comulative data
    categorical_data=df2.iloc[:,[1,9,10,11,12,13,14,15]]
    return categorical_data

def readfile():
    
    #############################
   # path = '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/Time_Based/Two/cleaned'
   # path ='/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/newExperiment_Trento/Sections/Sections_new_features/CSV'
    path='/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/newExperiment_Trento/Sections/Sections_new_features/CSV_Outlier_Excluded'
    df = pd.DataFrame()
    csvFiles = glob.glob(path + "/*.csv")
    listoflist={}
    for files in csvFiles:
        csvlist=pd.read_csv(files)
        listoflist[files]=csvlist
   
    
    #HisData(listoflist) # caculating the Histogram      
    
    return  listoflist


def WritCsv(data,path):
    
    with open(path, "w") as csv_file:
        df=pd.DataFrame(data)
        writer = df.to_csv(csv_file,index = False)
        print("writing is Finished")
        
        
def Culstring_Players(My_data):
        
        # creating dictionary of play style with their characteristics
        play_feature_dic={'items_visited_total':{'Achiever':'low','Explorer':'high','Careless':'low','other':'low'},
                        'questions_right_ratio':{'Achiever':'high','Explorer':'high','Careless':'low','other':'low'},
                        'questions_visited_total':{'Achiever':'high','Explorer':'low','Careless':'low','other':'low'},
                        'questions_wrong_ratio':{'Achiever':'low','Explorer':'low','Careless':'high','other':'high'},
                        'time_read_time_total':{'Achiever':'high','Explorer':'low','Careless':'low','other':'low'},
                        'time_nav_time_total':{'Achiever':'high','Explorer':'low','Careless':'low','other':'low'},
                        'time_map/time_total':{'Achiever':'high','Explorer':'high','Careless':'low','other':'low'}}
        
        play_style_dic={'Achiever':{'items_visited_total':'low','questions_right_ratio':'high','questions_visited_total':'high',
                                    'questions_wrong_ratio':'low','time_read_time_total':'high','time_nav_time_total':'low','time_map/time_total':'high'},
                        'Explorer':{'items_visited_total':'high','questions_right_ratio':'high','questions_visited_total':'low',
                                    'questions_wrong_ratio':'low','time_read_time_total':'low','time_nav_time_total':'high','time_map/time_total':'high'},
                        'Careless':{'items_visited_total':'low','questions_right_ratio':'low','questions_visited_total':'low',
                                    'questions_wrong_ratio':'high','time_read_time_total':'low','time_nav_time_total':'low','time_map/time_total':'low'},
                        'other':{'items_visited_total':'low','questions_right_ratio':'low','questions_visited_total':'low',
                                    'questions_wrong_ratio':'high','time_read_time_total':'low','time_nav_time_total':'high','time_map/time_total':'low'}}
        
        
        
        
        
        #df=pd.DataFrame(data)
        #Defining Lables
        labels_Player_Style = ["Achiever","Explorer","CareLess","Lost"]
    
      #  list_features=['items_visited_total','time_map/time_total','questions_visited_total','time_read_time_total','questions_right_ratio','time_nav_time_total'] # main order info gain
        list_features=['items_visited_total','questions_right_ratio','questions_visited_total','questions_wrong_ratio','time_read_time_total','time_nav_time_total','time_map/time_total'] # inf gain
      #  list_features=['items_visited_total','time_map/time_total','questions_visited_total','questions_wrong_ratio','time_read_time_total','time_nav_time_total','questions_right_ratio'] # inf gain
                          
 
        BnData=My_data.iloc[:,1:8] # selecting categorical data from dataset
        df=pd.DataFrame(BnData)
        #Assigning players type
        My_data['Player_Type']='other' # assignin other as a defult type
        counter=0
        ThresholdValue=0.1
        while (counter<len(list_features)+1):
            counter=counter+1
            print(My_data)
            ########### 3 Features to compare #############^    
            if counter==1:
               
                ###### new code with new dictionary 
                
                
                #########
                
                My_data['Player_Type'] = np.where((df[list_features[0]] =='low') & (df[list_features[1]] =='high'), 'Achiever',  # 
                                        np.where((df[list_features[0]] =='high') & (df[list_features[1]] =='high') ,'Explorer',
                                                  np.where((df[list_features[0]] =='low') & (df[list_features[1]] =='low') , 'Careless',
                                                            np.where((df[list_features[0]] =='low') & (df[list_features[1]] =='high'), 'other',My_data['Player_Type']))))
               
                print(My_data)
                if My_data[My_data['Player_Type']=="other"].shape[0]/My_data.shape[0] < ThresholdValue:
                    break
                
            elif counter==2:
                My_data['Player_Type'] = np.where((df[list_features[0]] =='medium') & (df[list_features[2]] =='high')  & (My_data['Player_Type']=='other'), 'Achiever', 
                                        np.where((df[list_features[0]] =='medium') & (df[list_features[2]] =='low') & (My_data['Player_Type']=='other'), 'Explorer', My_data['Player_Type']))
                print(My_data)
                if My_data[My_data['Player_Type']=="other"].shape[0]/My_data.shape[0] < ThresholdValue:
                    break
            
            elif counter==3:
                My_data['Player_Type'] = np.where((df[list_features[2]] =='medium') & (df[list_features[3]] =='high') &(My_data['Player_Type']=='other'), 'Careless', 
                                        np.where((df[list_features[2]] =='medium') & (df[list_features[3]] =='low')& (My_data['Player_Type']=='other'), 'Explorer', My_data['Player_Type']))
                print(My_data)
                if My_data[My_data['Player_Type']=="other"].shape[0]/My_data.shape[0] < ThresholdValue:
                    break                                                                                                                                                                           
            elif counter==4:
                My_data['Player_Type'] = np.where((df[list_features[3]] =='medium') & (df[list_features[4]] =='high') &(My_data['Player_Type']=='other'), 'Achiever', 
                                        np.where((df[list_features[3]] =='medium') & (df[list_features[4]] =='low')& (My_data['Player_Type']=='other'), 'Explorer', My_data['Player_Type']))   
                print(My_data)
                if My_data[My_data['Player_Type']=="other"].shape[0]/My_data.shape[0] < ThresholdValue:
                    break
            elif counter==5:
                My_data['Player_Type'] = np.where((df[list_features[4]] =='medium') & (df[list_features[5]] =='high') & (My_data['Player_Type']=='other'), 'Explorer', 
                                        np.where( (df[list_features[4]] =='medium') & (df[list_features[5]] =='low')&(My_data['Player_Type']=='other'), 'Achiever', My_data['Player_Type']))       
                print(My_data)
                if My_data[My_data['Player_Type']=="other"].shape[0]/My_data.shape[0] < ThresholdValue:
                    break
            elif counter==6:
                My_data['Player_Type'] = np.where((df[list_features[5]] =='medium') & (df[list_features[6]] =='high') &(My_data['Player_Type']=='other'), 'Explorer', 
                                        np.where((df[list_features[5]] =='medium') & (df[list_features[6]] =='low') & (My_data['Player_Type']=='other'), 'Careless', My_data['Player_Type']))  
            
                print(My_data)             
                if My_data[My_data['Player_Type']=="other"].shape[0]/My_data.shape[0] < ThresholdValue:
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
    
    for x in range(0,55):
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
        path="/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/newExperiment_Trento/New_Individual_users/CSV/"+str(i)+".csv"
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
def path_leaf(path):
    head, tail = ntpath.split(path)
    
    return tail or ntpath.basename(head)  

def extract_type(my_sample,play_feature_dic_new,feature_weights):
   # print (feature_weights)
    my_vote = {"Achiever":0,"Explorer":0,"Careless":0,"other":0} 
    for key,item in play_feature_dic_new.items():
       # print(key)
        if my_sample[key]=='medium':
            # there is no effect with this medium vaue 
            #print('this feature is medium')
            pass
        else:
            feature_weight=feature_weights[key]
            for key1 in item.keys():
                if (item[key1]==my_sample[key]):
                    my_vote[key1]+=feature_weight
                else:
                    my_vote[key1]-=feature_weight
                    
           # print(my_vote)               
                 
    return(max(my_vote,key=my_vote.get))           #returns only labels
   # return(sorted(my_vote,key=my_vote.get, reverse=True))
    
    
    
    
def Clustering_new(My_binded_data,my_section):
    #defining the styles and he features 
    play_feature_dic_new={'items_visited_total':{'Achiever':'low','Explorer':'high','Careless':'low','other':'low'},
                        'questions_right_ratio':{'Achiever':'high','Explorer':'high','Careless':'low','other':'low'},
                        'questions_visited_total':{'Achiever':'high','Explorer':'low','Careless':'low','other':'low'},
                        'questions_wrong_ratio':{'Achiever':'low','Explorer':'low','Careless':'high','other':'high'},
                        'time_read_time_total':{'Achiever':'high','Explorer':'low','Careless':'low','other':'low'},
                        'time_nav_time_total':{'Achiever':'high','Explorer':'low','Careless':'low','other':'high'},
                        'time_map/time_total':{'Achiever':'high','Explorer':'high','Careless':'low','other':'low'}}
    
    # list of features in orders for overall fix for all section
  #  list_features_new=['items_visited_total','questions_right_ratio','questions_visited_total','questions_wrong_ratio','time_read_time_total','time_nav_time_total','time_map/time_total'] # inf gain
    if my_section==0:
            list_features_new=['questions_visited_total','questions_right_ratio','time_read_time_total','items_visited_total','questions_wrong_ratio','time_map/time_total','time_nav_time_total'] # inf gain
    elif my_section==1:
            list_features_new=['items_visited_total','time_map/time_total','questions_visited_total','questions_wrong_ratio','questions_right_ratio','time_read_time_total','time_nav_time_total'] # inf gain
    elif my_section==2:
            list_features_new=['items_visited_total','time_map/time_total','questions_visited_total','questions_wrong_ratio','questions_right_ratio','time_read_time_total','time_nav_time_total'] # inf gain
    else:    #for section 4
            list_features_new=['questions_wrong_ratio','questions_right_ratio','time_nav_time_total','time_read_time_total','questions_visited_total','time_map/time_total','items_visited_total'] # inf gain

    
    # weight of features 
#     feature_weights={'items_visited_total':len(list_features_new)-list_features_new.index('items_visited_total'),
#                'questions_right_ratio':len(list_features_new)-list_features_new.index('questions_right_ratio'),
#                'questions_visited_total':len(list_features_new)-list_features_new.index('questions_visited_total'),
#                'questions_wrong_ratio':len(list_features_new)-list_features_new.index('questions_wrong_ratio'),
#                'time_read_time_total':len(list_features_new)-list_features_new.index('time_read_time_total'),
#                'time_nav_time_total':len(list_features_new)-list_features_new.index('time_nav_time_total'),
#                'time_map/time_total':len(list_features_new)-list_features_new.index('time_map/time_total')}
    
    feature_weights={'items_visited_total':7,
               'questions_right_ratio':6,
               'questions_visited_total':5,
               'questions_wrong_ratio':6,
               'time_read_time_total':4,
               'time_nav_time_total':4,
               'time_map/time_total':1}
    
    
    
   # print(My_binded_data)
    my_result=[]
    for indx in range(0,len(My_binded_data)):
        #print(My_binded_data)
        
        my_result.append(extract_type(My_binded_data.iloc[indx,1:8],play_feature_dic_new,feature_weights))
        
    My_binded_data['Player_Type']=my_result
    print(My_binded_data)
    
    return My_binded_data
    
#     csvfile = '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/Cluster_Validation/Sectoin'+str(my_section)+'.csv'
# 
#     #Assuming res is a flat list
#     with open(csvfile, "w") as output:
#         writer = csv.writer(output, lineterminator='\n')
#         for val in My_binded_data:
#             writer.writerow([val])
    
   
    
    
            
def main():
    print("start to clean data")
    # load data file
    Csv_Dics=readfile() 
    #print(Csv_Dics.keys())
    Lists_Labeled_data={}
    i=0
    for key in Csv_Dics.keys():
    # data["Read_time_Bin"]=CategorizeData(data['x0_time_read_time_total'], cut_points, labels)
        print(key)
        data_binded=CategorizeData(Csv_Dics[key],0)
        nameOfthefile=path_leaf(key)
        print(nameOfthefile)
        #data_binded=CategorizeData(data)
    #Clustring
        data_labaled=Clustering_new(data_binded,i)
     #   data_labaled=Culstring_Players(data_binded)
        TmpContiner=pd.DataFrame(data_labaled)
        Lists_Labeled_data[i]=TmpContiner# adding all the labled data into a list
    #writing bindeded data to CSV file
       
        path="/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/newExperiment_Trento/Sections/Sections_new_features/Labeled/L"+nameOfthefile
        WritCsv(data_labaled,path)
        i=i+1
    #
   #calling classification class 
   # Sub_Machine()
    Difrentiate_Labled_Data(Lists_Labeled_data)    
    #converting csv file into arff
    Converted_Data_arff = convert()
   # reslut=Ind_Classification()

if __name__ == '__main__':
   try:
        
        main()
   except Exception as ex:
        print(ex)

   print("Process is Finished")
   print("Clustering is finished")
   
   