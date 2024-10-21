# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

#This script is using the template file included in the "Module 3 Challenge" files.
#Credits for the baseline formatting of this script belong to whoever created this template file through the bootcamp course

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("Analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
month_Total_Tracker = 0
total_net = 0

# Add more variables to track other necessary financial data
net_Change_List = []
negative_Prof_Sum = 0
positive_Prof_Sum = 0
previous_Profit = 0
temp_Change = 0
final_Average_Change = 0

# Setting up dictionaries to store info for "Greatest Increase/Decrease in Profits" sections
great_Profit_Increase = {"Date": "",
                         "Profit": 0}
great_Profit_Decrease = {"Date": "",
                         "Loss": 0}


# Open and read the csv
with open(file_to_load, encoding='UTF-8') as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:

        # After every row, increment the month total tracker for use in summary output.
        # Every row in the data set is a new month so a simple increment function,
        # will work fine for finding the desired "Total Months" value
        month_Total_Tracker = month_Total_Tracker + 1

        # On every row, determine whether the profit/loss column value is a positive or negative number and add everything together.
        # Also, convert the gathered values to integers before calculating
        temp_Calc = row[1]
        temp_Calc = int(temp_Calc)

        if temp_Calc > 0:
            positive_Prof_Sum = positive_Prof_Sum + temp_Calc

        if temp_Calc < 0:
            negative_Prof_Sum = negative_Prof_Sum + temp_Calc

        total_net = negative_Prof_Sum + positive_Prof_Sum

        # Create temporary variables to store the info in the "Date" and "Profit/Losses" columns
        company_Date = row[0]
        company_Performance = int(row[1])

        # Only start tracking and managing profit change values *after* first proper data row
        if month_Total_Tracker > 1:

            # Subtract current company_Performance value from the previous one, then append that value into a list that tracks those values. 
            # This will be what stores the "Change" values that get used to find the desired "Average Change" summary display. 
            temp_Change = company_Performance - previous_Profit
            net_Change_List.append(temp_Change)

            # Process for assigning a specific date to the greatest increase/decrease.
            # Check if current profit change value is higher than the "great_Profit_Increase" dictionary value,
            # If yes, update dictionary info
            if temp_Change > great_Profit_Increase["Profit"]:
                great_Profit_Increase["Date"] = company_Date
                great_Profit_Increase["Profit"] = temp_Change

            # Check if current profit change value is lower than the "great_Profit_Decrease" dictionary value,
            # If yes, update dictionary info
            if temp_Change < great_Profit_Decrease["Loss"]:
                great_Profit_Decrease["Date"] = company_Date
                great_Profit_Decrease["Loss"] = temp_Change

        # Set previous_Profit value to most recent company_Performance value for use in the following rows
        previous_Profit = company_Performance

# After the loop finishes, calculate the final Average Change value. Get the sum of all values in the list,
# then divide by the length of the list.
final_Average_Change = sum(net_Change_List) / len(net_Change_List)

# Print output summary table to terminal
print("Financial Analysis")
print("------------------------------------------------")
print(f"Total Months: {month_Total_Tracker}")
print(f"Total:  ${total_net}")
print(f"Average Change: ${final_Average_Change:.2f}")
print(f"Greatest Increase in Profits: {great_Profit_Increase['Date']} (${great_Profit_Increase['Profit']})")
print(f"Greatest Increase in Profits: {great_Profit_Decrease['Date']} (${great_Profit_Decrease['Loss']})")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis" + "\n")
    txt_file.write("------------------------------------------------" + "\n")
    txt_file.write(f"Total Months: {month_Total_Tracker}" + "\n")
    txt_file.write(f"Total:  ${total_net}" + "\n")
    txt_file.write(f"Average Change: ${final_Average_Change:.2f}" + "\n")
    txt_file.write(f"Greatest Increase in Profits: {great_Profit_Increase['Date']} (${great_Profit_Increase['Profit']})" + "\n")
    txt_file.write(f"Greatest Increase in Profits: {great_Profit_Decrease['Date']} (${great_Profit_Decrease['Loss']})" + "\n")