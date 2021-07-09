import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from matplotlib import pyplot



X = []
XTest = [[0.7, 4.2],[3.8, 1.3], [2.5, 2.2], [3.3, 3.9], [0.5, 0.1]]
bias = -1.22 
W = [0.35, 0.19]

# definition de la fonction Rectified Linear Units ()     
def sigmoid(z):
 
    return (max(0,z)) # f(z)=max(0,z)


def sigmoidV2(V):
    # definition de la boucle des valeurs V
    valeur = [index for index in range(0, V)]
    # fait appel au fonction de calculer 
    vecteur = [sigmoid(index) for index in valeur]
    # affichage

    print(vecteur)
    print ('-' * 40)
    #pyplot.plot(valeur, v)
    #pyplot.show()
        

def predictV2(X,W,bias):
    # a la recherche de predicted_y = ?
    # input
    s = (W*X)+bias
    sigmoid(s)
    sigmoidV2(5)
 
    X, Y = make_regression(n_samples=100, n_features=2, noise=0)
    
    model = LinearRegression()
    model.fit(X, Y)
   
    XTest = [[0.7, 4.2],[3.8, 1.3], [2.5, 2.2], [3.3, 3.9], [0.5, 0.1]]
    
    #for position in range(len(XTest)): 
    #    XTest = XTest[position:2]  
    predict_y = model.predict(XTest)
  
    print("X=%s, Predict_y = %s" % (XTest[0], predict_y[0]))  
    
    
if __name__ == "__main__":
    #sigmoidV2(5)

    predictV2(0.2,0.19,bias)