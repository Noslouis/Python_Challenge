#dependencies
import pandas as pd
import numpy as np

#produce a reference for the CSV file
df=pd.read_csv('Resources/election_data.csv')

#to print the text to format the results
print('Election Results')
print(" ")
print("----------------------------------")
print("  ")

#determining the total votes and printing the results
total_votes=df['Ballot ID'].nunique()
print("Total Votes:   ",total_votes)
print("  ")
print("-----------------------------------")

#looping through the data in order to pull out the number of votes for each candidate
data=df.groupby(['Candidate']).count()
#computing the percentage
data['percentage']=round((data['Ballot ID']/total_votes)*100,3)
data=data.reset_index()
#determining the maximum value to see who the winner is using a for loop
Max=data['percentage'].max()
d=data.to_numpy().tolist()
winner=''
for i in range(0,len(d)):
    print("")
    if d[i][3]==Max:
        winner=d[i][0]
    print("{}: {}% ({})".format(d[i][0],d[i][3],d[i][1]))

#to print the winner's name    
print("   ")
print("-----------------------------------")
print("  ")
print("Winner : {}  ".format(winner))
print("   ")
print("-----------------------------------")

#determiningg the new text file using the result printed out
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
