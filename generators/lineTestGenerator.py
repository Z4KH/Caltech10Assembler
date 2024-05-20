"""
Generates tests for the Line Class
"""
import csv
import random

instructions = []
with open('out.txt', 'w') as file:
    file.write('')
with open('generators/instructions.txt') as file:
    reader = csv.DictReader(file, fieldnames=['binary', 'opcode', 'operands'], delimiter='\t')
    for line in reader:
        instructions.append(line)

operands = ['p', 'r', 'k', 'm', 'o']

instructions_to_generate = 200

out = open('out.txt', 'a')
hex_out = ''
instruction_num = 3065
instruction_num_for_hex = instruction_num
symbols = {}
labels = {}

for i in range(instructions_to_generate):
    instruction_idx = random.randint(0, 77)
    instruction = instructions[instruction_idx]
    if instruction['opcode']== None:
        line = '\n'
        hex_out = '\\n'
        continue
    if instruction['operands'] == None:
        operand = ''
    else:
        operand = instruction['operands'].strip()
    opcode = instruction['opcode'].strip()
    offset = random.randint(0, 255)
    off_hex = hex(offset)[2:]  
    off_hex = '0' * (2 - len(off_hex)) + off_hex

    if operand.strip() == '':
        binary = instruction['binary'].strip()
        off_hex = ''
        op_hex = hex(int(binary, 2))[2:]
        op_hex = '0' * (4- len(op_hex)) + op_hex
    else:
        binary = instruction['binary'].strip()[:8]
        op_hex = hex(int(binary, 2))[2:]
        op_hex = '0' * (2- len(op_hex)) + op_hex
    
    if i > 0: # instruction num is for first instruction, then inc
        instruction_num += 1
    instruction_num_hex = hex(instruction_num)[2:]
    instruction_num_hex = '0' * (4 - len(instruction_num_hex)) + instruction_num_hex

    if opcode.startswith('J') == False:
        instruction_hex = f'{instruction_num_hex} {op_hex}{off_hex}'
        hex_out = instruction_hex.upper()
    if opcode.startswith('J'): # jumps require labels
        line = f'{opcode} label' + str(i)
    elif operand == '':
        line = f'{opcode}'
    else: 
        if 'o' in operand:
            operand = operand.split(',')
            operand[1] = f' {offset}'
            operand = ','.join(operand)
        elif 'm' in operand or 'p' in operand:
            operand = hex(offset)
        else:
            operand = offset
        line = f'{opcode} {operand}'
    lines = f'"{line}",\n'

    if offset > 127:
        label_pc = instruction_num + offset - 256
        label_pc = hex(label_pc)[2:]
    else: 
        label_pc = instruction_num + offset
        label_pc = hex(label_pc)[2:]
    label_pc = '0' * (4 - len(label_pc)) + label_pc
    labels['label' + str(i)] = label_pc
    if opcode.startswith('J'):
        pc_jump = int(label_pc, 16)
        if instruction_num > pc_jump:
            diff = pc_jump - instruction_num - 1 + 256
            off_hex = hex(diff)[2:]
        else:
            diff = pc_jump - instruction_num - 1
            off_hex = hex(diff)[2:]
        off_hex = '0' * (2 - len(off_hex)) + off_hex
        instruction_hex = f'{instruction_num_hex} {op_hex}{off_hex}'
        hex_out = instruction_hex.upper()



    for (key, value) in instruction.items():
        if value == None:
            instruction[key] = ''
    out.write(f'# {' '.join(list(instruction.values()))}\n')
    out.write(f'text = "{line}"\n')
    out.write(f'line{i} = Line(text, "test", 2, [])\n')
    out.write(f'hex = line{i}.hex()\n')
    out.write(f'assert hex == "{hex_out}"\n')
    out.write(f'assert line{i}.error == False\n\n')

out.write('labels = {\n')
for label_name, value in labels.items():
    out.write(f"'{label_name}': '{value.upper()}',\n")
out.write('}\n')
out.write(f'Line.labels = labels')
out.close()


