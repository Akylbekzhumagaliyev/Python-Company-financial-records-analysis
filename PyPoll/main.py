import os
import csv
from collections import defaultdict, Counter

election_csv_path = os.path.join("..", "PyPoll", "election_data.csv")

with open(election_csv_path, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    print("Election Results")
    print("-"*30)

    num_row = len(list(csvfile))
    print("Total votes:", num_row)
    print("-"*30)

    candidates = []
    votes_count = 0

with open(election_csv_path, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csv_reader:
        candidate = row[2]
        if candidate in candidates:
            votes_count = votes_count + 1
        else: candidates.append(row[2])


with open(election_csv_path, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    votes_Khan = 0
    votes_Correy = 0
    votes_Li = 0
    votes_OTooley = 0

    for row in csv_reader:
        if row[2] == "Khan":
            votes_Khan = votes_Khan + 1
        if row[2] == "Correy":
            votes_Correy = votes_Correy + 1 
        if row[2] == "Li":
            votes_Li = votes_Li + 1
        if row[2] == "O'Tooley":
            votes_OTooley = votes_OTooley + 1            
    all_votes = [votes_Khan,votes_Correy,votes_Li,votes_OTooley]

    percent_Khan = votes_Khan/num_row*100
    percent_Correy = votes_Correy/num_row*100
    percent_Li = votes_Li/num_row*100
    percent_OTooley = votes_OTooley/num_row*100

print("Khan: "+'{:,.2f}'.format(percent_Khan)+"%", "("+str(votes_Khan)+")")
print("Correy: "+'{:,.2f}'.format(percent_Correy)+"%", "("+str(votes_Correy)+")")
print("Li: "+'{:,.2f}'.format(percent_Li)+"%", "("+str(votes_Li)+")")
print("O'Tooley: "+'{:,.2f}'.format(percent_OTooley)+"%", "("+str(votes_OTooley)+")")

with open(election_csv_path, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for i in range(1,len(all_votes)):        
        winner = max(all_votes)  
        maxname = str(candidates[all_votes.index(max(all_votes))])
    print("-"*30)
    print("Winner: ",maxname)
    print("-"*30)    

with open("results.txt",'w') as extract:
    print("Election Results",file=extract)
    print("-"*30,file=extract) 
    print("Total votes:", num_row,file=extract)
    print("-"*30,file=extract)
    print("Khan: "+'{:,.2f}'.format(percent_Khan)+"%", "("+str(votes_Khan)+")",file=extract)
    print("Correy: "+'{:,.2f}'.format(percent_Correy)+"%", "("+str(votes_Correy)+")",file=extract)
    print("Li: "+'{:,.2f}'.format(percent_Li)+"%", "("+str(votes_Li)+")",file=extract)
    print("O'Tooley: "+'{:,.2f}'.format(percent_OTooley)+"%", "("+str(votes_OTooley)+")",file=extract)
    print("-"*30,file=extract)
    print("Winner: ",maxname,file=extract)
    print("-"*30,file=extract)