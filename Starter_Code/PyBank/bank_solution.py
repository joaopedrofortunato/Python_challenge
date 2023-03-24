# Your analysis should align with the following results:
    # Total Months: 86
    # Total: $22564198
    # Average Change: $-8311.11
    # Greatest Increase in Profits: Aug-16 ($1862002)
    # Greatest Decrease in Profits: Feb-14 ($-1825558)

import csv

input_path = "Resources/budget_data.csv"

months = 0
total = 0
pos_total = 0
total_dif = 0

def totals(input_path, months, total):

    with open(input_path) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)

        for row in csvreader:
            # The total number of months included in the dataset
            months = months + 1
            # The net total amount of "Profit/Losses" over the entire period 
            total = total + int(row[1])

        print(f"Total Months: {months}")
        print(f"Total: ${total}")

def changes(input_path, months):

      with open(input_path) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)

        m = 0
        total_dif = 0
        max_increase = 0
        max_decrease = 0

        for row in csvreader:

            if months == 0:
                m = int(row[1])
                months = months + 1

            else:
                months = months + 1
                dif = int(row[1]) - m
                total_dif = total_dif + dif
                m = int(row[1])

                # The greatest increase in profits (date and amount) over the entire period
                if dif >= max_increase:
                    max_increase = dif
                    inc_month = row[0]

                # The greatest decrease in profits (date and amount) over the entire period
                if dif <= max_decrease:
                    max_decrease = dif
                    dec_month = row[0]
        
        # The changes in "Profit/Losses" over the entire period, and then the average of those changes 
        avg_dif = round(total_dif/(months - 1),2)

        print(f"Average Change: ${avg_dif}")
        print(f"Greatest Increase in Profits: {inc_month} (${max_increase})")
        print(f"Greatest Decrease in Profits: {dec_month} (${max_decrease})")


print("Financial Analysis")
print("-" * 25)
totals(input_path, months, total)
changes(input_path, months)