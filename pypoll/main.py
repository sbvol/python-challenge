#Completing the initial imports
import os
import csv

#Building links to files and their locations
election_data1 = os.path.join('../pythonstuff/election_data_1.csv')
election_data2 = os.path.join('../pythonstuff/election_data_2.csv')

#Creating all of my variables
voter_id = []
county_name = []
candidate_table = []
saved_list = []
number_votes = []
set_candidates = set()
list_candidates = []
percent_votes = []
max_vote = 0
total_number_votes = 0
vote_count = 0

#Reading files
with open(election_data1, newline="") as csvfile1:
    csvreader = csv.reader(csvfile1, delimiter=",")
    next(csvreader, None)
    
    for row in csvfile1:
        row_current = row.split(",")
        voter_id.append(row_current[0])
        county_name.append(row_current[1])
        candidate_table.append(row_current[2])

with open(election_data2, newline="") as csvfile1:
    csvreader = csv.reader(csvfile1, delimiter=",")
    next(csvreader, None)
    
    for row in csvfile1:
        row_current = row.split(",")
        voter_id.append(row_current[0])
        county_name.append(row_current[1])
        candidate_table.append(row_current[2])

#Calculating the total number of votes
total_number_votes = int(len(voter_id))

#Building a list of unique candidates using the set function
for name in candidate_table:
    set_candidates.add(name)

#Converting my set back to a list because sets and loops don't mix
list_candidates = list(set_candidates)

#Looping thru the list of candidates to gather total votes per candidate info
#Calculating percentage of total information
for name in list_candidates:
    vote_count = candidate_table.count(name)
    if vote_count > max_vote:
        max_vote = vote_count
        save_winner = name
    percent_of_vote = int(vote_count) / int(total_number_votes)
    vote_count = str(vote_count)
    percent_of_vote = percent_of_vote * 100
    percent_of_vote = str("%.1f" % percent_of_vote)
    number_votes.append(vote_count)
    percent_votes.append(percent_of_vote)

#Removing \n syntax from each list string...to make the output more pleasing to the eyeball
list_candidates[0] = list_candidates[0].strip()
list_candidates[1] = list_candidates[1].strip()
list_candidates[2] = list_candidates[2].strip()
list_candidates[3] = list_candidates[3].strip()
list_candidates[4] = list_candidates[4].strip()
list_candidates[5] = list_candidates[5].strip()
list_candidates[6] = list_candidates[6].strip()
list_candidates[7] = list_candidates[7].strip()
list_candidates[8] = list_candidates[8].strip()
list_candidates[9] = list_candidates[9].strip()

#Formatting the output for the screen
print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(total_number_votes))
print("-------------------------------------")
print(list_candidates[0], ": " + percent_votes[0] + "% " + "(" + number_votes[0] + ")")
print(list_candidates[1], ": " + percent_votes[1] + "% " + "(" + number_votes[1] + ")")
print(list_candidates[2], ": " + percent_votes[2] + "% " + "(" + number_votes[2] + ")")
print(list_candidates[3], ": " + percent_votes[3] + "% " + "(" + number_votes[3] + ")")
print(list_candidates[4], ": " + percent_votes[4] + "% " + "(" + number_votes[4] + ")")
print(list_candidates[5], ": " + percent_votes[5] + "% " + "(" + number_votes[5] + ")")
print(list_candidates[6], ": " + percent_votes[6] + "% " + "(" + number_votes[6] + ")")
print(list_candidates[7], ": " + percent_votes[7] + "% " + "(" + number_votes[7] + ")")
print(list_candidates[8], ": " + percent_votes[8] + "% " + "(" + number_votes[8] + ")")
print(list_candidates[9], ": " + percent_votes[9] + "% " + "(" + number_votes[9] + ")")
print("-------------------------------------")
print("Winner: " + save_winner)
print("-------------------------------------")

#Formating the output for the output file
output_path = os.path.join('../pythonstuff/output', 'election_analysis.csv')

with open(output_path, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------------------"])
    csvwriter.writerow(["Total Votes: " + str(total_number_votes)])
    csvwriter.writerow(["-------------------------------------"])
    csvwriter.writerow([list_candidates[0], ": " + percent_votes[0] + "% " + "(" + number_votes[0] + ")"])
    csvwriter.writerow([list_candidates[1], ": " + percent_votes[1] + "% " + "(" + number_votes[1] + ")"])
    csvwriter.writerow([list_candidates[2], ": " + percent_votes[2] + "% " + "(" + number_votes[2] + ")"])
    csvwriter.writerow([list_candidates[3], ": " + percent_votes[3] + "% " + "(" + number_votes[3] + ")"])
    csvwriter.writerow([list_candidates[4], ": " + percent_votes[4] + "% " + "(" + number_votes[4] + ")"])
    csvwriter.writerow([list_candidates[5], ": " + percent_votes[5] + "% " + "(" + number_votes[5] + ")"])
    csvwriter.writerow([list_candidates[6], ": " + percent_votes[6] + "% " + "(" + number_votes[6] + ")"])
    csvwriter.writerow([list_candidates[7], ": " + percent_votes[7] + "% " + "(" + number_votes[7] + ")"])
    csvwriter.writerow([list_candidates[8], ": " + percent_votes[8] + "% " + "(" + number_votes[8] + ")"])
    csvwriter.writerow([list_candidates[9], ": " + percent_votes[9] + "% " + "(" + number_votes[9] + ")"])
    csvwriter.writerow(["-------------------------------------"])
    csvwriter.writerow(["Winner: " + save_winner])
    csvwriter.writerow(["-------------------------------------"])

