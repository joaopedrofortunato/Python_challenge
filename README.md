# Python_challenge

## Description

     In this assignment, you'll use the concepts you've learned to complete two Python challenges, PyBank and PyPoll. Both tasks present a real-world situation where your newly developed Python scripting skills come in handy.

## Python_challenge UC Berkeley Data Analytics Bootcamp Module 3

### PyBank

#### Result:

    Financial Analysis
    ------------------
    Total Months: 86
    Total: $22564198
    Average Change: $-8311.11
    Greatest Increase in Profits: Aug-16 ($1862002)
    Greatest Decrease in Profits: Feb-14 ($-1825558)

#### Code:

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


### PyPoll

#### Result:

    Results
    --------------------
    Total Votes: 369711
    --------------------
    Charles Casper Stockham: 23.049% (85213)
    Diana DeGette: 73.812% (272892)
    Raymon Anthony Doane: 3.139% (11606)
    --------------------
    Winner: Diana DeGette

#### Code:

    import csv

    input_path = "Resources/election_data.csv"

    with open(input_path) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)

        candidates = []

        for row in csvreader:
            candidates.append(row[2])

        # A complete list of candidates who received votes
        res = [*set(candidates)]
        sorted_res = sorted(res)

        cand_1 = str(sorted_res[0])
        cand_2 = str(sorted_res[1])
        cand_3 = str(sorted_res[2])

    with open(input_path) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)

        votes_1 = 0
        votes_2 = 0
        votes_3 = 0

        # The total number of votes each candidate won
        for row in csvreader:
            if str(row[2]) == cand_1:
                votes_1 = votes_1 + 1
            elif str(row[2]) == cand_2:
                votes_2 = votes_2 + 1
            elif str(row[2]) == cand_3:
                votes_3 = votes_3 + 1

        # The total number of votes cast
        total = votes_1 + votes_2 + votes_3

        # The percentage of votes each candidate won
        percent_1 = round(votes_1 / total * 100, 3)
        percent_2 = round(votes_2 / total * 100, 3)
        percent_3 = round(votes_3 / total * 100, 3)

        # The winner of the election based on popular vote
        if votes_1 > votes_2 and votes_1 > votes_3:
            winner = cand_1
        elif votes_2 > votes_1 and votes_2 > votes_3:
            winner = cand_2
        elif votes_3 > votes_1 and votes_3 > votes_2:
            winner = cand_3
        
        print(f"Results")
        print(f"--------------------")
        print(f"Total Votes: {total}")
        print(f"--------------------")
        print(f"{cand_1}: {percent_1}% ({votes_1})")
        print(f"{cand_2}: {percent_2}% ({votes_2})")
        print(f"{cand_3}: {percent_3}% ({votes_3})")
        print(f"--------------------")
        print(f"Winner: {winner}")
