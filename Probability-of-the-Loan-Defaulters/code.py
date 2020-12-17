# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

p_a = len(df[df['fico'] > 700])/len(df)
p_b = len(df[df['purpose'] == 'debt_consolidation'])/len(df)

# Given debt consolidation probability of fico being greater than 700 p(a/b)
df1 = df[df['purpose'] == 'debt_consolidation']
p_b_a = len(df1[df1['fico']> 700])/len(df1)

# Given fico being greater than 700 probability of debt consolidation p(b/a)
df2 = df[df['fico'] > 700]
p_a_b = len(df2[df2['purpose'] == 'debt_consolidation'])/len(df2)

prob_lp = len(df[df['paid.back.loan']== 'Yes'])/len(df)
prob_cs = len(df[df['credit.policy']== 'Yes'])/len(df)

new_df = df[df['paid.back.loan']== 'Yes']
prob_pd_cs = len(new_df[new_df['credit.policy'] == 'Yes'])/len(new_df)
bayes = round((prob_pd_cs*prob_lp)/prob_cs,4)
bayes

da = df['purpose'].value_counts()
plt.bar(da.index,da)
plt.xticks(rotation = 45)
plt.show()

df1 = df[df['paid.back.loan']=='No']
db = df1['purpose'].value_counts()
plt.bar(db.index,db)
plt.xticks(rotation = 45)
plt.show()

inst_median = df['installment'].median()
inst_mean = df['installment'].mean()

plt.hist(df['installment'])    
plt.show()

plt.hist(df['log.annual.inc'])    
plt.show()


