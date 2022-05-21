# Program to classify movies using clustering and k-means by ISH and RSDA

import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt

data = pd.read_excel('peliculas.xlsx')
# print(data)

X = data[["Likes","Dislikes"]]
#Visualise data points
plt.scatter(X["Dislikes"],X["Likes"],c='black')
plt.xlabel('Dislikes')
plt.ylabel('Likes')
plt.show()

K=3

# Select random observation as centroids
Centroids = (X.sample(n=K))
plt.scatter(X["Dislikes"],X["Likes"],c='black')
plt.scatter(Centroids["Dislikes"],Centroids["Likes"],c='red')
plt.xlabel('Dislikes')
plt.ylabel('Likes')
plt.show()

diff = 1
j=0

while(diff!=0):
    XD=X
    i=1
    for index1,row_c in Centroids.iterrows():
        ED=[]
        for index2,row_d in XD.iterrows():
            d1=(row_c["Dislikes"]-row_d["Dislikes"])**2
            d2=(row_c["Likes"]-row_d["Likes"])**2
            d=np.sqrt(d1+d2)
            ED.append(d)
        X[i]=ED
        i=i+1

    C=[]
    for index,row in X.iterrows():
        min_dist=row[1]
        pos=1
        for i in range(K):
            if row[i+1] < min_dist:
                min_dist = row[i+1]
                pos=i+1
        C.append(pos)
    X["Cluster"]=C
    Centroids_new = X.groupby(["Cluster"]).mean()[["Likes","Dislikes"]]
    if j == 0:
        diff=1
        j=j+1
    else:
        diff = (Centroids_new['Likes'] - Centroids['Likes']).sum() + (Centroids_new['Dislikes'] - Centroids['Dislikes']).sum()
        print(diff.sum())
    Centroids = X.groupby(["Cluster"]).mean()[["Likes","Dislikes"]]

color=['blue','green','cyan']
for k in range(K):
    data=X[X["Cluster"]==k+1]
    plt.scatter(data["Dislikes"],data["Likes"],c=color[k])
    # plt.show()

plt.xlabel('Dislikes')
plt.ylabel('Likes')
plt.scatter(Centroids["Dislikes"],Centroids["Likes"],c='red')
plt.show()