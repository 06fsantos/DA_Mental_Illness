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
                             'DEPNDCOC','DEPNDHAL', 'DEPNDHER','DEPNDINH','DEPNDSED','DEPNDSTM','DEPNDTRN','DEPNDIEM','DEPNDPSY','ALCEVER','ALCYRTOT',
                             'ALDAYPYR','ALDAYPMO','ALDAYPWK','ALCDAYS', 'NODR30A','DR5DAY','MJEVER','MJYRTOT',
                             'MRDAYPYR','MRDAYPMO','MRDAYPWK','MJDAY30A','DEPNDALC','DEPNDMRJ']][(original_data.CATAGE != 1)].copy()

print(len(project_data.index))
print(project_data.shape)

#Consolidate poverty Values into average 
poverty2_Series = project_data['POVERTY2'].values[project_data['POVERTY2'].values >= 0]
poverty2_avg = poverty2_Series.mean()
print('average number of days drank in past year: {}'.format(poverty2_avg))

POVERTY2_avg_mask = (project_data.POVERTY2 == -9)
column_name1 = 'POVERTY2'
project_data.loc[POVERTY2_avg_mask,column_name1] = poverty2_avg

#Consolidate K6SCYR Values into average 
k6scyr_Series = project_data['K6SCYR'].values[project_data['K6SCYR'].values >= 0]
k6scyr_avg = k6scyr_Series.mean()
print('average number of days drank in past year: {}'.format(k6scyr_avg))

K6SCYR_avg_mask = (project_data.K6SCYR == -9)
column_name1 = 'K6SCYR'
project_data.loc[K6SCYR_avg_mask,column_name1] = k6scyr_avg

#Consolidate HEALTH2 Values into average 
health2_Series = project_data['HEALTH2'].values[project_data['HEALTH2'].values >= 0]
health2_avg = health2_Series.mean()
print('average number of days drank in past year: {}'.format(health2_avg))

HEALTH2_avg_mask = (project_data.HEALTH2 == -9)
column_name1 = 'HEALTH2'
project_data.loc[HEALTH2_avg_mask,column_name1] = health2_avg

#Consolidate ALCYRTOT Values into zero or average 
ALCYRTOT_mask = (project_data.ALCYRTOT == 991) | (project_data.ALCYRTOT == 993)
column_name1 = 'ALCYRTOT'
project_data.loc[ALCYRTOT_mask,column_name1] = 0

alcyrtot_Series = project_data['ALCYRTOT'].values[project_data['ALCYRTOT'].values <= 366]
alcyrtot_avg = alcyrtot_Series.mean()
print('average number of days drank in past year: {}'.format(alcyrtot_avg))

ALCYRTOT_avg_mask = (project_data.ALCYRTOT == 994) | (project_data.ALCYRTOT == 997) | (project_data.ALCYRTOT == 998)
column_name1 = 'ALCYRTOT'
project_data.loc[ALCYRTOT_avg_mask,column_name1] = alcyrtot_avg

#Consolidate ALDAYPYR  Values into zero or average 
ALDAYPYR_mask = (project_data.ALDAYPYR == 991) | (project_data.ALDAYPYR == 993)
column_name2 = 'ALDAYPYR'
project_data.loc[ALDAYPYR_mask,column_name2] = 0

aldaypyr_Series = project_data['ALDAYPYR'].values[project_data['ALDAYPYR'].values <= 366]
aldaypyr_avg = aldaypyr_Series.mean()
print('average number of days drank in past year: {}'.format(aldaypyr_avg))

ALDAYPYR_avg_mask = (project_data.ALDAYPYR == 989) | (project_data.ALDAYPYR == 994) | (project_data.ALDAYPYR == 997) | (project_data.ALDAYPYR == 998) | (project_data.ALDAYPYR == 999)
column_name2 = 'ALDAYPYR'
project_data.loc[ALDAYPYR_avg_mask,column_name2] = aldaypyr_avg

#Consolidate ALDAYPMO Values into zero 
ALDAYPMO_mask = (project_data.ALDAYPMO == 91) | (project_data.ALDAYPMO == 93)
column_name2 = 'ALDAYPMO'
project_data.loc[ALDAYPMO_mask,column_name2] = 0

aldaypmo_Series = project_data['ALDAYPMO'].values[project_data['ALDAYPMO'].values <= 366]
aldaypmo_avg = aldaypmo_Series.mean()
print('average number of days drank in past year: {}'.format(aldaypmo_avg))

ALDAYPMO_avg_mask = (project_data.ALDAYPMO == 89) | (project_data.ALDAYPMO == 94) | (project_data.ALDAYPMO == 97) | (project_data.ALDAYPMO == 98) | (project_data.ALDAYPMO == 99)
column_name2 = 'ALDAYPMO'
project_data.loc[ALDAYPMO_avg_mask,column_name2] = 0

#Consolidate ALDAYPWK Values into zero 
ALDAYPWK_mask = (project_data.ALDAYPWK == 91) | (project_data.ALDAYPWK == 93)
column_name2 = 'ALDAYPWK'
project_data.loc[ALDAYPWK_mask,column_name2] = 0

aldaypwk_Series = project_data['ALDAYPWK'].values[project_data['ALDAYPWK'].values <= 366]
aldaypwk_avg = aldaypwk_Series.mean()
print('average number of days drank in past year: {}'.format(aldaypwk_avg))

ALDAYPWK_avg_mask = (project_data.ALDAYPWK == 94) | (project_data.ALDAYPWK == 97) | (project_data.ALDAYPWK == 98) | (project_data.ALDAYPWK == 99)
column_name2 = 'ALDAYPWK'
project_data.loc[ALDAYPWK_avg_mask,column_name2] = aldaypwk_avg

#Consolidate ALCDAYS Values into zero 
ALCDAYS_mask = (project_data.ALCDAYS == 91) | (project_data.ALCDAYS == 93)
column_name2 = 'ALCDAYS'
project_data.loc[ALCDAYS_mask,column_name2] = 0

alcdays_Series = project_data['ALCDAYS'].values[project_data['ALCDAYS'].values <= 366]
alcdays_avg = alcdays_Series.mean()
print('average number of days drank in past year: {}'.format(alcdays_avg))

ALCDAYS_avg_mask = (project_data.ALCDAYS == 94) | (project_data.ALCDAYS == 97) | (project_data.ALCDAYS == 98)
column_name2 = 'ALCDAYS'
project_data.loc[ALCDAYS_avg_mask,column_name2] = alcdays_avg

#Consolidate NODR30A Values into zero 
NODR30A_mask = (project_data.NODR30A == 991) | (project_data.NODR30A == 993)
column_name2 = 'NODR30A'
project_data.loc[NODR30A_mask,column_name2] = 0

nodr30a_Series = project_data['NODR30A'].values[project_data['NODR30A'].values <= 366]
nodr30a_avg = nodr30a_Series.mean()
print('average number of days drank in past year: {}'.format(nodr30a_avg))

NODR30A_avg_mask = (project_data.NODR30A == 994) | (project_data.NODR30A == 997) | (project_data.NODR30A == 998)
column_name2 = 'NODR30A'
project_data.loc[NODR30A_avg_mask,column_name2] = nodr30a_avg

#Consolidate DR5DAY Values into zero 
DR5DAY_mask = (project_data.DR5DAY == 91) | (project_data.DR5DAY == 93) | (project_data.DR5DAY == 80)
column_name2 = 'DR5DAY'
project_data.loc[DR5DAY_mask,column_name2] = 0

dr5day_Series = project_data['DR5DAY'].values[project_data['DR5DAY'].values <= 366]
dr5day_avg = dr5day_Series.mean()
print('average number of days drank in past year: {}'.format(dr5day_avg))

DR5DAY_avg_mask = (project_data.DR5DAY == 94) | (project_data.DR5DAY == 97) | (project_data.DR5DAY == 98)
column_name2 = 'DR5DAY'
project_data.loc[DR5DAY_avg_mask,column_name2] = dr5day_avg

#Consolidate MJYRTOT Values into zero 
MJYRTOT_mask = (project_data.MJYRTOT == 991) | (project_data.MJYRTOT == 993)
column_name2 = 'MJYRTOT'
project_data.loc[MJYRTOT_mask,column_name2] = 0

mjyrtot_Series = project_data['MJYRTOT'].values[project_data['MJYRTOT'].values <= 366]
mjyrtot_avg = mjyrtot_Series.mean()
print('average number of days drank in past year: {}'.format(mjyrtot_avg))

MJYRTOT_avg_mask = (project_data.MJYRTOT == 994) | (project_data.MJYRTOT == 997) | (project_data.MJYRTOT == 998)
column_name2 = 'MJYRTOT'
project_data.loc[MJYRTOT_avg_mask,column_name2] = mjyrtot_avg

#Consolidate MRDAYPYR Values into zero 
MRDAYPYR_mask = (project_data.MRDAYPYR == 991) | (project_data.MRDAYPYR == 993)
column_name2 = 'MRDAYPYR'
project_data.loc[MRDAYPYR_mask,column_name2] = 0

mrdaypyr_Series = project_data['MRDAYPYR'].values[project_data['MRDAYPYR'].values <= 366]
mrdaypyr_avg = mrdaypyr_Series.mean()
print('average number of days drank in past year: {}'.format(mrdaypyr_avg))

MRDAYPYR_avg_mask = (project_data.MRDAYPYR == 989) | (project_data.MRDAYPYR == 994) | (project_data.MRDAYPYR == 997) | (project_data.MRDAYPYR == 998) | (project_data.MRDAYPYR == 999)
column_name2 = 'MRDAYPYR'
project_data.loc[MRDAYPYR_avg_mask,column_name2] = mrdaypyr_avg

#Consolidate MRDAYPMO Values into zero 
MRDAYPMO_mask = (project_data.MRDAYPMO == 91) | (project_data.MRDAYPMO == 93)
column_name2 = 'MRDAYPMO'
project_data.loc[MRDAYPYR_mask,column_name2] = 0

mrdaypmo_Series = project_data['MRDAYPMO'].values[project_data['MRDAYPMO'].values <= 366]
mrdaypmo_avg = mrdaypmo_Series.mean()
print('average number of days drank in past year: {}'.format(mrdaypmo_avg))

MRDAYPMO_avg_mask = (project_data.MRDAYPMO == 89) | (project_data.MRDAYPMO == 94) | (project_data.MRDAYPMO == 97) | (project_data.MRDAYPMO == 98) | (project_data.MRDAYPMO == 99)
column_name2 = 'MRDAYPMO'
project_data.loc[MRDAYPYR_avg_mask,column_name2] = mrdaypmo_avg

#Consolidate MRDAYPWK Values into zero 
MRDAYPWK_mask = (project_data.MRDAYPWK == 91) | (project_data.MRDAYPWK == 93)
column_name2 = 'MRDAYPWK'
project_data.loc[MRDAYPWK_mask,column_name2] = 0

mrdaypwk_Series = project_data['MRDAYPWK'].values[project_data['MRDAYPWK'].values <= 366]
mrdaypwk_avg = mrdaypwk_Series.mean()
print('average number of days drank in past year: {}'.format(mrdaypwk_avg))

MRDAYPWK_avg_mask = (project_data.MRDAYPWK == 94) | (project_data.MRDAYPWK == 97) | (project_data.MRDAYPWK == 98) | (project_data.MRDAYPWK == 99)
column_name2 = 'MRDAYPWK'
project_data.loc[MRDAYPWK_avg_mask,column_name2] = mrdaypwk_avg

#Consolidate MJDAY30A Values into zero 
MJDAY30A_mask = (project_data.MJDAY30A == 91) | (project_data.MJDAY30A == 93)
column_name2 = 'MJDAY30A'
project_data.loc[MJDAY30A_mask,column_name2] = 0

mjday30a_Series = project_data['MJDAY30A'].values[project_data['MJDAY30A'].values <= 366]
mjday30a_avg = mjday30a_Series.mean()
print('average number of days drank in past year: {}'.format(mjday30a_avg))

MJDAY30A_avg_mask = (project_data.MJDAY30A == 94) | (project_data.MJDAY30A == 97) | (project_data.MJDAY30A == 98)
column_name2 = 'MJDAY30A'
project_data.loc[MJDAY30A_avg_mask,column_name2] = mjday30a_avg

#Test to ensure values were correctly replaced
'''
project_data2 = project_data[project_data['MJDAY30A'] == 0]

print(project_data2.shape)
'''


#Select Columns Indicating Drug Dependence Outside of Marijuana and Alcohol Along with ID
drug_columns = original_data[['QUESTID2','DEPNDANL','DEPNDCOC','DEPNDHAL', 'POVERTY2', 
                             'DEPNDHER','DEPNDINH','DEPNDSED','DEPNDSTM','DEPNDTRN','DEPNDIEM','DEPNDPSY','ALCEVER','ALCYRTOT','ALDAYPYR','ALDAYPMO','ALDAYPWK','ALCDAYS','NODR30A','DR5DAY','MJEVER','MJYRTOT','MRDAYPYR',
                             'MRDAYPMO','MRDAYPWK','MJDAY30A']].copy()
                             
                             
#Create Column of IDs Where Drug Dependence Outside Weed/Alcohol was Indicated 
remove = drug_columns['QUESTID2'][(drug_columns['DEPNDANL'] == 1) | (drug_columns['DEPNDCOC'] == 1) | (drug_columns['DEPNDHAL'] == 1) | (drug_columns['DEPNDHER'] == 1) | (drug_columns['DEPNDINH'] == 1) | (drug_columns['DEPNDSED'] == 1)
                                  | (drug_columns['DEPNDSTM'] == 1) | (drug_columns['DEPNDTRN'] == 1) | (drug_columns['DEPNDIEM'] == 1) | (drug_columns['DEPNDPSY'] == 1) | (drug_columns['ALCEVER'] == 85) | (drug_columns['ALCYRTOT'] == 985)
                                  | (drug_columns['ALDAYPYR'] == 985) | (drug_columns['ALDAYPMO'] == 85) | (drug_columns['ALDAYPWK'] == 85) | (drug_columns['ALCDAYS'] == 85) | (drug_columns['NODR30A'] == 985) | (drug_columns['DR5DAY'] == 85)
                                  | (drug_columns['MJYRTOT'] == 985) | (drug_columns['MRDAYPYR'] == 985) | (drug_columns['MRDAYPMO'] == 85) | (drug_columns['MRDAYPWK'] == 85) | (drug_columns['MJDAY30A'] == 85)]
                     
print(len(remove.index))




#project_data = project_data.drop([remove])
project_data_removed = project_data[~project_data['QUESTID2'].isin(remove)].dropna()
project_data_removed = project_data_removed.drop(['QUESTID2','DEPNDANL','DEPNDCOC','DEPNDHAL','DEPNDHER','DEPNDINH','DEPNDSED','DEPNDSTM','DEPNDTRN','DEPNDIEM','DEPNDPSY'], axis = 1)
print('Table went from',len(project_data),'to',len(project_data_removed))
print ('number of alcohol dependencies: {}'.format(project_data_removed['DEPNDALC'].sum()))
print ('number of marijuana dependencies: {}'.format(project_data_removed['DEPNDMRJ'].sum()))

file_out = 'Project_Data_set.xlsx'
file_name = 'Data_Analytics_Project_Data.'
sheet = 'Data'

with pd.ExcelWriter(file_out, engine = 'xlsxwriter') as writer:
    project_data_removed.to_excel(writer)
    writer.save()
    writer.close()

