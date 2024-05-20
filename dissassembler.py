out = open('out.txt', 'w')

with open('gcdEuclidCaltech10.asm') as inFile:
    for line in inFile:
        if ';' in line:
            idx = line.find(';')
            line = line[:idx]
        out.write(line)

out.close()