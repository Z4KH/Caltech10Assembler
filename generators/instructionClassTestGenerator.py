"""
Generates the tests for instructions with no operands.
It does not test for errors, only for proper translation
"""
import random

def main():
    with open('test_generation/testgenerator_output.txt', 'w') as file:
        file.write('') # clear file
    with open('test_generation/instructions.txt') as instruction_file:
        for line in instruction_file:
            instruction_split = line.split('\t')
            instruction_hex = hex(int(instruction_split[0], 2))[2:]
            instruction_hex = '0' * (4 - len(instruction_hex)) + instruction_hex
            line_num = random.randint(0,1000000)
            file = 'test'
            opcode = instruction_split[1].strip()
            comment = line
            generate_test(opcode, file, line_num, instruction_hex, comment)


def generate_test(opcode, testfile, line_num, instruction_hex, comment):
    instruction_num = hex(random.randint(0, 8191))[2:] # range of PC
    instruction_num = ('0' * (4 -len(instruction_num))) + instruction_num
    with open('test_generation/testgenerator_output.txt', 'a') as file:
        file.write(f'# {comment}\n')
        file.write(f"instruction = Instruction('{opcode}', '', '{testfile}', {line_num})\n")
        file.write(f"hex = instruction.hex({int(instruction_num, 16)}, [], [], False, [])\n")
        file.write(f'assert hex == "{instruction_num.upper()} {instruction_hex.upper()}"\n')
        file.write(f'assert instruction._error == False\n')
        file.write('\n')

if __name__ == '__main__':
    main()


# instruction = LoadStoreInstruction('LD', 'X+4', 'test', 1)
# hex = instruction.hex(42, {}, [], False)
# assert hex == '002A 9704'
# assert instruction._error == False