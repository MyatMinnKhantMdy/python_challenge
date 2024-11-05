# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
previous_value = None # Tracks the previous month's Profit/Losses for calculating changes
changes = []          # Stores each monthly change in Profit/Losses
dates = []            # Stores the dates corresponding to each change
# Open and read the csv
with open(file_to_load) as financial_data:
    csvReader = csv.reader(financial_data)

    # Skip the header row
    header = next(csvReader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(csvReader)
    total_months += 1
    total_net += int(first_row[1])
    previous_value = int(first_row[1])

    # Process each row of data
    for row in csvReader:
        total_months += 1
        profit_loss = int(row[1])
        total_net += profit_loss

        # calculate the monthly change and add it to the list
        change = profit_loss - previous_value # calculate the change
        changes.append(change)                # store the change in the list for later analysis
        dates.append(row[0])                  # store the date associated with the change

        # Update previous_value to current profit/loss
        previous_value = profit_loss

# average changes
average_change = sum(changes) / len(changes)

# Calculate the greatest increase in profits (month and amount)
greatest_increase = max(changes)

# Calculate the greatest decrease in losses (month and amount)
greatest_decrease = min(changes)

#Find the dates for the greatest increase and decrease
greatest_increase_date = dates[changes.index(greatest_increase)]
greatest_decrease_date = dates[changes.index(greatest_decrease)]

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
