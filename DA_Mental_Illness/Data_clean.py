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
import numpy as np

#Load Original Data Set 
original_data = pd.read_csv('36361-0001-Data.tsv', sep='\t')

project_data = original_data[['CASEID', 'HEALTH2', 'AGE2', 'EDUCCAT2', 'EMPSTAT4', 'POVERTY2', 'K6SCMON', 'K6SCYR', 'K6SCMAX', 'QUESTID2','DEPNDANL',
                             'DEPNDCOC','DEPNDHAL', 'DEPNDHER','DEPNDINH','DEPNDSED','DEPNDSTM','DEPNDTRN','DEPNDIEM','DEPNDPSY','ALCEVER','ALCYRTOT',
                             'ALBSTWAY','ALDAYPYR','ALDAYPMO','ALDAYPWK','ALCDAYS', 'NODR30A','DR5DAY','MJEVER','MJYRTOT',
                             'MRDAYPYR','MRDAYPMO','MRDAYPWK','MJDAY30A','DEPNDALC','DEPNDMRJ']][(original_data.CATAGE != 1)].copy()

print(len(project_data.index))
print(project_data.shape)



#Consolidate ALCYRTOT Values into zero and identify the mean average for the column 
ALCYRTOT_mask = (project_data.ALCYRTOT == 991) | (project_data.ALCYRTOT == 993)
column_name1 = 'ALCYRTOT'
project_data.loc[ALCYRTOT_mask,column_name1] = 0

alcyrtot_Series = project_data['ALCYRTOT'].values[project_data['ALCYRTOT'].values <= 366]
alcyrtot_avg = alcyrtot_Series.mean()
print('average number of days drank in past year: {}'.format(alcyrtot_avg))

#Consolidate ALDAYPYR  Values into zero 
ALDAYPYR_mask = (project_data.ALDAYPYR == 991) | (project_data.ALDAYPYR == 993)
column_name2 = 'ALDAYPYR'
project_data.loc[ALDAYPYR_mask,column_name2] = 0

#Consolidate ALDAYPMO Values into zero 
ALDAYPMO_mask = (project_data.ALDAYPMO == 91) | (project_data.ALDAYPMO == 93)
column_name2 = 'ALDAYPMO'
project_data.loc[ALDAYPMO_mask,column_name2] = 0

#Consolidate ALDAYPWK Values into zero 
ALDAYPWK_mask = (project_data.ALDAYPWK == 91) | (project_data.ALDAYPWK == 93)
column_name2 = 'ALDAYPWK'
project_data.loc[ALDAYPWK_mask,column_name2] = 0

#Consolidate ALCDAYS Values into zero 
ALCDAYS_mask = (project_data.ALCDAYS == 91) | (project_data.ALCDAYS == 93)
column_name2 = 'ALCDAYS'
project_data.loc[ALCDAYS_mask,column_name2] = 0

#Consolidate NODR30A Values into zero 
NODR30A_mask = (project_data.NODR30A == 991) | (project_data.NODR30A == 993)
column_name2 = 'NODR30A'
project_data.loc[NODR30A_mask,column_name2] = 0

#Consolidate DR5DAY Values into zero 
DR5DAY_mask = (project_data.DR5DAY == 91) | (project_data.DR5DAY == 93)
column_name2 = 'DR5DAY'
project_data.loc[DR5DAY_mask,column_name2] = 0

#Consolidate MJYRTOT Values into zero 
MJYRTOT_mask = (project_data.MJYRTOT == 91) | (project_data.MJYRTOT == 93)
column_name2 = 'MJYRTOT'
project_data.loc[MJYRTOT_mask,column_name2] = 0

#Consolidate MRDAYPYR Values into zero 
MRDAYPYR_mask = (project_data.MRDAYPYR == 991) | (project_data.MRDAYPYR == 993)
column_name2 = 'MRDAYPYR'
project_data.loc[MRDAYPYR_mask,column_name2] = 0

#Consolidate MRDAYPMO Values into zero 
MRDAYPMO_mask = (project_data.MRDAYPMO == 91) | (project_data.MRDAYPMO == 93)
column_name2 = 'MRDAYPMO'
project_data.loc[MRDAYPYR_mask,column_name2] = 0

#Consolidate MRDAYPWK Values into zero 
MRDAYPWK_mask = (project_data.MRDAYPWK == 91) | (project_data.MRDAYPWK == 93)
column_name2 = 'MRDAYPWK'
project_data.loc[MRDAYPWK_mask,column_name2] = 0

#Consolidate MJDAY30A Values into zero 
MJDAY30A_mask = (project_data.MJDAY30A == 91) | (project_data.MJDAY30A == 93)
column_name2 = 'MJDAY30A'
project_data.loc[MJDAY30A_mask,column_name2] = 0


#Select Columns Indicating Drug Dependence Outside of Marijuana and Alcohol Along with ID
drug_columns = original_data[['QUESTID2','DEPNDANL','DEPNDCOC','DEPNDHAL',
                             'DEPNDHER','DEPNDINH','DEPNDSED','DEPNDSTM','DEPNDTRN','DEPNDIEM','DEPNDPSY','ALCEVER','ALCYRTOT','ALDAYPYR','ALDAYPMO','ALDAYPWK','ALCDAYS','NODR30A','DR5DAY','MJEVER','MJYRTOT','MRDAYPYR',
                             'MRDAYPMO','MRDAYPWK','MJDAY30A']].copy()
                             
                             
#Create Column of IDs Where Drug Dependence Outside Weed/Alcohol was Indicated 
remove = drug_columns['QUESTID2'][(drug_columns['DEPNDANL'] == 1) | (drug_columns['DEPNDCOC'] == 1) | (drug_columns['DEPNDHAL'] == 1) | (drug_columns['DEPNDHER'] == 1) | (drug_columns['DEPNDINH'] == 1)| (drug_columns['DEPNDSED'] == 1)
                                  | (drug_columns['DEPNDSTM'] == 1) | (drug_columns['DEPNDTRN'] == 1) | (drug_columns['DEPNDIEM'] == 1) | (drug_columns['DEPNDPSY'] == 1)]
                     
print(len(remove.index))




#project_data = project_data.drop([remove])
project_data_removed = project_data[~project_data['QUESTID2'].isin(remove)].dropna()
project_data_removed = project_data_removed.drop(['QUESTID2','DEPNDANL','DEPNDCOC','DEPNDHAL','DEPNDHER','DEPNDINH','DEPNDSED','DEPNDSTM','DEPNDTRN','DEPNDIEM','DEPNDPSY'], axis = 1)
print ('Table went from',len(project_data),'to',len(project_data_removed))
print ('number of alcohol dependencies: {}'.format(project_data_removed['DEPNDALC'].sum()))
print ('number of marijuana dependencies: {}'.format(project_data_removed['DEPNDMRJ'].sum()))

file_out = 'Project_Data_set.xlsx'
file_name = 'Data_Analytics_Project_Data.'
sheet = 'Data'

with pd.ExcelWriter(file_out, engine = 'xlsxwriter') as writer:
    project_data_removed.to_excel(writer)
    writer.save()
    writer.close()
