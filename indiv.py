import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

df0=pd.read_csv('agents.csv')
df0.head()

df1=pd.read_csv('clutches.csv')
df1.head()

df2=pd.read_csv('other.csv')
df2.head()

import plotly.graph_objects as go
import plotly.figure_factory as ff
plt.style.use('dark_background')
fig = ff.create_table(df0, height_constant=60)
agents = ['Jett', 'Reyna']
Wins = [15,4]
Matches = [18,4]
trace1 = go.Bar(x=agents, y=Wins, xaxis='x2', yaxis='y2',
                marker=dict(color='#0099ff'),
                name='Wins')
trace2 = go.Bar(x=agents, y=Matches, xaxis='x2', yaxis='y2',
                marker=dict(color='#404040'),
                name='Matches Played')
fig.add_traces([trace1, trace2])
fig['layout']['xaxis2'] = {}
fig['layout']['yaxis2'] = {}
fig.layout.yaxis.update({'domain': [0, .45]})
fig.layout.yaxis2.update({'domain': [.6, 1]})
fig.layout.yaxis2.update({'anchor': 'x2'})
fig.layout.xaxis2.update({'anchor': 'y2'})
fig.layout.yaxis2.update({'title': 'Matches'})
fig.layout.margin.update({'t':75, 'l':50})
fig.layout.update({'title': 'Agent Pick Comparison'})
fig.layout.update({'height':800})
fig.show()

import pandas as pd
import plotly.graph_objects as go

fig = go.Figure(go.Scatter(x = df1['Ign'], y = df1['Percentage'],
                  name='Clutch %'))

fig.update_layout(title='Total clutches(Since Masters Iceland)',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)

fig.show()

fig = px.scatter(df2, x='FB', y="FD",hover_name = 'Ign',
                 color = 'Ign',template = 'plotly_dark')

fig.update_traces(marker_line=dict(width=1, color='DarkSlateGray'))

fig.show()



import plotly.graph_objects as go

Ign = ['t3xture','BuzZ','allow','Meteor','fiveK']
KPR = [95, 87, 93, 84, 85]
fig = go.Figure(data=[go.Pie(labels=Ign, values=KPR, hole=.3)])
fig.layout.update({'title': 'Kills Per Round'})
fig.update_traces(marker_line=dict(width=1, color='DarkSlateGray'))
fig.show()
