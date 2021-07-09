import matplotlib.pyplot as plt
import sys


bias = 4
w1 = 3
w2 = 2

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

if __name__ ==  "__main__":

    plotData(sys.dataset)	

