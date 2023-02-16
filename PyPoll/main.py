#dependencies
import pandas as pd
import numpy as np

#create a reference for the CSV file
df=pd.read_csv('Resources/election_data.csv')

#printing the text to format the results
print('Election Results')
print(" ")
print("----------------------------------")
print("  ")

#finding the total votes and printing the results
total_votes=df['Ballot ID'].nunique()
print("Total Votes:   ",total_votes)
print("  ")
print("-----------------------------------")

#looping through the data to extract the number of votes for each candidate
data=df.groupby(['Candidate']).count()
#calculating the percentage
data['percentage']=round((data['Ballot ID']/total_votes)*100,3)
data=data.reset_index()
#finding the maximum value to see who the winner is with a for loop
Max=data['percentage'].max()
d=data.to_numpy().tolist()
winner=''
for i in range(0,len(d)):
    print("")
    if d[i][3]==Max:
        winner=d[i][0]
    print("{}: {}% ({})".format(d[i][0],d[i][3],d[i][1]))

#printing the winner's name    
print("   ")
print("-----------------------------------")
print("  ")
print("Winner : {}  ".format(winner))
print("   ")
print("-----------------------------------")

#creating the new text file with the result printed out
import sys
sys.stdout = open('analysis/output.txt', 'wt')
print('Election Results')
print(" ")
print("----------------------------------")
print("  ")
print("Total Votes:   ",total_votes)
print("  ")
print("-----------------------------------")
for i in range(0,len(d)):
    print("")
    if d[i][3]==Max:
        winner=d[i][0]
    print("{}: {}% ({})".format(d[i][0],d[i][3],d[i][1]))    
print("   ")
print("-----------------------------------")
print("  ")
print("Winner : {}  ".format(winner))
print("   ")
print("-----------------------------------")
