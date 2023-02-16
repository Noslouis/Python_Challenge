#dependencies
import pandas as pd
import numpy as np

#produce a reference for the CSV file
df=pd.read_csv('Resources/budget_data.csv')

#to print the text to format the results
print("Financial Analysis")
print("    ")
print("-------------------------------------------------------")
print("     ")

#values that are unique -> months
Total_months=df['Date'].nunique()
print("Total Months:   ",Total_months)
print("    ")

#computing the sum of the column of Profit/Losses 
Total=df['Profit/Losses'].sum()
print("Total:    $",Total)
print("    ")

#producing a list and computing the average with a for loop
lis=[]
d= df.to_numpy().tolist()
for i in range(0,len(d)-1):
    change=d[i+1][1]-d[i][1]
    lis.append(change)
change=round(sum(lis)/len(lis),2)
lis.insert(0,0)
#producing a new column to harbour the average values
df['Average change']=lis

#computing the greatest increase and decrease from that new column using a for loop
d=df.to_numpy().tolist()
max_change=df['Average change'].max()
min_change=df['Average change'].min()
min_date=""
max_date=""
for i in range(0,len(d)):
    if d[i][2]==max_change:
        max_date=d[i][0]
    elif d[i][2]==min_change:
        min_date=d[i][0]

#to print all the results out
print("")
print("Greatest Increase in profit : {} (${})".format(max_date,max_change))
print("")
print("Greatest Decrease in profit : {} (${})".format(min_date,min_change))
print(" ")

#producing the new text file using the result printed out
import sys
sys.stdout = open('analysis/output.txt', 'wt')
print("Financial Analysis")
print("    ")
print("-------------------------------------------------------")
print("     ")
Total_months=df['Date'].nunique()
print("Total Months:   ",Total_months)
print("    ")
Total=df['Profit/Losses'].sum()
print("Total:    $",Total)
print("    ")
print("Average Change: ${}".format(change))
print("  ")
print("")
print("Greatest Increase in profit : {} (${})".format(max_date,max_change))
print("")
print("Greatest Decrease in profit : {} (${})".format(min_date,min_change))
print(" ")
