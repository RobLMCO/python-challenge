


import os #  to modify path (regardless of OS type)
csvpath = os.path.join("..", "Resources", "election_data.csv")
import csv

csvHeaderList = ["Voter ID", "County", "Candidate"]

       
def file_to_collection(vcfFile):
    collection = []  # This will hold every dict per row
    votecount = 0
    with open(vcfFile , newline="", encoding="utf-8") as file:
        for arow in csv.reader(file , delimiter = ","):
            if "#" in arow[0]:
                continue  # this ignores the first line, it's okay
            collection.append({arow[0]: arow[1:]})
            votecount = votecount + 1
    print(f'Total Votes: {votecount - 1}')
    return collection



print("Election Results")
print("-------------------------")
voting = file_to_collection(csvpath)
print("-------------------------")
candidatenames = []
candidates = []
n = 0
TotalVotes = 0
from collections import Counter
for name in voting:
    for x in sorted(Counter(name).items()):
        TotalVotes = TotalVotes + 1
        candidates.append(x[1][1])
#print(TotalVotes - 1)        
#print(candidates)
from  more_itertools import unique_everseen
candidatenames = list(unique_everseen(candidates))
#print(candidatenames)
candidatecount = len(candidatenames)
#print(f"There are {candidatecount} candidates")
from collections import defaultdict
results = dict()
for i in candidatenames:
    for j in candidates:
        results[i] = results.get(i, 0) + j.count(i)

n = 1
WinnerTally = 0
WinnerName = ""
#print(results)
while n < candidatecount:
    print(f"{candidatenames[n]}: {int(results[candidatenames[n]])/(TotalVotes-1)*100}% ({results[candidatenames[n]]})")
    if results[candidatenames[n]] >> WinnerTally:
        WinnerTally = results[candidatenames[n]]
        WinnerName = candidatenames[n]
    n = n + 1
print("-------------------------")
print(f"Winner: {WinnerName}")
print("-------------------------")







  



  

