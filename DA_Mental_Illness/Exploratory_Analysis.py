'''
Created on 31 Mar 2019

@author: filipe
'''
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

def isolate_columns(df, col_name, depend_col):
    
    df = df.loc[df[depend_col] == 1]
    
    col = df[col_name].copy(deep = False)
    print (col)
    return col

def plot_relationship(x, y, title):
    
    fig = plt.figure()
    ax = fig.add_subplot(111)

    
    ax.scatter(x, y, color = 'r', marker = '.', alpha = 0.1)
    ax.set_title(title)
    ax.set_ylabel = 'K6 score (>13 associated with severe mental illness)'
    ax.set_xlabel = 'Number of times drank alcohol in the past 12 months'
    
    
    plt.show()
if __name__ == '__main__':
    data = pd.read_excel(io = 'Project_Data_set.xlsx')
    
    # Relationship between alcohol abuse
    alc_x_data = isolate_columns(data, 'ALDAYPYR', 'DEPNDALC')
    alc_y_data = isolate_columns(data, 'K6SCMAX', 'DEPNDALC')
    title = 'relationship between alcohol abuse and mental distress (K6)'
    plot_relationship(alc_x_data, alc_y_data, title)
    
    # relationship between marijuana abuse use and K6
    mrj_x_data = isolate_columns(data, 'MRDAYPYR', 'DEPNDMRJ')
    mrj_y_data = isolate_columns(data, 'K6SCMAX', 'DEPNDMRJ')
    title = 'relationship between marijuana abuse and mental distress (K6)'
    plot_relationship(mrj_x_data, mrj_y_data, title)
    
    # relationship between marijuana abuse use and K6
    mrj_x_data = isolate_columns(data, 'POVERTY2', 'DEPNDMRJ')
    mrj_y_data = isolate_columns(data, 'K6SCMAX', 'DEPNDMRJ')
    title = 'relationship between marijuana abusers living in poverty and mental distress (K6)'
    plot_relationship(mrj_x_data, mrj_y_data, title)
    
    # relationship between marijuana abuse use and K6
    mrj_x_data = isolate_columns(data, 'POVERTY2', 'DEPNDALC')
    mrj_y_data = isolate_columns(data, 'K6SCMAX', 'DEPNDALC')
    title = 'relationship between alcohol abusers living in poverty and mental distress (K6)'
    plot_relationship(mrj_x_data, mrj_y_data, title)
    

    