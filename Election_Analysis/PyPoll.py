# Add dependencies
import csv
import os
# Assign variable to load file from path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign variable to save file to path
file_to_save = os.path.join("Analysis", "Election_Analysis.txt")
# Open election results and read file
with open(file_to_load) as election_data:
    # Read the file object with the file reader
    file_reader = csv.reader(election_data)
    # Read and print header row in CSV file
    headers = next(file_reader)
    print(headers)

#for row in file_reader:
# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("Analysis","Election_Analysis.txt")

# Use the open statement to open the file as a text file.
with open(file_to_save,"w") as txt_file:
    # Write data to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")