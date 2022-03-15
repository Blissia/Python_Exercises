# Add dependencies
import csv
import os
# Assign variable to load file from path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign variable to save file to path
file_to_save = os.path.join("Analysis", "Election_Analysis.txt")

# Initialize total vote counter
total_votes = 0

# Candidate options and votes
candidate_options = []
candidate_votes = {}

# Track winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open election results and read file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read header in CSV file
    headers = next(file_reader)
    # Print each row in CSV file
    for row in file_reader:
        # Add to total vote count
        total_votes += 1
        # Retrieve candidate name from each row
        candidate_name = row[2]
        # If candidate's name matches no existing candidate, add them to candidate list
        if candidate_name not in candidate_options:
            # Add candidate name to candidate list
            candidate_options.append(candidate_name)
            # Begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to candidate's count
        candidate_votes[candidate_name] += 1

# Open and save results to text file
with open(file_to_save,"w") as txt_file:
    # Print final vote count
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end="")
    # Save final vote count to text file
    txt_file.write(election_results)
    # Determine percentage of votes for each candidate by iterating through candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # Display results for each candidate
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's name, vote count, and percentage of votes
        print(candidate_results)
        # Save candidate results to text file
        txt_file.write(candidate_results)
        # Determine winning candidate, vote count, and percentage
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    # Print winning candidate's results
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
    print(winning_candidate_summary)
    # Save winning candidate's results to text file
    txt_file.write(winning_candidate_summary)