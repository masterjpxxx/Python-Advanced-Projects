#! Python 3
#  This program search for a regex patern that can be found within the txt files in the given directory

import os, re

# Step 1: Ask the user for the directory containing the txt files
folder_path = input("Please input a location where to search: ")
# Step 2: Ask for the regex patern
regex = input("What is the regex pattern to be used for searching: ")
pattern = re.compile(regex)
# Step 3: Perform the search and display the output

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        with open(os.path.join(folder_path, filename), "r") as f:
            for line in f:
                if pattern.search(line):
                    print(f"{filename}: {line.strip()}")