'''
Created on Sep 26, 2017

@author: rezakhoshkangini
'''
import subprocess, os
from subprocess import call
from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_boston
from sklearn.linear_model import (LinearRegression, Ridge,Lasso, RandomizedLasso)
from sklearn.feature_selection import RFE, f_regression,SelectPercentile, f_classif
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn import datasets, svm

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import glob
from pandas.core.frame import DataFrame
from pandas.core.internals import items_overlap_with_suffix
import ntpath
from sklearn.feature_selection import SelectKBest, f_classif,chi2,SelectFromModel
from sklearn.svm import LinearSVC
# class Class_Order_Extration:
#     '''
#     classdocs
#     '''
# 
# 
#     def __init__(self,my_section):
#        # self.__init__(my_section)
#         self.orderextraction=my_section
#  
def SVMmethod(arrayb,colname):
    
    X1 = arrayb[:,0:12]
    Y1 = arrayb[:,12]
    X1.shape
    X1_indices = np.arange(X1.shape[-1])
    selector = SelectPercentile(f_classif, percentile=10)
    clf = svm.SVC(kernel='linear')
    clf.fit(X1, Y1)

    svm_weights = (clf.coef_ ** 2).sum(axis=0)
    svm_weights /= svm_weights.max()
    
    my_list=svm_weights.tolist()
    my_weight_dic=dict(zip(colname,my_list))
    
#     plt.figure()
#     plt.bar(X1_indices - .25, svm_weights[X1_indices], label='SVM weight',color='navy', edgecolor='black')
#     plt.xticks(range(X1.shape[1]), X1_indices)
#     plt.xlim([-1, X1.shape[1]])
#     plt.show()
    
    #sklearn.feature_selection.mutual_info_regression(X1, Y1, discrete_features=’auto’, n_neighbors=3, copy=True, random_state=None)
    
    return my_weight_dic
 
def TreeForest(array,colname):
    X = array[:,0:12]
    Y = array[:,12]
            # feature extraction
            #  model = LogisticRegression()
            #model=GainRatioAttributeEval()
            #  rfe = RFE(model, 3)
            #  fit = rfe.fit(X, Y)
            #print("Num Features: %d",  fit.n_features_)
            #print("Selected Features: %s",  fit.support_)
            #print("Feature Ranking: %s",  fit.ranking_)

    model = ExtraTreesClassifier()
    model.fit(X, Y)
            
            
            # display the relative importance of each attribute
    print(model.feature_importances_)
    my_weight=model.feature_importances_
    std = np.std([tree.feature_importances_ for tree in model.estimators_],axis=0)
    indices = np.argsort(my_weight)[::-1]
           
    my_list=my_weight.tolist()
    my_weight_dic=dict(zip(colname,my_list))
            
    # Plot the feature importances of the forest
#     plt.figure()
#     plt.title("Feature importances")
#     plt.bar(range(X.shape[1]), my_weight[indices],
#     color="r", yerr=std[indices], align="center")
#     plt.xticks(range(X.shape[1]), indices)
#     plt.xlim([-1, X.shape[1]])
#     plt.show()
            
            
    return  my_weight_dic
 
       
def my_path_leaf(path):
    head, tail = ntpath.split(path)
    
    return tail or ntpath.basename(head) 
        
def Orderextraction(my_section,nameOfthefile):
        
    print('hello reza')
    path='/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/newExperiment_Trento/Sections/Sections_new_features/TestforOrders/csv_for_Atribute_selection'
    csvFiles = glob.glob(path + "/*.csv")
    listoflist={}
    unique_headers = set()
    for files in csvFiles:
        csvlist=pd.read_csv(files)
        listoflist[files]=csvlist
          
        
    for key in listoflist.keys():
        this_key=my_path_leaf(key)
        if this_key==nameOfthefile:
            my_array=listoflist[key]        
            colname=my_array.columns.tolist()
            colname=colname[:-1]
            array=my_array.values
            my_weight_dic=SVMmethod(array,colname)
          #  my_weight_dic=TreeForest(array,colname)
         #array = dataframe.values
            
            return my_weight_dic
        
        
        
        
        
        
        
#         for counter in range(0,4):
#             file_out = open("/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/newExperiment_Trento/Sections/Sections_new_features/TestforOrders/Arff_for_AttributeSelection/out"+str(counter+1)+".txt", "w")
#             cmd =['java', '-Xmx1024M', '-cp', '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Python_Code/weka.jar', 'weka.attributeSelection.GainRatioAttributeEval', '-s' + " weka.attributeSelection.Ranker -T -1.7976931348623157E308 -N, -1" + '-i', '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/newExperiment_Trento/Sections/Sections_new_features/TestforOrders/Arff_for_AttributeSelection/section'+str(counter)+'.arff']
#             call(['java', '-Xmx1024M', '-cp', '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Python_Code/weka.jar', 'weka.attributeSelection.GainRatioAttributeEval', '-s' , + " weka.attributeSelection.Ranker -T -1.7976931348623157E308 -1 " + , '-i' , '/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/newExperiment_Trento/Sections/Sections_new_features/TestforOrders/Arff_for_AttributeSelection/section1.arff'], stdout=file_out)


 