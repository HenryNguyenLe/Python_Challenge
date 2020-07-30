
import os
import csv
import operator


# define colors for 
red = '\033[31m'
grn = '\033[32m'
blu = '\033[34m'
yel = '\033[33m'
nc = '\033[30m'
bolt = '\033[1m'

# create the path to raw election data
# use os path to eliminate issue with 'slash' btw different os 
election_csv = os.path.join('Resources','houston_election_data.csv')


# create empty lists to store data while looping
candidate_list = []   # list to store all candidate's names
candidate_vote_count = []   # list to store numbers of votes 
total_votes = 0  # initial value of total votes is "zero"


# build pipeline to the csv file
with open(election_csv, 'r', newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # looping to read all candidate's names and voted times
    for row in csvreader:
        
        # count total votes = total rows in the table
        total_votes += 1   # each row contribute to 1-count
        
        # read candidate's name in each of the row list, index = 0
        candidate_name = (row[0])
        
        # conditional count how many times candidate's name appears in the candidate list
        if candidate_name in candidate_list:
            candidate_index = candidate_list.index(candidate_name)
            candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
        else:
            #if candidate's name is read the first time, add to list and count 1 
            candidate_list.append(candidate_name)
            candidate_vote_count.append(1)
        unsorted_candidate_dict = dict(zip(candidate_list,candidate_vote_count))
          
            
#  Calculate the percentage of votes each candidate won and make a list of all percentages
perc_list = []  # empty list to store vote percentage of each candidate
for each_candidate in range(len(candidate_list)):
    vote_perc = round (candidate_vote_count[each_candidate] / total_votes * 100, 2)
    perc_list.append (vote_perc)
    

# sorted dictionary from large to small based on vote numbers
sorted_candidate_list = sorted(unsorted_candidate_dict.items(), key=operator.itemgetter(1),reverse=True)
sorted_candidate_dict = dict (sorted_candidate_list)



# Split sorted dictionary into 3 lists
sorted_candidate_name = list(sorted_candidate_dict.keys())  # Candidate names
sorted_vote_perc = list(sorted(perc_list,reverse=True))     # Candidate's vote percentage
sorted_vote_count = list(sorted_candidate_dict.values())    # Candidate's number of votes



# find the names of 1st and 2nd winners
first_place_candidate = list(sorted_candidate_dict.keys())[0]
second_place_candidate = list(sorted_candidate_dict.keys())[1]

# print terminal headers
print('-------------------------------------------------')
print('-------------------------------------------------')
print('')
print(f'Author: {red}{bolt}Henry Le{nc}')
print('')
print('-------------------------------------------------')
print('-------------------------------------------------')
print(f'{bolt}Houston Mayoral Election Results{nc}')
print('-------------------------------------------------')

# print the total number of votes cast 
print(f'Total Cast Votes: {yel}{"{:,.0f}".format(total_votes)}{nc}')
print('-------------------------------------------------')


# print a complete list of candidates who received votes
# print the percentage of votes each candidate won
# print the total number of votes each candidate won
for each_name in range(len(sorted_candidate_name)):
    print(f'{sorted_candidate_name[each_name]} : {sorted_vote_perc[each_name]}% ({"{:,.0f}".format(sorted_vote_count[each_name])})')

    
# print the names of the two candidates who will advance to the runoff election.
print('-------------------------------------------------')
print(f'1st Advancing Candidate:  {grn}{first_place_candidate}{nc}')
print(f'2nd Advancing Candidate:  {blu}{second_place_candidate}{nc}')
print('-------------------------------------------------')
print('=================================================\n')
print(f'============  {bolt}THE END OF THIS REPORT{nc}  ===========\n')
print('=================================================\n')

# export a txt file with the results
output_path = os.path.join('Houston_Mayoral_Election_Results.txt')
with open(output_path, "w", newline="") as outputfile:
    outputfile.write('-------------------------------------------------\n')
    outputfile.write('-------------------------------------------------\n')
    outputfile.write('\n')
    outputfile.write('Author: Henry Le')
    outputfile.write('\n')
    outputfile.write('-------------------------------------------------\n')
    outputfile.write('-------------------------------------------------\n')
    outputfile.write('Houston Mayoral Election Results \n')
    outputfile.write('-------------------------------------------------\n')
    outputfile.write(f'Total Cast Votes: {total_votes} \n')
    outputfile.write('-------------------------------------------------\n')
    outputfile.write('\n')
    for ea_cand in range(len(candidate_list)):
        outputfile.write(f'{sorted_candidate_name[ea_cand]} : {sorted_vote_perc[ea_cand]}% ({sorted_vote_count[ea_cand]})\n')
    outputfile.write('\n')
    outputfile.write('-------------------------------------------------\n')
    outputfile.write('\n')
    outputfile.write(f'1st Advancing Candidate:  {first_place_candidate}\n')
    outputfile.write(f'2nd Advancing Candidate:  {second_place_candidate}\n')
    outputfile.write('\n')
    outputfile.write('-------------------------------------------------\n')
    outputfile.write('\n')

    outputfile.write('=================================================\n')
    outputfile.write('============  THE END OF THIS REPORT  ===========\n')
    outputfile.write('=================================================\n')
    
