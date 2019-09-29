import os
import csv

csvreader = os.path.join("election_data.csv")
#List to capture the names of candidates
candidates = []
# List to capture the votes each candidate recieves
count_votes = []
# List to capture the % of total votes for each candidate
percent_votes = []

# A counter for the total number of votes 
total_votes = 0

with open(csvreader, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Add to vote counter for each row
        total_votes += 1 

        #If candidate is not in the list yet: then add their name and a vote
        #If candidate is in the list add a vote 
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            count_votes.append(1)
        else:
            index = candidates.index(row[2])
            count_votes[index] += 1
    
    # Add to percent_votes list 
    for votes in count_votes:
        vote_percentage = (votes/total_votes) * 100
        vote_percentage = round(vote_percentage)
        vote_percentage = "%.3f%%" % vote_percentage
        percent_votes.append(vote_percentage)
    
    # Calculate the winner
    winner = max(count_votes)
    index = count_votes.index(winner)
    winning_candidate = candidates[index]

# Displaying results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {percent_votes[i]} ({count_votes[i]})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Exporting to .txt file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = (f"Total Votes: {total_votes}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {percent_votes[i]} ({count_votes[i]})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))  