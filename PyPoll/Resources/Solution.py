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
        
        # Adding votes for Candidate when repeated
        candidate_votes[candidate_name] += 1

# Print the results within the Terminal
print("\nElection Results\n")
print("-----------------------------------------\n")
print(f"Total Votes: {total_votes}")
print(f"{candidate_votes}\n")