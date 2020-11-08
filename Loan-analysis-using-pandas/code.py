# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank = pd.read_csv(path)

categorical_var = bank.select_dtypes(exclude = 'number')
print(categorical_var)
categorical_var.shape
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)
numerical_var.shape

banks = bank.drop(['Loan_ID'], axis = 1)
print(banks.isnull().sum())
bank_mode = banks.mode().iloc[0]
banks = banks.fillna(bank_mode)
print(banks.isnull().sum())
print(banks.shape)

avg_loan_amount = bank.pivot_table(index = ['Gender', 'Married', 'Self_Employed'],values = 'LoanAmount',aggfunc='mean')
avg_loan_amount

loan_approved_se = banks.loc[(banks["Self_Employed"]=="Yes")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
loan_approved_nse = banks.loc[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y'),["Loan_Status"]].count()
ls = bank['Loan_Status'].count()
percentage_se = (loan_approved_se/ls)*100
percentage_nse = (loan_approved_nse/ls)*100

banks['Loan_Amount_Term'] = banks['Loan_Amount_Term']/12
big_loan_term = banks[banks["Loan_Amount_Term"] >=25]
len(big_loan_term)

columns_to_show = ['ApplicantIncome', 'Credit_History']
 
loan_groupby=banks.groupby(['Loan_Status'])

loan_groupby=loan_groupby[columns_to_show]

# Check the mean value 
mean_values=loan_groupby.agg([np.mean])

print(mean_values)




