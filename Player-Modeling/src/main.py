'''
Created on May 11, 2017

@author: Reza Khoshkangini PhD Student DAS Unit FBK and Univesity of Padova
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
from Order_Extraction import Orderextraction
from audioop import reverse
from List_to_CSV import wrt_to_csv
from Player_Sepration import WritCsv
from Configuration import config 
 


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
    MydataSample=[]
    MySample=pd.DataFrame(MydataSample)
    fd=pd.DataFrame(my_data)
    # HisData(my_data) 
    # print(data)
    
    MySample=my_data.head(0)
    MySample["Id_Name"]= my_data.iloc[:,0] 
   
    labels = ["low","medium","high"]
    for i in range(len(my_data.columns)-1):
        print(my_data.iloc[:,i+1])
        col=my_data.iloc[:,i+1]
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
#             
        #Minserting the label colun to dtaframe    
        MySample.iloc[:,i+1]=colBin    
        
        
         
            
    #print (pd.value_counts(data["Read_time_Bin"], sort=False))
   #selwcting columns for individual sections
   
    #selecting columns for comulative data
   # categorical_data=df2.iloc[:,[1,14,15,16,17,18,19,20,21,22,23,24,25]]
    return MySample

def readfile():
    
    #############################
   # path = '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/Time_Based/Two/cleaned'
   # path ='/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/newExperiment_Trento/Sections/Sections_new_features/CSV'
    path='/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/newExperiment_Trento/Sections/Sections_new_features/CSV_Outlier_Exclude_12Feature'
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
    #print(Users_name.keys())
    
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
 
def path_leaf(path):
    head, tail = ntpath.split(path)
    
    return tail or ntpath.basename(head)  


def extract_type(my_sample,play_feature_dic_new,feature_orders):
    # print (feature_weights)
    my_vote = {"Achiever":0,"Explorer":0,"Careless":0,"other":0} 
    
    my_lst_key=["Id_Name","Achiever","Explorer","Careless","other"]
    my_vote_id = {"Id_Name":my_sample[0],"Achiever":[],"Explorer":[],"Careless":[],"other":[]} 
    my_vote_id_con = {"Id_Name":my_sample[0],"Achiever":0,"Achiever_Conf":0,"Explorer":0,"Explorer_Conf":0,"Careless":0,"Careless_Conf":0,"other":0,"other_Conf":0}
    for key,item in play_feature_dic_new.items():
        # print(key)
        if my_sample[key]=='medium':
            # there is no effect with this medium vaue 
            #print('this feature is medium')
            pass
        else:
            feature_weight=feature_orders[key]
            my_ordertest={}
            my_ordertest=sorted(feature_orders.values(),reverse=True)
            
            feature_order=my_ordertest.index(feature_orders[key])
            feature_weight=feature_orders[key]
            #feature_weight=feature_weights[key]
            for key1 in item.keys():
                if (item[key1]==my_sample[key]):
                    my_vote[key1]+=feature_weight*(1/(feature_order+1))
                else:
                    my_vote[key1]-=feature_weight*(1/(feature_order+1))
                    
                    
            #print(my_vote)               
    total_weight=sum(feature_orders.values())
    for cokey in my_vote.keys():
        my_confidence=round((my_vote[cokey]/total_weight)*100)  
        my_vote_id_con.update(my_vote)  
        my_vote_id_con[cokey+str('_Conf')]=my_confidence
        
        #my_vote_id[cokey].append(my_vote[cokey])
        #my_vote_id[cokey].append(my_confidence)
        
        
    if len(set(my_vote.values()))==2:
        print('they are similar')
        print(my_vote)              
    #return(max(my_vote,key=my_vote.get))           #returns only labels
    return(sorted(my_vote,key=my_vote.get, reverse=True)[0],my_vote_id_con[sorted(my_vote,key=my_vote.get, reverse=True)[0]+str('_Conf')]
,my_vote_id_con)
   


def cal_weight(my_section,nameOfthefile):  
    
   # atribTest(my_section)
    my_weight_orders=Orderextraction(my_section,nameOfthefile)
    
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
    
    
    return  my_weight_orders
    
    
def Clustering_new(My_binded_data,my_section,nameOfthefile):
    #defining the styles and he features 
    
    
  
    feature_order=cal_weight(my_section,nameOfthefile)
    # print(My_binded_data)
    my_result=[]
    my_confid=[]
    my_result_confidence=[]
    for indx in range(0,len(My_binded_data)):
        #print(My_binded_data)
        play_feature_dic_new=config()
        selected_style,confid,styles_confidecs=extract_type(My_binded_data.iloc[indx,0:len(My_binded_data.columns)],play_feature_dic_new,feature_order)
        my_result.append(selected_style)
        my_confid.append(confid)
        my_result_confidence.append(styles_confidecs)
        
    My_binded_data['Player_Type']=my_result
    My_binded_data['Confidence']=my_confid
   
    print(My_binded_data)
  
    
    return My_binded_data,my_result_confidence
    
    
            
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
        path="/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/newExperiment_Trento/Sections/Sections_new_features/Labeled/"
        #data_binded=CategorizeData(data)
    #Clustring
        data_labaled,data_confid=Clustering_new(data_binded,i,nameOfthefile)
        WritCsv(data_confid,path+str('Conf_'+nameOfthefile))
     #   data_labaled=Culstring_Players(data_binded)
        TmpContiner=pd.DataFrame(data_labaled)
        Lists_Labeled_data[i]=TmpContiner# adding all the labled data into a list
    #writing bindeded data to CSV file
       
        
        WritCsv(data_labaled,path+str('Result_'+nameOfthefile))
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
   
   