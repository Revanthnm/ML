import pandas as pd
import numpy as np
 
data = pd.read_csv("dataset/pgm1.csv")
print(data)
 
d = np.array(data)[:,:-1]
print("\n The attributes are: \n",d)

target = np.array(data)[:,-1]
print("\n The target is: ",target)

num_attribute = len(d[0])

def train(c,t):
    hypothesis = ['0']*num_attribute
             
    for i in range(0, len(d)):
        if t[i] == 'yes':
            print ("\nInstance ", i+1, "is", d[i], " and is Positive Instance")
            for j in range(0, num_attribute):
                if hypothesis[j] == '0' or hypothesis[j] == d[i][j]:
                    hypothesis[j] = d[i][j]
                else:
                    hypothesis[j] = '?'
            print("The hypothesis for the training instance", i+1, " is: " , hypothesis, "\n")
            
        if t[i] == 'no':
            print ("\nInstance ", i+1, "is", d[i], " and is Negative Instance Hence Ignored")
                 
    return hypothesis

print("\n The final hypothesis is:",train(d,target))