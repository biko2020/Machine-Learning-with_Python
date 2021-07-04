def f(x):
    	
	return -x+5
	
def generateData(n):
	from random import seed
	from random import random
# generate random numbers between 0-1
    
	seed(1)
	min=0
	max=11 # nombre d enregistrement
	
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
   data_set	= generateData(1)
   # afficher le tableaux dataset dans un colonne
   for row in data_set:
     print(row,end = "")
    #print(i, '\n')
     print()
