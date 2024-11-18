import csv

# Step 1: Read data from the .txt file
with open("input.txt", "r") as f:
    lines = f.readlines()

# Step 2: Process data into rows
# Assuming the .txt file has tab-separated values:
rows = [line.strip().split("\t")[::-1] for line in lines]

# Step 3: Write processed data to a .csv file
with open('output.csv', 'w', newline="") as output_file:
    writer = csv.writer(output_file, delimiter=",")
    writer.writerow(["Contact", "Name", "Group"])
    output = writer.writerows(rows)
    print('Successfully converted txt -> csv')