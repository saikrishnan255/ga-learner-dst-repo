# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file


loan_status = data['Loan_Status'].value_counts()
loan_status.plot(kind = 'bar')
plt.show()

property_and_loan = data.groupby(['Property_Area','Loan_Status'])
property_and_loan = property_and_loan.size().unstack()
property_and_loan.plot(kind = 'bar', stacked = False)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()

education_and_loan = data.groupby(['Education','Loan_Status'])[['Loan_Status']]
education_and_loan = education_and_loan.count().unstack()
education_and_loan.plot(kind = 'bar', stacked = True)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation = 45)
plt.show()

graduate = data[data['Education'] == 'Graduate']
not_graduate = data[data['Education'] == 'Not Graduate']
fig,(ax_1, ax_2) = plt.subplots(1,2, figsize = [12,6])
graduate['LoanAmount'].plot(kind = 'density', label = 'Graduate', ax = ax_1, title = 'Loan amount distribution for graduates')
not_graduate['LoanAmount'].plot(kind = 'density', label = 'Not Graduate', ax = ax_2, title = 'Loan amount Distribution for Non-Graduates')
plt.show()

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
fig,(ax_1, ax_2, ax_3) = plt.subplots(nrows = 3, ncols = 1, figsize = [6,10])
ax_1.scatter(x = data['ApplicantIncome'], y = data['LoanAmount'], )
ax_1.set(title = 'Applicant Income')
ax_2.scatter(x = data['CoapplicantIncome'], y = data['LoanAmount'], )
ax_2.set(title = 'Coapplicant Income')
ax_3.scatter(x = data['TotalIncome'], y = data['LoanAmount'], )
ax_3.set(title = 'Total Income')
plt.show()


#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 3
#Plotting a stacked bar plot




#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 4 
#Subsetting the dataframe based on 'Education' column


#Subsetting the dataframe based on 'Education' column


#Plotting density plot for 'Graduate'


#Plotting density plot for 'Graduate'


#For automatic legend display


# Step 5
#Setting up the subplots


#Plotting scatter plot


#Setting the subplot axis title


#Plotting scatter plot


#Setting the subplot axis title


#Creating a new column 'TotalIncome'


#Plotting scatter plot



#Setting the subplot axis title



