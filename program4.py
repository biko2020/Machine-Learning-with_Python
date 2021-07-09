import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from matplotlib import pyplot


w = []
X = []
bias = 0.3
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
    s = W*X+bias
    sigmoid(s)
    sigmoidV2(5)
 
    X, Y = make_regression(n_samples=100, n_features=2, noise=0)
    
    model = LinearRegression()
    model.fit(X, Y)
    #XTest, z = np.arange(10).reshape((3, 2)), range(5)
    XTest = [[1.2,1.3]]
    predict_y = model.predict(XTest)
  
    print("X=%s, Predict_y = %s" % (XTest[0], predict_y[0]))  
    
    
if __name__ == "__main__":
    #sigmoidV2(5)

    predictV2(4.2,0.2,bias)