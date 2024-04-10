import csv

file = open("00_colour_list_hex_v3.csv", "r")
all_colours = list(csv.reader(file, delimiter=","))
file.close()

# remove the first row (header values)
all_colours.pop(0)

# get the first 50 rows
print(all_colours[:50])

print(f"Length: {len(all_colours)}")