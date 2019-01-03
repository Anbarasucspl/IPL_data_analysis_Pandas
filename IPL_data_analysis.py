import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
class graph_plot:
	def barplotseaborn(self,value1,value2,xlabelval,ylabelval,titleval):
		plt.figure(figsize=(15, 7))
		sns.barplot(x=value1, y=value2  )
		plt.xticks(rotation=90)
		plt.xlabel(xlabelval)
		plt.ylabel(ylabelval)
		plt.title(titleval)
matches_data=pd.read_csv('D:\Python\ipl\matches.csv',index_col=['id'])
deliveries_data=pd.read_csv('D:\Python\ipl\deliveries.csv',index_col=['match_id'])
total_match=matches_data['season'].value_counts().values
Year_value=matches_data['season'].value_counts().index
obj_bar_plot = graph_plot()
obj_bar_plot.barplotseaborn(Year_value,total_match,'Calender Year','Numbers Of matches','No of IPL Matches Played Year-Wise')
total_match_city=matches_data['city'].value_counts().values
city_name=matches_data['city'].value_counts().index
obj_bar_plot.barplotseaborn(city_name,total_match_city,'Venue Name','Numbers Of matches','No of IPL Matches Played Venue-wise')
total_team_wise=matches_data['winner'].value_counts().values
team_name=matches_data['winner'].value_counts().index
obj_bar_plot.barplotseaborn(team_name,total_team_wise,'IPL Team Name','Numbers Of matches Won','No of IPL Matches Won Team-wise')
