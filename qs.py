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
#4) What are the top 3 best-selling (in terms of revenue) products in each article group? What
#share of orders contained these products?
data.sort_values('Age',ascending =False).groupby('Sex').head(3)
#What share of orders contained these products?
data.groupby(["Sex"])\
.agg({"Age" : "sum"})[["Age"]]\
.apply(lambda x: 100*x/x.sum())\
.sort_values(by="Age", ascending=False)

#https://www.codeforests.com/2020/07/18/calculate-percentage-within-group/

#6) What is the average revenue per customer by cohort? Please visualize with a chart of your
#choice. Which cohort has on average the most valuable, and which the least valuable
#customers? (Cohort is defined as ‘year’ e.g. if a customer has registered in January 2021, he
#belongs in the 2021 cohort.)
data3=data.groupby(['Survived', 'Pclass']).mean()
data3
fig, ax = plt.subplots(figsize=(15,7))
data3.groupby(['Survived','Pclass']).mean()['Siblings/Spouses Aboard'].unstack().plot(ax=ax)

