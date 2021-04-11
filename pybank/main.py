# Modules
import os
import csv
csvpath = os.path.join("resources","budget_data.csv")
# print(csvpath)
# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    # Identify variables
    total_months = 0
    total_pl = 0
    average_pl =[]
    date = []
    pl_change =[]
    pl =[]
    #Starting for loop
    for row in csvreader:
        total_months = total_months + 1
        total_pl = total_pl + int(row[1])
        pl.append(row[1])
        date.append(row[0])
    for row in range(1,len(pl)):
        pl_change.append(int(pl[row])-int(pl[row-1]))
    average_pl = sum(pl_change)/len(pl_change)   
    print(average_pl)
    max_increase = max(pl_change)
    min_decrease = min(pl_change)
    max_date = date[pl_change.index(max_increase)+1]
    min_date = date[pl_change.index(min_decrease)+1]
