"""
Generates tests for the Macro Class
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

instructions_to_generate = random.randint(3, 20)

out = open('out.txt', 'a')
hex_out = ''
lines = ''
instruction_num = random.randint(0, 8191)
instruction_num_for_hex = instruction_num
symbols = {}
arguments_init = ''
arguments_hex = ''
labels = {}

for i in range(instructions_to_generate):
    instruction_idx = random.randint(0, 77)
    instruction = instructions[instruction_idx]
    if instruction['opcode']== None:
        lines += '\n'
        hex_out += '\n'
        continue
    if instruction['operands'] == None:
        operand = ''
    else:
        operand = instruction['operands'].strip()
    opcode = instruction['opcode'].strip()
    offset = random.randint(0, 256)
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
        instruction_hex = f'{instruction_num_hex} {op_hex}{off_hex}\n'
        hex_out += instruction_hex.upper()
    if opcode.startswith('J'): # jumps require labels
        line = f'{opcode} label' + str(i)
    elif operand == '':
        line = f'{opcode}'
    else: 
        line = f'{opcode} {operand + str(i)}'
    lines += f'"{line}",\n'

    if offset > 127:
        label_pc = instruction_num + offset - 256
        label_pc = hex(label_pc)[2:]
    else: 
        label_pc = instruction_num + offset
        label_pc = hex(label_pc)[2:]
    if operand != '' and opcode.startswith('J') == False:
        arguments_init += f'{operand[-1]}{str(i)},'
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
        instruction_hex = f'{instruction_num_hex} {op_hex}{off_hex}\n'
        hex_out += instruction_hex.upper()

    if operand != '' and opcode.startswith('J') == False:
        arguments_hex += f'0x{off_hex},'
    
arguments_init = arguments_init[:len(arguments_init) - 1]
arguments_hex = arguments_hex[:len(arguments_hex) - 1]

out.write(f'arguments = "{arguments_init}"\n')
out.write(f'lines = [\n{lines}]\n')
out.write(f'macro = Macro("macro", arguments, lines, "test", 2)\n')
out.write(f'arguments = "{arguments_hex}"\n')
out.write(f'instruction_num = {instruction_num_for_hex}\nsymbols = []\n')
out.write('labels = {\n')
for label_name, value in labels.items():
    out.write(f"'{label_name}': '{value.upper()}',\n")
out.write('}\n')
out.write('(hex, num) = macro.hex(arguments, instruction_num, symbols, labels, False, [])\n')
out.write(f'assert hex == """{hex_out}"""\n\n')
out.write('assert macro.error == False')
out.close()



    

# example output
# lines = [
#         'LD X+4'
#         'LD X++10'
#         'LD X- + 21'
#         'LD +   X + 21'
#         'LD X + arg'
#     ]
    
#     arguments = 'arg, arg2'
#     macro = Macro('macro', arguments, lines, 'test', 2)
#     hex = macro.hex(arguments, instruction_num, symbols, labels, stack_init, bytes_table)
#     assert hex == '0000.....'##########

