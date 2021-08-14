import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt

acsscore = pd.read_csv('acs.csv')
acsscore.head()
kdd = pd.read_csv('kd.csv')
kdd.head()

multi = pd.read_csv('multi.csv')
multi.head()

headshots = pd.read_csv('hsots.csv')
headshots.head()


damange = pd.read_csv('damange.csv')
damange.head()

output1 = pd.merge(acsscore, kdd,
                   on='Ign',
                   how='outer')

output1.head(26)



final=output1.drop(['Team_y'], axis=1)
final.head()

last = pd.merge(damange, final,
                   on='Ign',
                   how='outer')
last.head()

all= pd.merge(headshots, last,
                   on='Ign',
                   how='outer')
all.head()

all.drop(['Team_x'], axis=1)


multikills= pd.merge(all, multi,
                   on='Ign',
                   how='outer')
multikills.head()

multikills.drop(['Team_x','Team_y'], axis=1)
multikills.to_csv('master.csv')
