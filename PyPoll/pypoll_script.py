# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

#This script is using the template file included in the "Module 3 Challenge" files.
#Credits for the baseline formatting of this script belong to whoever created this template file through the bootcamp course

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_Info_Tracker = {} # Dictionary that holds a candidate's name and a count of each vote they receive
unique_Candidates = [] # Tracker for each unique candidate name
temp_Candidate_Name = ""  # Temporary holder for a candidate's name to add to list of unique candidates

# Winning Candidate and Winning Count Tracker
winning_Candidate_Info = {"Name": "",
                          "Votes": 0}

# Open the CSV file and process it
with open(file_to_load, encoding='UTF-8') as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes = total_votes + 1

        # Get the candidate's name from the row
        temp_Candidate_Name = row[2]

        # If the candidate is not already in the candidate list, add their name to the unique candidate name tracker.
        # Also, add their name to the candidate info dictionary and initialize the value tied to their name to 0
        if temp_Candidate_Name not in unique_Candidates:
            unique_Candidates.append(temp_Candidate_Name)
            candidate_Info_Tracker[temp_Candidate_Name] = 0 
        
        # Add a vote to the candidate's count in their dictionary entry
        candidate_Info_Tracker[temp_Candidate_Name] = candidate_Info_Tracker[temp_Candidate_Name] + 1   

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the first 4 lines of results table (to terminal)
    print("")
    print("Election Results")
    print("")
    print("------------------------------------------------")
    print("")
    print(f'Total Votes: {total_votes}')
    print("")
    print("------------------------------------------------")
    print("")

    # Print the first 4 lines of results table to text file
    txt_file.write("Election Results" + "\n")
    txt_file.write("\n")
    txt_file.write("------------------------------------------------" + "\n")
    txt_file.write("\n")
    txt_file.write(f"Total Votes: {total_votes}" + "\n")
    txt_file.write("\n")
    txt_file.write("------------------------------------------------" + "\n")

    # Loop through the candidates in the candidate dictionary to determine vote percentages and identify the winner
    for candidate in candidate_Info_Tracker:

        # Get the vote count and calculate the percentage
        temp_Votes = candidate_Info_Tracker[candidate]
        temp_Percentage = (temp_Votes / total_votes) * 100

        # Update the winning candidate dictionary if this current candidate has more votes
        if temp_Votes > winning_Candidate_Info["Votes"]:
            winning_Candidate_Info["Name"] = candidate
            winning_Candidate_Info["Votes"] = temp_Votes

        # Print and save each candidate's vote count and percentage
        results = (f'{candidate}: {temp_Percentage:.3f}% ({temp_Votes})')
        print(results)
        print("")

        # Print results to text file
        txt_file.write("\n")
        txt_file.write(f'{results}' + '\n')
        txt_file.write("\n")

    # Generate and print the winning candidate summary
    print("------------------------------------------------")
    print("")
    print(f'Winner: {winning_Candidate_Info["Name"]}')
    print("")
    print("------------------------------------------------")

    # Save and write the winning candidate summary to the text file
    txt_file.write("------------------------------------------------" + "\n")
    txt_file.write("\n")
    txt_file.write(f'Winner: {winning_Candidate_Info["Name"]}' + '\n')
    txt_file.write("\n")
    txt_file.write("------------------------------------------------" + "\n")

