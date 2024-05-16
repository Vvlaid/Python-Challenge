import csv

# Path to File using Relative Path
election_data = r"PyPoll\Resources\election_data.csv"

# Varible, list, and dictionary for the requirements
candidates = []
candidate_votes = {}
percent_votes = []
total_votes = 1

# Preparing variable for winner and winner votes count
winner = ""
winning_count = 0

# Opening CVS Election File to read the data within
with open(election_data, newline = "") as poll_data:
    csvreader = csv.DictReader(poll_data)
    
    # Coding for the count to start after the header
    csv_header = next(csvreader)
    
    # For Loop for the Candidates and Count of their votes
    for row in csvreader:
        total_votes += 1
        candidate_name = row["Candidate"]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        # Adding votes for Candidate when repeated in dataset
        candidate_votes[candidate_name] += 1

    # Figuring out the percetage of votes per candidate
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        votes_percent = float(votes)/float(total_votes) * 100

        # Condition for finding winning candidate
        if (votes > winning_count):
            winning_count = votes
            winner = candidate

        # Variable for all candidate voter count with percents
        results = f"{candidate}: {votes_percent:.3f}% ({votes})"
        print(results)

# Print the results within the Terminal
print("\nElection Results\n")
print("-----------------------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------------------")
print(results)
print("-----------------------------------------")
print(f"Winner: {winner}")
print(f"-------------------------------------------")

with open('election_results', "w") as text:
    text.write("\nElection Results \n \n"),
    text.write("------------------------------------------- \n \n"),
    text.write(f"Total Votes: {total_votes} \n \n"),
    text.write("-------------------------------------------\n \n"),
    text.write(f"{results}\n \n"),
    text.write(f"-------------------------------------------\n \n"),
    text.write(f"Winner: {winner}\n\n")
    text.write(f"-------------------------------------------")