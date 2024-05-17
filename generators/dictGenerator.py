import csv

out = open('out.txt', 'w')
opcodes = []
with open('generators/instructions.txt') as file:
    for line in file:
        if line.strip() not in opcodes:
            opcodes.append(line.strip())
print(opcodes)
out.close()