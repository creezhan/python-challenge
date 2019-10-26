#Print Financial Analysis
print ("Election Results")
print ("----------------------------")

# Modules
import os
import csv
from collections import Counter
total = 0

# Set path for file
csvpath = os.path.join("election_data.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#total number of votes
    rowcount = len(list(csvreader)) - 1
print ("Total Votes: "+str(rowcount))
print ("----------------------------")

#list of candidates
votesCount = Counter()
candidates = []
percentage = []
winner = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        candidates.append(str(row[2]))
    for name in candidates:
        votesCount[name] += 1

names = tuple(votesCount.keys())
votes = tuple(votesCount.values())

for x in votes:
    percentage.append((int(x)/rowcount)*100)

# number of votes per candidate
for x in range(len(names)):
    print (str(names[x])+ ": "+ str(round(percentage[x],3)) +"% " + "(" + str(votes[x])+ ")")

#percentage of votes per candidate

print ("----------------------------")
#find winner
winner = names[0]
print ("Winner: " + str(winner) )
print ("----------------------------")