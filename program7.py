from sklearn.model_selection import train_test_split
from sklearn.datasets import make_blobs
from keras.models import Sequential
from keras.layers import Activation, Dense
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


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


def g(bias,w1,w2,x):

    return (-bias/w2)-(w1/w2)*x

def plotData(dataset,W,bias):

    c0=dataset[:,2]==0
    c1=dataset[:,2]==1

    XD1=dataset[:,0][c0]
    YD1=dataset[:,1][c0]

    XD2=dataset[:,0][c1]
    YD2=dataset[:,1][c1]

    plt.plot(XD1,YD1, 'gD')
    plt.plot(XD2,YD2, 'bo')
    #pour tracer la droite(modèle)
    w1=W[0][0]
    w2=W[1][0]

    plt.plot([0,g(bias,w1,w2,0)],[5,g(bias,w1,w2,5)])
    plt.show()
	
if __name__ == "__main__":
   # en fait appel a la fonction generatedata avec le parametre n
    dataset = generateData(100)
    dataset =  np.array(dataset)
    X = dataset[:,:2]
    y = dataset[:,2]
    y = y.astype(int)
                                                  
    layer = Dense(1, input_shape=(2,) , activation='sigmoid',kernel_initializer='ones',bias_initializer='zeros')
    model = Sequential()
    model.add(layer)
    W,bias=model.get_weights() #in the initialization step
    model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=25)
    model.fit(X_train,y_train,epochs=5000)

	# on fait appel a la fonction poltdata
    plotData(dataset,W,bias)