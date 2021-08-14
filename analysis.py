import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('master.csv')
df.head()



plt.style.use('dark_background')
fig = px.scatter(df, x='Headshots', y="Kills",hover_name = 'Ign',
                 color = 'Team',template = 'plotly_dark')

fig.update_traces(marker_line=dict(width=1, color='DarkSlateGray'))

fig.show()


fig = px.scatter(df, x='Matches', y="Acs",hover_name = 'Ign',
                 color = 'Team',template = 'plotly_dark')

fig.update_traces(marker_line=dict(width=1, color='DarkSlateGray'))

fig.show()



fig = px.scatter(df, x='Matches', y="Kd",hover_name = 'Ign',
                 color = 'Team',template = 'plotly_dark')

fig.update_traces(marker_line=dict(width=1, color='DarkSlateGray'))

fig.show()




import matplotlib.pyplot as plt

fig=px.bar(df, x="Kills", y="Ign",color="Multikills")
plt.style.use('grayscale')

fig.show()
