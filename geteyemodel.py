# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 11:15:18 2018

@author: Administrator
"""

from sklearn import svm

from sklearn.datasets import load_svmlight_file
import pandas as pd  
from sklearn.ensemble import RandomForestClassifier  
from sklearn import metrics  
  #引入评价指标
from sklearn import cross_validation

from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix    #计算混淆矩阵

from sklearn.metrics import matthews_corrcoef #计算MCC

from sklearn.metrics import  roc_auc_score  #计算MCC 只对二分类可以计算

from sklearn.metrics import  accuracy_score  #计算ACC

from sklearn.externals import joblib

#导入训练数据，这里的训练数据使用Under-Sampling处理过的  
fr_n="eye_train.txt"

X,y=load_svmlight_file(fr_n)


# Run classifier  

print("===cross validation===")

clf = svm.SVC(kernel='rbf')

#scores=cross_validation.cross_val_score(clf,X,y,cv=5,scoring="accuracy")

#print(scores,scores.mean())



print("===performance on TEST===")

# Split the data into a training set and a test set; 分为训练集 检验集

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

clf= svm.SVC(kernel='rbf')

clf.fit(X_train,y_train)

y_pred =clf.predict(X_test)

# 计算混淆 矩阵 Compute confusion matrix

cm = confusion_matrix(y_test, y_pred)

print(cm)
Precision = (float)(cm[0][0]/(cm[1][0]+cm[0][0]))
Recall = (float)(cm[0][0]/(cm[0][0]+cm[0][1]))
F1 = 2*Precision*Recall/(Precision+Recall)
#计算准确率,MCC等
print("Precision: %f "%Precision)
print("Recall: %f"%Recall)
print("F1 Score: %f"%F1)
print("MCC: %f " %matthews_corrcoef(y_test,y_pred))

print( "ACC:  %f "% accuracy_score(y_test,y_pred))
print("AUC Score (Test): " , metrics.roc_auc_score(y_test,y_pred))

joblib.dump(clf,'rf1.model')