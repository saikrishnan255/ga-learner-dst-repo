# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)

data['Gender'] = data['Gender'].replace('-','Agender')

align = data['Alignment'].value_counts()
plt.bar(align.index,align)
plt.show()

d = data[['Combat','Strength']].rank(axis = 0)
d['d^2'] = (d['Combat'] - d['Strength'])**2
d_square = d['d^2'].sum()
l = len(d['Combat'])

spearman = 1-((6*d_square)/(l*(l**2-1)))
print(spearman)

f = data[['Combat','Intelligence']].rank(axis = 0)
f['d^2'] = (f['Combat'] - f['Intelligence'])**2
f_square = f['d^2'].sum()
l = len(f['Combat'])

spearman = 1-((6*f_square)/(l*(l**2-1)))
print(spearman)

best = data[data['Total'] > data['Total'].quantile(0.99)]
super_best_names = list(best['Name'])



