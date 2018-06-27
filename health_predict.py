
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 15:13:53 2018

@author: Administrator
"""
from sklearn.datasets import load_svmlight_file
from sklearn import svm
from sklearn.externals import joblib
from sys import argv
import numpy as np
from scipy.sparse import csr_matrix, coo_matrix
def convert(term_dict):
    ''' Convert a dictionary with elements of form ('d1', 't1'): 12 to a CSR type         matrix.
    The element ('d1', 't1'): 12 becomes entry (0, 0) = 12.
    * Conversion from 1-indexed to 0-indexed.
    * d is row
    * t is column.
    '''
    # Create the appropriate format for the COO format.

    data = []
    row = []
    col = []
    for k, v in term_dict.items():
        r = int(k[0][1:])
        c = int(k[1][1:])
        data.append(v)
        row.append(r-1)
        col.append(c-1)
    # Create the COO-matrix
 #   print(row,col)
    coo = coo_matrix((data,(row,col)))

    # Let Scipy convert COO to CSR format and return

    return csr_matrix(coo)
def getmatrix(eyeargv):
    eyeargv = np.array(eyeargv).astype('float')
    num = (int)(len(eyeargv)/5)
    dic = {}
    for j in range(num):
        for t in range(5):
            dic['d'+str(j+1),'t'+str(t+1)] = eyeargv[j*6+t]
        
  #      print(j)
#    b = {('d'+str(i),'t1'):eyeargv[0]}
    #b = {('d'+str(i),'t1'):  eyeargv[0],('d'+str(i),'t2'): eyeargv[1],('d'+str(i),'t3'):eyeargv[2],('d'+str(i),'t4'):eyeargv[3],('d'+str(i),'t5'):eyeargv[4],('d'+str(i),'t6'):eyeargv[5]}
  #  print(dic)
    c = convert(dic)
    return c
#fr_n="E:/raw_project/eye_model/eye_predict.txt"

#X,y=load_svmlight_file(fr_n)

RF=joblib.load('rf_health.model')

#a = argv[1]
#a = {('d1','t1'):0.560695,('d1','t2'):0.550624,('d1','t3'):0.0,('d1','t4'):0.0,('d1','t5'):0.0035411,('d1','t6'):0.00353881,('d2','t1'): 12,('d2','t2'): 10,('d2','t3'):5,('d2','t4'):5,('d2','t5'):5,('d2','t6'):5}
#应用模型argv[1:7]进行预测

#doc_term_dict = {('d1','t1'):  0.560695,('d1','t2'): 0.550624,('d1','t3'):0.0,('d1','t4'):0.0,('d1','t5'):0.0035411,('d1','t6'):0.00353881,('d2','t1'): 12,('d2','t2'): 10,('d2','t3'):5,('d2','t4'):5,('d2','t5'):5,('d2','t6'):5}   
#b = convert(a)
#result=RF.predict(b)
#print(result)
#print('-------------------------------------------------')
num = (int)((len(argv)-1)/5)
res = []
a = getmatrix(argv[1:])
#print(a)
   # res.append(RF.predict(a)[-1])
res = RF.predict(a)
print(res)
