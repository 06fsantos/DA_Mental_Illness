'''
Created on 31 Mar 2019

@author: filipe
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')

def plot_heatmap(df):
    plt.figure(figsize = (5, 5))
    sns.heatmap(df.corr(), cmap = 'coolwarm', annot=False)
    plt.show()

df = pd.read_excel("Project_Data_set.xlsx")

df1 = df.loc[df['DEPNDALC'] == 1]
print (df1.shape)
df2 = df.loc[df['DEPNDMRJ'] == 1]

df.drop(['DEPNDALC', 'ALCEVER', 'DEPNDMRJ', 'MJEVER'], axis = 1)
df1.drop(labels = ['DEPNDALC', 'ALCEVER', 'DEPNDMRJ', 'MJEVER'], axis = 1)
df2.drop(labels = ['DEPNDALC', 'ALCEVER', 'DEPNDMRJ', 'MJEVER'], axis = 1)
print (df2.head())

print (df.corr())
plot_heatmap(df)

print (df1.corr())
plot_heatmap(df1)

print (df2.corr())
plot_heatmap(df2)

if __name__ == '__main__':
    pass