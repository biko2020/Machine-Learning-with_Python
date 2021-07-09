import matplotlib.pyplot as plt
import os
import numpy as np 
import pandas as pd
import seaborn as sns
import sys

# importe les donnees de dataset depuis le fichier  diabetes.csv
for dirname, _, filenames in os.walk('/path/dir'):
     for filename in filenames:
        dataset = pd.read_csv('/path/file')

# initialiser les parametres de la fonction g()
bias = 4
w1 = 3
w2 = 2


def g(bias,w1,w2,x):

   for X in range(0,5):
       if X != 0:
          x = 5
          return x

def plotData(dataset):
 
    c0=dataset[:,2]==0
    c1=dataset[:,2]==1

    XD1=dataset[:,0][c0]
    YD1=dataset[:,1][c0]

    XD2=dataset[:,0][c1]
    YD2=dataset[:,1][c1]

    plt.plot(XD1,YD1, 'ro')
    plt.plot(XD2,YD2, 'ro')

plt.plot([0,g(bias,w1,w2,0)],[0,g(bias,w1,w2,5)])
plt.show() # affiche la figure a l'ecran
   

<<<<<<< HEAD
if __name__ ==  "__main__":

   plotData(sys.dataset)
  
=======
if __name__ ==  "__main__ ":

   plotData(sys.dataset)
  
>>>>>>> 540ee1369afc83311a2a0fe6457df46f046195ea
