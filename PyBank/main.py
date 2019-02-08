import os #  to modify path (regardless of OS type)
csvpath = os.path.join("..", "Resources", "budget_data.csv")
import csv

csvHeaderList = ["Date", "Profit/Losses", "Change"]

# Define Variables

myMonthList = []
myBalanceList = []
myAverageList = []

TotalMonths = 0
FinalBalance = 0
SumDifferences = 0
AverageChange = 0

MaxDate = ""
MinDate = ""
MaxProfit = 0
MinProfit = 0

# Open the CSV using encoding="utf8"
with open(csvpath, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_HeaderRow = next(csvreader)
   
    
    # Build lists of the months and balances, calculate the final balance, sum of differences, and the Max/Min profits

    for row in csvreader:
        myMonthList.append(row[0])
        myBalanceList.append(row[1])
        FinalBalance = FinalBalance + int(row[1])
        change = int(myBalanceList[int(len(myBalanceList)) - 1]) - int(myBalanceList[int(len(myBalanceList)) - 2])
        myAverageList.append(change)
        SumDifferences = SumDifferences + change
        if change > MaxProfit:
            MaxProfit = change
            MaxDate = row[0]
        if change < MinProfit:
            MinProfit = change
            MinDate = row[0]
        
        
        
# Calculate the Average Change         
TotalMonths = len(myMonthList)
AverageChange = SumDifferences / (len(myAverageList) - 1)

# Output the results
print("Financial Analysis")
print("----------------------------")
print("Total Months: {}".format(TotalMonths))
print("Total: ${}".format(FinalBalance))
print("Average Change: ${:0.2f}".format(AverageChange))
#print("Sum of Averages: ${}".format(SumAverages))
print("Greatest Increase in Profits: {} (${})".format(MaxDate, MaxProfit))
print("Greatest Decrease in Profits: {} (${})".format(MinDate, MinProfit))


# save the output file path
output_txt_file = os.path.join("PyBank.txt")

# open the output text file and then write the summary
with open(output_txt_file, "w") as textfile:
    textfile.writelines("Financial Analysis \n")
    textfile.writelines("---------------------------- \n")
    textfile.writelines("Total Months: {} \n".format(TotalMonths))
    textfile.writelines("Total: ${} \n".format(FinalBalance))
    textfile.writelines("Average Change: ${:0.2f} \n".format(AverageChange))
    textfile.writelines("Greatest Increase in Profits: {} (${}) \n".format(MaxDate, MaxProfit))
    textfile.writelines("Greatest Decrease in Profits: {} (${}) \n".format(MinDate, MinProfit))
    textfile.close()

# Zip all three lists together into tuples
roster = zip(myMonthList, myBalanceList, myAverageList)


# save the output file path
output_csv_file = os.path.join("PyBank.csv")

# open the output csv file, create a header row, and then write the zipped object to the csv
with open(output_csv_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(csvHeaderList)

    writer.writerows(roster)


for title in roster:
    print(title)

