import csv
import secrets
from pathlib import Path

#path to data folder
cwd = Path.cwd() / "data"

#Opening input and output CSV files
with open(cwd / "users_in.csv", "r") as file_input, open(cwd / "users_out.csv", "w", newline='') as file_output:
    # Read the input CSV file as a dictionary
    reader = csv.DictReader(file_input)

    #Print the headers
    print("CSV Headers:", reader.fieldnames)

    # Checking if the fieldnames are read properly
    if reader.fieldnames is None:
        print("Error: No header found in CSV file.")
    else:
        # Writing the  output CSV file
        writer = csv.DictWriter(file_output, fieldnames=reader.fieldnames)

        # Write the header to the output file
        writer.writeheader()

        # Loop through each user and add a random password
        for user in reader:
            user["password"] = secrets.token_hex(8)  # Generates a random password
            writer.writerow(user)  # Write the user record with the password to the output file
