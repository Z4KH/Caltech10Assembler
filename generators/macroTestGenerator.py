"""
Generates tests for the Macro Class
"""
import csv
import random

instructions = []
with open('generators/instructions.txt') as file:
    reader = csv.DictReader(file, fieldnames=['binary', 'opcode', 'operands'])
    for line in reader:
        instructions.append(line)

no_operand_instructions = instructions = {
            'ASR': '0111000100000001',
            'DEC': '0111101100000000',
            'INC': '0000000000000000',
            'LSL': '0101100000000000',
            'LSR': '0111000100000000',
            'NEG': '0010011100000000',
            'NOT': '0010110100000000',
            'RLC': '0101000000000000',
            'ROL': '0101001000000000',
            'ROR': '0111000100000010',
            'RRC': '0111000100000011',
            'STI': '0111111110000001',
            'CLI': '0000011101101001',
            'STU': '0111111100100010',
            'CLU': '0000011111001010',
            'STC': '0111111100001100',
            'CLC': '0000011111100100',
            'TAX': '0000011110000000',
            'TXA': '0110011100000001',
            'INX': '0000010110000000',
            'DEX': '0000110110000000',
            'TAS': '0000011101010000',
            'TSA': '0110011100000000',
            'INS': '0000011001000000',
            'DES': '0000111001000000',
            'NOP': '0001111110000000',
            'RTS': '0001111100000000',
            'POPF': '0000001000000000',
            'PUSHF': '0000111000000000'
        }

relative_jumps = {
            'JA': '10001000',
            'JAE': '10001100',
            'JB': '10001111',
            'JC': '10001111',
            'JBE': '10001011',
            'JE': '10011111',
            'JG': '10101111',	
            'JGE': '10111011',
            'JL': '10111000',
            'JLE': '10101100',
            'JNE': '10011100',
            'JNS': '10011000',
            'JNU': '10111100',
            'JNV': '10101000',
            'JS': '10011011',
            'JU': '10111111',
            'JV': '10101011',
        }

multi_op_instructions = ['ADC', 'ADD', 'AND', 'CMP', 'OR', 
'SUBB', 'SUB', 'TST', 'XOR']

operands = ['p', 'r', 'k', 'm', 'o']

instructions_to_generate = random.randint(3, 20)

for i in range(instructions_to_generate):
    instruction_idx = random.randint(0, 85)
    instruction = instructions[instruction_idx]
    opcode = instruction[opcode]

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
#     hex = macro.hex('4', 0, [], [], False, [])
#     assert hex == '0000.....'##########

