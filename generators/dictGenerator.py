import csv

out = open('out.txt', 'w')
with open('test_generation/instructions.txt') as file:
    reader = csv.reader(file, delimiter='\t')
    lines = []
    for line in reader:
        out.write(f"'{line[1]}': '{line[0]}',\n")