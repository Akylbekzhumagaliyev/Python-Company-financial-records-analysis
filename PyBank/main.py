import os
import csv

budget_csv_path = os.path.join("..", "PyBank", "budget_data.csv")

with open(budget_csv_path, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    print("Financial analysis")
    print("-"*30)
    
    num_row = len(list(csvfile))
    print("Total months:", num_row)

with open(budget_csv_path, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)    

    total = 0
    for row in csv_reader:
        total += int(row[1])
    print ("Total:",'${:,}'.format(total))

with open(budget_csv_path, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    all_rows = csvfile.readlines()

    changes_list = []
    range_list = []

    for row in all_rows[0:]:
        row = row.strip("\n")
        range_list.append(row.split(","))
        
    for row, change in enumerate(range_list[1:]):
        changes_list.append(int(change[1])-int(range_list[row][1]))
    average = sum(changes_list)/len(changes_list)
 
    print("Average:",'${:,.2f}'.format(average))
    
with open(budget_csv_path, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    profits = [0]
    months = []
    changes_list = []

    for row in csv_reader:
        profits.append(int(row[1]))
        months.append(row[0])
        
    for i in range(1,len(profits)):
        changes_list.append(profits[i] - profits[i-1])
        maxchange = max(changes_list)
        minchange = min(changes_list)

        maxchangemonth = str(months[changes_list.index(max(changes_list))])
        minchangemonth = str(months[changes_list.index(min(changes_list))])


    print("Greatest Increase in Profits:", maxchangemonth,"("+'${:,}'.format(maxchange)+")")
    print("Greatest Decrease in Profits:", minchangemonth,"("+'${:,}'.format(minchange)+")")

with open("results.txt",'w') as extract:
    print("Financial analysis",file=extract)
    print("-"*30,file=extract)    
    print("Total months:", num_row,file=extract)
    print("Total:",'${:,}'.format(total),file=extract)
    print("Average:",'${:,.2f}'.format(average),file=extract)
    print("Greatest Increase in Profits:", maxchangemonth,"("+'${:,}'.format(maxchange)+")",file=extract)
    print("Greatest Decrease in Profits:", minchangemonth,"("+'${:,}'.format(minchange)+")",file=extract)