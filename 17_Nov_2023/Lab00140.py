# csv - format

import csv

with open("Data1.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # print(row) # OP : All the data from "Data1.csv" file as list
        # print(row[0]) # OP : All the Names will print
        # print(row[1])  # OP : All the Age will print
        # print(row[2])  # OP : All the City will print

        print(row[0],row[1],row[2] ,sep='|')  # OP : All the items will be separated by |

        # print('|'.join(row)) # OP : All the data from "Data1.csv" file separated by |
