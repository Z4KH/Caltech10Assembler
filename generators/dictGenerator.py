import csv

out = open('out.txt', 'w')
out.write('[')
with open('generators/instructions.txt') as file:
    for line in file:
        out.write(f'"{line.strip()}", ')
