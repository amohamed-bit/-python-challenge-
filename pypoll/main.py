# Modules
import os
import csv
csvpath = os.path.join("resources","election_data.csv")
# print(csvpath)
# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    # Identify variables
    