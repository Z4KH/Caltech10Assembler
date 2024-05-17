"""
Generates the tests for single operand-only instructions.
(ADCI, ADDI, ANDI, CMPI, ORI, SBBI, SUBI, TSTI, XORI, LDI, LDD, STD, IN, OUT)
"""
import random

def main():
    with open('test_generation/testgenerator_output.txt', 'w') as file:
        file.write('') # clear file
    with open('test_generation/instructions.txt') as instruction_file:
        for line in instruction_file:
            instruction_split = line.split('\t')
            instruction_hex = hex(int(instruction_split[0][:8].strip(), 2)) # instruction byte in hex
            line_num = random.randint(0,1000000)
            file = 'test'
            instruction_num = random.randint(0, 8191) # range of PC
            offset = random.randint(-128, 255)
            opcode = instruction_split[1]
            operands = instruction_split[2].strip()
            if 'm' in operands or 'p' in operands:
                operands = hex(abs(offset)) # not checking for errors
                offset_hex = hex(abs(offset))[2:]
            else:
                operands = offset
                if offset < 0:
                    offset += 256
                offset_hex = hex(offset)[2:]
            comment = line
            generate_test(opcode, operands, file, line_num, instruction_hex, offset_hex, comment)


def generate_test(opcode, operands, testfile, line_num, instruction_hex, offset_hex, comment):
    instruction_num = hex(random.randint(0, 8191))[2:] # range of PC
    instruction_num = ('0' * (4 -len(instruction_num))) + instruction_num
    offset_hex = ('0' * (2 - len(offset_hex))) + offset_hex
    with open('test_generation/testgenerator_output.txt', 'a') as file:
        file.write(f'# {comment}\n')
        file.write(f"instruction = OperandInstruction('{opcode}', '{operands}', '{testfile}', {line_num})\n")
        file.write(f"hex = instruction.hex({int(instruction_num, 16)}, [], [], False, [])\n")
        file.write(f'assert hex == "{instruction_num.upper()} {instruction_hex[2:].upper()}{offset_hex.upper()}"\n')
        file.write(f'assert instruction._error == False\n')
        file.write('\n')

if __name__ == '__main__':
    main()

# ex)
# instruction = LoadStoreInstruction('LD', 'X+4', 'test', 1)
# hex = instruction.hex(42, {}, [], False)
# assert hex == '002A 9704'
# assert instruction._error == False