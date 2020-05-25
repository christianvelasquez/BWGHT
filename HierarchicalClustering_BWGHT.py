#!/usr/bin/env python
# coding: utf-8

# In[112]:


import numpy as np
import pandas as pd
import math

# Read in the data.
df = pd.read_csv('BWGHT.csv')
df = df[['cigprice','bwght']]
data_top = df.head(n = 50) # First 50 rows of dataset.
data_top


# In[116]:


# Initialize a dictionary that assigns the data points to a group/cluster.
group = list(data_top.index) 
mydict = {}
for groupNum in range(len(data_top)):
    dictTemp = {group[groupNum]: data_top.values[groupNum]}
    mydict.update(dictTemp)
mydict


# In[114]:


# Function to get the calculated distance matrix.
def dist(a, b):
    d = [a[0] - b[0], a[1] - b[1]]
    return math.sqrt(d[0] * d[0] + d[1] * d[1]),a,b

for i in range(len(mydict)):
    if len(mydict) != 1: # Repeat the process until there is only 1 cluster left.    
        # Calculate the distances between each possible combination of data points by calling the dist function.
        dists = []
        for m in range (len(mydict)):
            for k in range (len(mydict)):
                if (m < k):
                    d = dist(mydict[m],mydict[k])
                    dists += [d]
        dists = np.array(dists)
        print("ITERATION #",i+1,":")
        print("Distances between all possible combinations of data points:\n",dists)

        distValues = []
        for i in range(len(dists)):
            d = dists[i][0]
            distValues += [d]
        distValues = np.array(distValues)
        minIndex = np.argmin(distValues)
        min = dists[minIndex]
        print("\nMinimum result:",min)

        # Get the two closest points.
        minPoints = min[1:]
        
        # Get the keys of the data points.
        print("\nKeys of the data points:")
        for i in mydict:
            if (all(minPoints[0]==mydict[i])):
                firstGroup = i
                print(firstGroup,mydict[i])
                break
        for j in mydict:
            # If the two values are the same (i.e. the min distance is 0), then get the second instance of the value in the dictionary.
            if j == firstGroup:
                continue
            else:
                if (all(minPoints[1]==mydict[j])):
                    if(firstGroup == j):
                        break
                    else:
                        secondGroup = j
                        print(secondGroup,mydict[j])
                        break
        
        # Get the midpoint of the two closest points.
        xMidpoint = (minPoints[0][0]+minPoints[1][0])/2
        yMidpoint = (minPoints[0][1]+minPoints[1][1])/2
        midpoint = np.array([xMidpoint,yMidpoint])
        print("\nMidpoint: ",midpoint)
        
        # Add the midpoint as a new key/value pair in the dictionary.
        mydict[len(mydict)] = midpoint

        # Delete the key/value pair of the data points with the minimum distance.
        del mydict[firstGroup]
        del mydict[secondGroup]

        # Reset the keys of the dictionary to prevent skipping of key numbers.
        mydict = {i: v for i, v in enumerate(mydict.values())}
        print("\nUpdated dictionary:")
        print(mydict,"\n")
    else:
        break


# In[ ]:




