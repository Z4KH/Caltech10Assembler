"""
Generates the tests for jump instructions.
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
            opcode = instruction_split[1]
            operands = instruction_split[2].strip()
            instruction_num = random.randint(128, 8191) # range of PC except less than 128 for testing purposes
            # relative jmp must be within 127 of the instruction_num bc adds from next pc
            rand = random.randint(0,1)
            if rand == 0:
                label_num = random.randint(instruction_num - 126,instruction_num + 128)
                error = False
            else:
                rand = random.randint(257, 500)
                label_num = random.randint(instruction_num+rand, 8191)
                error = True

            if label_num < instruction_num:
                offset = label_num - instruction_num - 1 + 256 # flip bits
            else:
                offset = label_num - instruction_num + 1
            label_num = hex(label_num)[2:]
            label_num = '0' * (4 - len(label_num)) + label_num
            offset_hex = hex(offset)[2:].upper()
            comment = line
            generate_test(opcode, operands, file, line_num, instruction_hex, offset_hex, comment, error, label_num, instruction_num)


def generate_test(opcode, operands, testfile, line_num, instruction_hex, offset_hex, comment, error, label_num, instruction_num):
    instruction_numh = hex(instruction_num)[2:]
    instruction_numh = ('0' * (4 -len(instruction_numh))) + instruction_numh
    offset_hex = ('0' * (2 - len(offset_hex))) + offset_hex
    with open('test_generation/testgenerator_output.txt', 'a') as file:
        file.write(f'# {comment}\n')
        file.write(f"instruction = CallJmpInstruction('{opcode}', 'label', '{testfile}', {line_num})\n")
        file.write(f"hex = instruction.hex({instruction_num}, []," + "{'label': '" + label_num.upper() + "'}, False)\n")
        if error == False:
            file.write(f'assert hex == "{instruction_numh.upper()} {instruction_hex[2:].upper()}{offset_hex.upper()}"\n')
            file.write(f'assert instruction._error == {str(error)}\n')
        else:
            file.write(f'assert instruction._error == {str(error)}\n')
        file.write('\n\n')

if __name__ == '__main__':
    main()


# instruction = CallJmpInstruction('JMP', 'label', 'test', 1)
# hex = instruction.hex(42, symbols[], {label: PCaddress}, stackInit)
# assert hex == '002A 9704'
# assert instruction._error == False

# must test 110aaaaaaaaaaaaa	JMP	a
# 111aaaaaaaaaaaaa	CALL	a in addition