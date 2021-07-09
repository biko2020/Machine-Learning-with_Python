import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

bias = 0.3

# definition de la fonction d'activation sigmoid()     
def sigmoid(z):
    
    return 1/(1+np.exp(-z)) # retourn la formule de la fonction d'activation


    # XTest=[0.7, 4.2]
    # W = [0.1,0.2] 
    # bias=0.3

def predict(x1,x2,w1,w2,bias):
    # a la recherche de predicted_y = ?
    # input
    s = (w1*x1)+(w2*x2)+bias
    sigmoid(s)
    X, Y = make_regression(n_samples=100, n_features=2, noise=0)
    
    model = LinearRegression()
    model.fit(X, Y)
    
    XTest = [[x1,x2]]
    predict_y = model.predict(XTest)
  
    print("X=%s, Predict_y = %s" % (XTest[0], predict_y[0]))  
    
    
if __name__ == "__main__":
     predict(4.7,0.2,0.1,0.2,0.3)