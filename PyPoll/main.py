


import os #  Modify path (regardless of OS type)
csvpath = os.path.join("..", "Resources", "election_data.csv")
import csv

csvHeaderList = ["Voter ID", "County", "Candidate"]

# Use a function store the poll data file to a collection and tally the total votes       
def file_to_collection(vcfFile):
    collection = []  
    votecount = 0
    with open(vcfFile , newline="", encoding="utf-8") as file:
        for arow in csv.reader(file , delimiter = ","):
            if "#" in arow[0]:
                continue  
            collection.append({arow[0]: arow[1:]})
            votecount = votecount + 1
    print(f'Total Votes: {votecount - 1}')
    return collection


# Save the output file path
output_txt_file = os.path.join("PyPoll.txt")

# Open the output text file and then write the summary
with open(output_txt_file, "w") as textfile:
    #print(results)
    print("Election Results")
    print("-------------------------")
    voting = file_to_collection(csvpath)
    print("-------------------------")

    candidatenames = []
    candidates = []
    n = 0
    TotalVotes = 0

    # Use the Counter method to add up the total votes in the collection of votes
    # We did this already in the function file to collection call 
    from collections import Counter
    for name in voting:
        for x in sorted(Counter(name).items()):
            TotalVotes = TotalVotes + 1
            candidates.append(x[1][1])
            
    #print(candidates)

    # Use an iterator method from the more_itertools module to make a list of the unique candidates
    from  more_itertools import unique_everseen
    candidatenames = list(unique_everseen(candidates))
    #print(candidatenames)
    # Count the number of candidates in the candidate list
    candidatecount = len(candidatenames)
    #print(f"There are {candidatecount} candidates")
    
    # Make a dictionary of the candidate names and tally all of thier votes as results
    from collections import defaultdict
    results = dict()
    for i in candidatenames:
        for j in candidates:
         results[i] = results.get(i, 0) + j.count(i)

    n = 1
    WinnerTally = 0
    WinnerName = ""

    textfile.writelines("Election Results \n")
    textfile.writelines("------------------------- \n")
    textfile.writelines("Total Votes: {} \n".format(TotalVotes - 1))   
    textfile.writelines("------------------------- \n")
    
    # Output each candidate result including vote percentage of overall poll
    while n < candidatecount:
        CandidateResult = ""
        CandidatePercentage = 0
        #print(f"{candidatenames[n]}: {int(results[candidatenames[n]])/(TotalVotes-1)*100}% ({results[candidatenames[n]]})")
        CandidatePercentage = round(results[candidatenames[n]]/(TotalVotes-1)*100, 2)
        CandidateResult = str(candidatenames[n] + ": " + str(CandidatePercentage) + "% (" + str(results[candidatenames[n]]) + ")")
        textfile.writelines("{} \n".format(CandidateResult)) 
        print(CandidateResult)

        # Find the winner
        if results[candidatenames[n]] >> WinnerTally:
           WinnerTally = results[candidatenames[n]]
           WinnerName = candidatenames[n]
        n = n + 1
    
    # Output the winner
    textfile.writelines("------------------------- \n")
    textfile.writelines("Winner: {} \n".format(WinnerName))
    textfile.writelines("------------------------- \n")
    print("-------------------------")
    print(f"Winner: {WinnerName}")
    print("-------------------------")
    textfile.close()










  



  

