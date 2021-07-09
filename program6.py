import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split



def f(x):
    	
	return -x+5
	
def generateData(n):
	from random import seed
	from random import random
# generate random numbers between 0-1
    
	seed(1)
	min=0
	max=100 # nombre d enregistrement
	
	dataset=[]
	
	for _ in range(max):
		
		valueX1 = random()
		scaledvalueX1 = min + (valueX1 * (max - min))
		valueX2 = random()
		scaledvalueX2 = min + (valueX2 * (max - min))
		
		x1=round(scaledvalueX1,1)
		x2=round(scaledvalueX2,1)
		
		y0=f(x1)
		cl=0
		
		if(x2>y0):
			cl=1
			dataset.append([x1,x2,cl])
			
	return dataset
	
if __name__ == "__main__":
   # en fait appel a la fonction generatedata avec le parametre n
    dataset = generateData(100)
    dataset =  np.array(dataset)
    X = dataset[:,:2]
    y = dataset[:,2]
    y = y.astype(int)
    # diviser en learning set et test set
    X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.2,random_state=25)
    #afficher le contenu de dataset 100/2
    print(X_train[0:50,:]) 
    print('-' * 40)
    print(X_train[51:100,:])


    