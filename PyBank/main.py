import os
import csv
import datetime
#Creating an object out of the CSV file
csvreader = os.path.join("budget_data.csv")

total_months = 0
net_profit = 0
value = 0
profit_change = 0
date_holder = []
profits = []

#Open and run th csv file
with open(csvreader, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading in the header row
    csv_header = next(csvreader)

    #Reading the first row- we can't calculate changes in profit on this
    first_row = next(csvreader)
    total_months += 1
    net_profit += int(first_row[1])
    value = int(first_row[1])
    
    #Going through each row of data after the header & first row 
    for row in csvreader:
        # Keeping track of date
        date_holder.append(row[0])
        # Calculate the change in profit and adding it to the list of profits
        profit_change = int(row[1])-value
        profits.append(profit_change)
        value = int(row[1])
        #Total number of months
        total_months += 1
        #Total net amount of "Profit/Losses over entire period"
        net_profit = net_profit + int(row[1])

    #Calculating the greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = date_holder[greatest_index]

    #Calculating the greatest decrease in profits
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = date_holder[worst_index]

    #Calculating average change in profits = profits / number of months
    avg_change = sum(profits)/len(profits)
    

#Print the Financial Analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${round(avg_change,2)}")
print(f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {worst_date} (${greatest_decrease})")
#Exporting to .txt file
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "----------------------------"
line3 = (f"Total Months: {total_months}")
line4 = (f"Total: ${net_profit}")
line5 = (f"Average Change: ${round(avg_change,2)}")
line6 = (f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})")
line7 = (f"Greatest Decrease in Profits: {worst_date} (${greatest_decrease})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))

