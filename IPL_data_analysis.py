import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
class graph_plot:
    def barplotseaborn(self,value1,value2,xlabelval,ylabelval,titleval):
        plt.figure(figsize=(15, 7))
        draw_graph=sns.barplot(x=value1, y=value2  )
        plt.xticks(rotation=90)
        plt.xlabel(xlabelval)
        plt.ylabel(ylabelval)
        plt.title(titleval)
        plt.show()
    def pie_graph(self,value1,label_field):
        plt.pie(value1,labels=label_field,startangle=90,autopct='%.1f%%')
        plt.title('TOSS_DECISION : ')
        plt.show()
matches_data=pd.read_csv('D:\Python\ipl\matches.csv')
deliveries_data=pd.read_csv('D:\Python\ipl\deliveries.csv')

#No of Matches played across seasons
total_match=matches_data['season'].value_counts().values
Year_value=matches_data['season'].value_counts().index
obj_bar_plot = graph_plot()
obj_bar_plot.barplotseaborn(Year_value,total_match,'Calender Year','Numbers Of matches','No of IPL Matches Played Year-Wise')

# No of Matches played Venue-Wise
total_match_city=matches_data['city'].value_counts().values
city_name=matches_data['city'].value_counts().index
obj_bar_plot.barplotseaborn(city_name,total_match_city,'Venue Name','Numbers Of matches','No of IPL Matches Played Venue-wise')

# No of Matches played Team-Wise
tot_mat_team= matches_data['team1'].append(matches_data['team2'])
obj_bar_plot.barplotseaborn(tot_mat_team.value_counts().index,tot_mat_team.value_counts().values,'IPL Team Name','Numbers Of matches Played','No of IPL Matches Played Team-wise')

#No of IPL Matches Won Team-wise
total_team_wise=matches_data['winner'].value_counts().values
team_name=matches_data['winner'].value_counts().index
obj_bar_plot.barplotseaborn(team_name,total_team_wise,'IPL Team Name','Numbers Of matches Won','No of IPL Matches Won Team-wise')

#Top 10 Batsmen with most runs
Striker_details=deliveries_data.groupby('batsman').sum().sort_values(by=['batsman_runs'], ascending=False)[:10]
Striker_run_details=Striker_details['batsman_runs']
obj_bar_plot.barplotseaborn(Striker_run_details.index,Striker_run_details.values,'Batsmen_Name','Runs Scored','Top 10 Batsmen with most runs')

#Top 10 Wicket takers
deliveries_data_dismissal=deliveries_data['dismissal_kind'].dropna()
dismissal_Kind=deliveries_data_dismissal[~deliveries_data_dismissal.str.contains('r')].unique().tolist()
dismissal_bowler_tot=deliveries_data[deliveries_data["dismissal_kind"].isin(dismissal_Kind)]
obj_bar_plot.barplotseaborn(dismissal_bowler_tot['bowler'].value_counts().index[0:10],dismissal_bowler_tot['bowler'].value_counts().values[0:10],'Bowler_Name','Total Wickets','Top 10 Wicket takers')

# Most dismissal Batsman vs Bowler
most_dismissal_bowler=dismissal_bowler_tot.groupby(['bowler','batsman']).count().sort_values(by='inning',ascending=False)[0:10]
most_dis=most_dismissal_bowler['inning'].reset_index()
plt.figure(figsize=(15, 7))
out1=sns.regplot(data=most_dis, x="bowler", y="inning", fit_reg=False, marker="o", color="skyblue", scatter_kws={'s':400})
for line in range(0,most_dis.shape[0]):
    out1.text(most_dis.bowler[line], most_dis.inning[line], most_dis.batsman[line], horizontalalignment='left', size='medium', color='black', weight='semibold')
plt.show()

# top 10 highest innings total
mergeddata=matches_data.merge(deliveries_data,left_on='id', right_on='match_id', how='left')
tot_runs_innings=mergeddata.groupby(['id','match_id','season','inning','batting_team']).sum().sort_values(by='total_runs',ascending=False)
top_highest_runs=tot_runs_innings['total_runs'].reset_index()[:10] 
plt.figure(figsize=(15, 7))
out2=sns.regplot(data=top_highest_runs, x='batting_team',y='total_runs', fit_reg=False, marker='o', color='green', scatter_kws={'s':400})
tot_val3=top_highest_runs.reset_index()
for high_val in range(0,top_highest_runs.shape[0]):
    out2.text(top_highest_runs.batting_team[high_val],top_highest_runs.total_runs[high_val],top_highest_runs.total_runs[high_val], horizontalalignment='left', size='medium', color='red', weight='semibold')
plt.show()

#Toss Decision
total_toss_decision=matches_data['toss_decision'].value_counts().values
toss_type=matches_data['toss_decision'].value_counts().index
obj_bar_plot.pie_graph(total_toss_decision,toss_type)
