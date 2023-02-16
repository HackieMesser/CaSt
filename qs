#1) On average, how many cups of coffee are bought per order?
#data.loc[data['Pclass']==1,'Age'].mean() put 1 in '' for category

data['Age'].mean()

#2) Who are the top 10% most valuable customers (in terms of revenue)?
data2=data.groupby('Age')['Age'].sum()
data2
#https://sparkbyexamples.com/pandas/pandas-groupby-sum-examples/     
#3) What is average CLV (Customer Lifetime Value - sum of all revenue from customer) of
#customers with subscription and without? Please visualize with a chart of your choice.
data.groupby('Sex')['Age','Fare'].mean().plot.bar()
