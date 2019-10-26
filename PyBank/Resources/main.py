#Print Financial Analysis
print ("Financial Analysis")
print ("----------------------------")

# Modules
import os
import csv
total = 0

# Set path for file
csvpath = os.path.join("budget_data.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#total number of months
    rowcount = len(list(csvreader)) - 1
print ("Total Months: "+str(rowcount))

#net total amount
total = 0
date = []
profitloss = []
change = []
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        total += int(row[1])
        profitloss.append(float(row[1]))
        date.append(row[0])
    print ("Total: $" + str(total))
#Average of the changes in Profit/Losses
    for i in range(1,len(profitloss)):
        change.append(profitloss[i]-profitloss[i-1])
    avgchange = sum(change)/len(change)
    print ("Average Change: $" + str(round(avgchange,2)))
    maxchange = round(max(change))
    minchange = round(min(change))
    maxindex = change.index(maxchange)+1
    minindex = change.index(minchange)+1
    maxdate =  date[maxindex]
    mindate = date[minindex]
    print("Greatest Increase in Profits: "+ str(maxdate) + " ("+str(maxchange)+")")
    print("Greatest Decrease in Profits: "+ str(mindate)+ " ("+str(minchange)+")")