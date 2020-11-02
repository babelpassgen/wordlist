"""
Simple cleaner script for diceware txt file format
"""
import sys, csv

input_filepath = sys.argv[1]
output_filepath = sys.argv[2]

with open(input_filepath) as csvfile:
    spamreader = csv.reader(csvfile, delimiter="\t")
    with open(output_filepath, 'w') as outfile:
        for row in spamreader:
            outfile.write(row[1] + "\n")

