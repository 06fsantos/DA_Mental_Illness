'''
Created on 31 Mar 2019

@author: filipe
'''
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

def isolate_columns_dependency(df, col_name, depend_col, depend_val, k6_col, k6_lim, sub_col, sub_min):
    
    df = df.loc[df[depend_col] == depend_val]
    df = df.loc[df[sub_col] > sub_min]
    df = df.loc[df[k6_col] > k6_lim]
    
    print (df.corr())
    
    col = df[col_name].copy(deep = False)
    
    return col


def isolate_columns(df, col_name):
    
    col = df[col_name].copy(deep = False)
    return col 

def plot_relationship(x, y, title):
    
    fig = plt.figure()
    ax = fig.add_subplot(111)

    
    ax.scatter(x, y, color = 'r', marker = '.', alpha = 0.5)
    ax.set_title(title)
    ax.set_ylabel('K6 score (>13 associated with severe mental illness)')
    ax.set_xlabel =('Number of times drank alcohol in the past 12 months') 
    
    
    plt.show()
if __name__ == '__main__':
    data = pd.read_excel(io = 'Project_Data_set.xlsx')
    
    # Relationship between number of drinks and k6 for people who abuse alcohol 
    alc_x_data = isolate_columns_dependency(data, 'NODR30A', 'DEPNDALC', 1, 'K6SCMON', 2, 'NODR30A', 0)
    alc_y_data = isolate_columns_dependency(data, 'K6SCMON', 'DEPNDALC', 1, 'K6SCMON', 2, 'NODR30A', 0)
    title = 'alcohol consumption in the past year and mental distress (K6) for people were dependent on alcohol in the past 12 months'
    plot_relationship(alc_x_data, alc_y_data, title)
    
    # Relationship between number of drinks and k6 for non abusers 
    alc_x_data = isolate_columns_dependency(data, 'NODR30A', 'DEPNDALC', 0, 'K6SCMON', 2, 'NODR30A', 0)
    alc_y_data = isolate_columns_dependency(data, 'K6SCMON', 'DEPNDALC', 0, 'K6SCMON', 2, 'NODR30A', 0)
    title = 'alcohol consumption in the past year and mental distress (K6) for people were not dependent on alcohol in the past 12 months'
    plot_relationship(alc_x_data, alc_y_data, title)
    
    # Relationship between number of drinks and k6 for people who abuse alcohol 
    alc_x_data = isolate_columns_dependency(data, 'MJDAY30A', 'DEPNDMRJ', 1, 'K6SCMON', 2, 'MJDAY30A', 0)
    alc_y_data = isolate_columns_dependency(data, 'K6SCMON', 'DEPNDMRJ', 1, 'K6SCMON', 2, 'MJDAY30A', 0)
    title = 'marijuana consumption in past month and mental distress (K6) for people were dependent on marijuana in the past 12 months'
    plot_relationship(alc_x_data, alc_y_data, title)
    
    # Relationship between number of drinks and k6 for non abusers 
    alc_x_data = isolate_columns_dependency(data, 'MJDAY30A', 'DEPNDMRJ', 0, 'K6SCMON', 2, 'MJDAY30A', 0)
    alc_y_data = isolate_columns_dependency(data, 'K6SCMON', 'DEPNDMRJ', 0, 'K6SCMON', 2, 'MJDAY30A', 0)
    title = 'marijuana consumption in past month and mental distress (K6) for people were not dependent on marijuana in the past 12 months'
    plot_relationship(alc_x_data, alc_y_data, title)
    '''
    # relationship between marijuana abuse use and K6
    mrj_x_data = isolate_columns_dependency(data, 'MRDAYPYR', 'DEPNDMRJ', 0, 'K6SCMAX', 0, 'MRDAYPYR', 10)
    mrj_y_data = isolate_columns_dependency(data, 'K6SCMAX', 'DEPNDMRJ', 0, 'K6SCMAX', 0, 'MRDAYPYR', 10)
    title = 'relationship between marijuana abuse and mental distress (K6)'
    plot_relationship(mrj_x_data, mrj_y_data, title)
    
    # relationship between marijuana abuse use and K6
    mrj_x_data = isolate_columns_dependency(data, 'POVERTY2', 'DEPNDMRJ', 'K6SCMAX', 0, 'MRDAYPYR', 10)
    mrj_y_data = isolate_columns_dependency(data, 'K6SCMAX', 'DEPNDMRJ', 'K6SCMAX', 0, 'MRDAYPYR', 10)
    title = 'relationship between marijuana abusers living in poverty and mental distress (K6)'
    plot_relationship(mrj_x_data, mrj_y_data, title)
    
    # relationship between marijuana abuse use and K6
    mrj_x_data = isolate_columns_dependency(data, 'POVERTY2', 'DEPNDALC', 'K6SCMAX', 0, 'ALDAYPYR', 10)
    mrj_y_data = isolate_columns_dependency(data, 'K6SCMAX', 'DEPNDALC', 'K6SCMAX', 0, 'ALDAYPYR', 10)
    title = 'relationship between alcohol abusers living in poverty and mental distress (K6)'
    plot_relationship(mrj_x_data, mrj_y_data, title)
    
    # Relationship between general health and mental health
    alc_x_data = isolate_columns(data, 'HEALTH2')
    alc_y_data = isolate_columns(data, 'K6SCMAX')
    title = 'relationship between general health and mental distress (K6)'
    plot_relationship(alc_x_data, alc_y_data, title)
    '''

    