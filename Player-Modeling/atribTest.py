# Feature Importance
# Recursive Feature Elimination
from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import glob
from pandas.core.frame import DataFrame

path='/Users/rezakhoshkangini/Documents/Drexel_Documents/Work/Mat-Code/newExperiment_Trento/Sections/Sections_new_features/TestforOrders/csv_for_Atribute_selection'
csvFiles = glob.glob(path + "/*.csv")
listoflist={}
for files in csvFiles:
    csvlist=pd.read_csv(files)
    listoflist[files]=csvlist
    #HisData(listoflist) # caculating the Histogram      
 

array=csvlist.values
#array = dataframe.values
X = array[:,0:12]
Y = array[:,12]
# feature extraction
model = LogisticRegression()
#model=GainRatioAttributeEval()
rfe = RFE(model, 3)
fit = rfe.fit(X, Y)
#print("Num Features: %d",  fit.n_features_)
#print("Selected Features: %s",  fit.support_)
#print("Feature Ranking: %s",  fit.ranking_)

model = ExtraTreesClassifier()
model.fit(X, Y)
# display the relative importance of each attribute
print(model.feature_importances_)
my_weight=model.feature_importances_
i, = np.where( my_weight)

return my_weight

