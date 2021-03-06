# -*- coding: utf-8 -*-
"""project1_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vZGuunY6ql1IvPO9hen0q04dbXCGJYqn
"""

#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import dataset
df = pd.read_csv('https://raw.githubusercontent.com/CunyLaguardiaDataAnalytics/datasets/master/2014-15_To_2016-17_School-_Level_NYC_Regents_Report_For_All_Variables.csv')

#iterating the columns to get column names

for col in df.columns:
  print(col)

#not unique, they're all 'K-8'

df['School Level'].is_unique

#remove multiple columns

drop_cols = ['School DBN', 'School Level', 'Regents Exam', 'Year', 'Total Tested', 'Mean Score', 'Number Scoring Below 65','Percent Scoring Below 65', 'Number Scoring 65 or Above', 'Percent Scoring 65 or Above', 'Number Scoring 80 or Above','Number Scoring CR','Percent Scoring CR']
df.drop(drop_cols, inplace = True, axis=1)

#fiilter out 's'
df[df['Percent Scoring 80 or Above']!='s']
#hmmm

df.head(18762)

#filter out rows with 's' in 'Percent Scoring 80 or Above' column
df2 = df[df['Percent Scoring 80 or Above']!='s']
df2.isnull()

#total # of missing values
df2.isnull().sum()

df2.head(202670)
#success

#change datatype to float

df3 = df2.astype({'Percent Scoring 80 or Above':'float'})
df3['Percent Scoring 80 or Above'].dtype

#filter out 0 from 'Percent Scoring 80 or Above' column
df3[df3['Percent Scoring 80 or Above']>0]

#assign filtered dataset to new df4
df4 = df3[df3['Percent Scoring 80 or Above']>0]

#now i want to compare LIC HS percentages to rest of the schools

#first, some stats of the whole dataset after filtering out missing data 's' and 0%
df4.describe()

#select rows containing 'LIC HS'

df4.loc[df4['School Name']=='Long Island City High School']

#assign to new df5

df5=df4.loc[df4['School Name']=='Long Island City High School']

#number of rows/count
df5.count()

#stats of only LIC HS after filters
df5.describe()

#select rows NOT 'LIC HS'
df6 = df4.loc[df4['School Name']!='Long Island City High School']
df6

#stats of other schools NOT lic hs
df6.describe()

#count how many times 'Percent Scoring 80 or Above' shows up in unique school names in other schools NOT lic hs
df6.groupby(['School Name'])['Percent Scoring 80 or Above'].count().sort_values(ascending=False)

#count how many times 'Percent Scoring 80 or Above' shows up in lic hs
df5.groupby(['School Name'])['Percent Scoring 80 or Above'].count().sort_values(ascending=False)

#mean of all other schools not lic hs for 'Percent Scoring 80 or Above'
df6.groupby(['School Name'])['Percent Scoring 80 or Above'].mean().sort_values(ascending=False)

#plot bar graph of means of all  other schools NOT lic hs vs mean of lic hs
data = {'Long Island City High School':12.988483, 'All Other Schools':29.100267}

schools = list(data.keys())
means = list(data.values())

fig = plt.figure(figsize = (5, 10))
plt.bar(schools, means, color ='maroon', width = 0.4)

plt.xlabel("LIC HS vs All Other Schools")
plt.ylabel("Average Percent Scoring 80 or Above")
plt.title("Comparison of Avg % Scores 80 or Above of LIC HS vs All Other Schools")
plt.show()