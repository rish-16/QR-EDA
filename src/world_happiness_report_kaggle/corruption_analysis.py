'''
Dataset obtained from 
https://www.kaggle.com/mathurinache/world-happiness-report-20152021
'''

from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
import csv

df_2015 = pd.DataFrame(pd.read_csv('../../datasets/world_happiness_report/2015.csv'))
df_2016 = pd.DataFrame(pd.read_csv('../../datasets/world_happiness_report/2016.csv'))
df_2017 = pd.DataFrame(pd.read_csv('../../datasets/world_happiness_report/2017.csv'))
df_2018 = pd.DataFrame(pd.read_csv('../../datasets/world_happiness_report/2018.csv'))
df_2019 = pd.DataFrame(pd.read_csv('../../datasets/world_happiness_report/2019.csv'))
df_2020 = pd.DataFrame(pd.read_csv('../../datasets/world_happiness_report/2020.csv'))
df_2021 = pd.DataFrame(pd.read_csv('../../datasets/world_happiness_report/2021.csv'))

dfs = [
    df_2015,
    df_2016,
    df_2017,
    df_2018,
    df_2019,
    df_2020,
    df_2021    
]

countries = []

# for df in dfs:
    # print (df.columns)
    # df.set_index('Country', inplace=True)

for df in dfs:
    countries.append(df['Country'].tolist())
    
unique_countries = list(set.intersection(*map(set, countries)))
happiness_data = {}

for ctr in unique_countries:
    happiness_data[ctr] = []
    
for df in dfs:
    for ctr in unique_countries:
        happiness_data[ctr].append(df[df['Country'] == ctr]['Corruption'].astype(float).values[0])
        
FINAL_COUNTRIES = ['Singapore', 'Malaysia', 'Vietnam', 'Indonesia', 'Philippines', 'Cambodia', 'Thailand', 'United States', 'United Kingdom']
FINAL_DICT = {}
    
for ctr in FINAL_COUNTRIES:
    FINAL_DICT[ctr] = happiness_data[ctr][-3:]
    
pprint (FINAL_DICT)
        
# years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
years = ['2019', '2020', '2021']
for ctr, pts in FINAL_DICT.items():
    plt.scatter(years, pts, 5)
    plt.plot(years, pts)
    
plt.title("Corruption in ASEAN 2015 - 2021")    
plt.ylim([0, 1])
plt.legend(FINAL_COUNTRIES)
plt.xlabel("Years")
plt.ylabel("Corruption levels")
plt.show()