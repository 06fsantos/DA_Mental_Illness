#!/usr/local/bin/python2.7
# encoding: utf-8
'''
ECS784P.data_analyctics_cleaning -- shortdesc

ECS784P.data_analyctics_cleaning is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2019 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''

import pandas as pd


#Load Original Data Set 
original_data = pd.read_csv('36361-0001-Data.tsv', sep='\t')

project_data = original_data[['CASEID', 'HEALTH2', 'AGE2', 'EDUCCAT2', 'EMPSTAT4', 'POVERTY2', 'K6SCMON', 'K6SCYR', 'K6SCMAX', 'QUESTID2','DEPNDANL',
                             'DEPNDCOC','DEPNDHAL', 'DEPNDHER','DEPNDINH','DEPNDSED','DEPNDSTM','DEPNDTRN','DEPNDILL','DEPNDPSY','ALCEVER','ALCYRTOT',
                             'ALBSTWAY','ALDAYPYR','ALDAYPMO','ALDAYPWK','ALCDAYS', 'NODR30A','DR5DAY','MJEVER','MJYRTOT',
                             'MRDAYPYR','MRDAYPMO','MRDAYPWK','MJDAY30A','DEPNDALC','DEPNDMRJ']][(original_data.CATAGE != 1)].copy()

print(len(project_data.index))
print(project_data.shape)
#print(project_data.duplicated().sum())


#Select Columns Indicating Drug Dependence Outside of Marijuana and Alcohol Along with ID
drug_columns = original_data[['QUESTID2','DEPNDANL','DEPNDCOC','DEPNDHAL',
                             'DEPNDHER','DEPNDINH','DEPNDSED','DEPNDSTM','DEPNDTRN','DEPNDILL','DEPNDPSY']].copy()
                             
#Create Column of IDs Where Drug Dependence Outside Weed/Alcohol was Indicated 
remove = drug_columns['QUESTID2'][(drug_columns.DEPNDANL == 1) | (drug_columns.DEPNDCOC == 1) | (drug_columns.DEPNDHAL == 1) | (drug_columns.DEPNDHER == 1) | (drug_columns.DEPNDINH == 1)| (drug_columns.DEPNDSED == 1) | (drug_columns.DEPNDSTM == 1) | (drug_columns.DEPNDTRN == 1)]
print(len(remove.index))

#project_data = project_data.drop([remove])
project_data_removed = project_data[~project_data['QUESTID2'].isin(remove)].dropna()
project_data_removed = project_data_removed.drop(['QUESTID2','DEPNDANL','DEPNDCOC','DEPNDHAL','DEPNDHER','DEPNDINH','DEPNDSED','DEPNDSTM','DEPNDTRN','DEPNDILL','DEPNDPSY'], axis = 1)
print('Table went from',len(project_data),'to',len(project_data_removed))

file_out = 'Project_Data_set.xlsx'
file_name = 'Data_Analytics_Project_Data.'
sheet = 'Data'

with pd.ExcelWriter(file_out, engine = 'xlsxwriter') as writer:
    project_data_removed.to_excel(writer)
    writer.save()
    writer.close()
