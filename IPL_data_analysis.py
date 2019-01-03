import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#import plotly as ply
matches_data=pd.read_csv('D:\Python\ipl\matches.csv',index_col=['id'])
deliveries_data=pd.read_csv('D:\Python\ipl\deliveries.csv',index_col=['match_id'])
total_match=matches_data['season'].value_counts().values
Year_value=matches_data['season'].value_counts().index
plt.figure(figsize=(15, 7))
sns.barplot(x=Year_value, y=total_match )
plt.xlabel('Calender Year')
plt.ylabel('Numbers Of matches')
plt.title('No of IPL Matches Played Year-Wise')
total_match_city=matches_data['city'].value_counts().values
city_name=matches_data['city'].value_counts().index
plt.figure(figsize=(15, 7))
sns.barplot(x=city_name, y=total_match_city  )
plt.xticks(rotation=90)
plt.xlabel('Venue Name')
plt.ylabel('Numbers Of matches')
plt.title('No of IPL Matches Played Venue-wise')
total_match_city=matches_data['winner'].value_counts().values
city_name=matches_data['winner'].value_counts().index
plt.figure(figsize=(15, 7))
sns.barplot(x=city_name, y=total_match_city )
plt.xticks(rotation=90)
plt.xlabel('IPL Team Name')
plt.ylabel('Numbers Of matches Won')
plt.title('No of IPL Matches Won Team-wise')
