import matplotlib.pyplot as plt
import os
import numpy as np 
import pandas as pd
import seaborn as sns


for dirname, _, filenames in os.walk('../bimbiko/Downloads/ML-TP'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv('../bimbiko/diabetescsv/diabetes.csv')
#df.describe()
df.shape()


def plotData(dataset):

     c0=dataset[:,2]==0
     c1=dataset[:,2]==1
     XD1=dataset[:,0][c0]
     YD1=dataset[:,1][c0]
     XD2=dataset[:,0][c1]
     YD2=dataset[:,1][c1]
     
     plt.plot(XD1,YD1, 'gD')
     plt.plot(XD2,YD2, 'bo')
     plt.plot([0,g(bias,w1,w2,0)],[0,g(bias,w1,w2,5)])
    
     #plt.matshow()
     plt.show(dataset)