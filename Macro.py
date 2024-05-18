"""
This file implements the Macro class for the Caltech10 Assembler.

Revision History
    5/17/2024   Zachary Pestrikov   Wrote File
"""

from Instructions.Instruction import Instruction
from Instructions.OperandInstructions.OperandInstruction import OperandInstruction
from Instructions.OperandInstructions.CallJmp import CallJmpInstruction
from Instructions.OperandInstructions.MultiOpInstructions.MultiOpInstruction import MultiOpInstruction
from Instructions.OperandInstructions.MultiOpInstructions.LoadStoreInstruction import LoadStoreInstruction

class Macro():
    """
    This class implements macros. Macros are
    combinations of instructions that can be grouped
    together and used under the same name throughout
    an assembly program, but with different arguments.

    Therefore, macros contain their name, their arguments,
    and their instructions. They cannot contain labels or
    other macros. Macros will be defined by the #macro pseudo-op.
    They will be called in the form.
    Label: MacroName(Arguments) ; comments
    """
    _opcodes = ['LDI', 'LDD', 'LD', 'STD', 'ST', 'JMP', 'JA', 'JAE', 'JNC',
        'JB', 'JC', 'JBE', 'JE', 'JZ', 'JG', 'JGE', 'JL', 'JLE', 'JNE', 
        'JNZ', 'JNS', 'JNU', 'JNV', 'JS', 'JU', 'JV', 'CALL', 'RTS', 'POPF', 
        'PUSHF', 'IN', 'OUT', 'NOP', 'TAX', 'TXA', 'INX', 'DEX', 'TAS', 'TSA', 
        'INS', 'DES', 'STI', 'CLI', 'STU', 'CLU', 'STC', 'CLC', 'AND', 'ANDI', 
        'ASR', 'CMP', 'CMPI', 'DEC', 'INC', 'LSL', 'LSR', 'NEG', 'NOT', 'OR', 
        'ORI', 'RLC', 'ROL', 'ROR', 'RRC', 'SBB', 'SBBI', 'SUB', 'SUBI', 'TST', 
        'TSTI', 'XOR', 'XORI'
    ]
    no_operand_instructions = [
        'ASR', 'DEC', 'INC', 'LSL', 'LSR', 'NEG', 'NOT', 'RLC', 'ROL', 'ROR', 'RRC', 
        'STI', 'CLI', 'STU', 'CLU', 'STC', 'CLC', 'TAX', 'TXA', 'INX', 'DEX', 'TAS', 
        'TSA', 'INS', 'DES', 'NOP', 'RTS', 'POPF', 'PUSHF'
    ]
    single_operand_instructions = [
        'ADCI', 'ADDI', 'ANDI', 'CMPI', 
        'ORI', 'SBBI', 'SUBI', 'TSTI', 'XORI', 
        'LDI', 'LDD', 'STD', 'IN', 'OUT'
    ]
    call_jmp_instructions = [
        "CALL", "JMP", "JA", "JAE", "JNC", "JB", "JC", "JBE", "JE", "JZ", "JG", 
        "JGE", "JL", "JLE", "JNE", "JNZ", "JNS", "JNU", "JNV", "JS", "JU", "JV"
    ]
    multi_op_instructions = [
        'ADC', 'ADD', 'AND', 'CMP', 'OR', 
        'SBB', 'SUB', 'TST', 'XOR'
    ]
    load_store_instructions = ['LD', 'ST']

    macros = []
    errors = []
    
    def __init__(self, name, arguments, lines, file, line_num):
        """
        This method initializes an instance of the Macro class.
        It is called when the macro is defined
        It will ensure that the arguments are valid. 
        Valid arguments are those that are not
        instructions, start with letters, and contain only
        letters and numbers. Valid names have the same
        requirements. Underscores are allowed for both,
        however.

        It will also ensure that the macro name has not been
        defined already, and that the lines contain only valid
        opcodes, operands and arguments, and comments.

        Arguments and name get passed in as stripped strings.
        Lines gets passed in as a list of lines in the macro.

        The macro name and arguments are case sensitive.
        Lines come in stripped
        """
        self._error = False
        self._name = name
        self._arguments = []
        self._file = file
        self._line_num = line_num

        # validate name
        if self._check_valid(name) == False:
            self.errors.append(f'Definition Error/File: {file}/Line: {line_num}/Invalid Macro Name {name}')
            self._error = True
        
        # valide arguments
        arguments = arguments.split(',')
        for argument in arguments:
            argument = argument.strip()
            if argument == '':
                continue
            elif argument in self._arguments: # cannon allow user to have two args with same name
                self.errors.append(f'Definition Error/File: {file}/Line: {line_num}/Duplicate Macro Arg "{argument}"')
                self._error = True
            elif self._check_valid(argument) == True:
                self._arguments.append(argument)
            else:
                self.errors.append(f'Definition Error/File: {file}/Line: {line_num}/Invalid Argument Name {argument}')
                self._error = True
        
        # Line num is the number that the macro's definition begins.
        # Thus, the first instruction in the macro is on line_num+1
        # validate the lines don't have labels have opcodes and have
        line_tuples = []
        for (offset, line) in enumerate(lines):
            if ';' in line: # comment
                line = line.split(';')[0].strip()
                lines[offset] = line
            if line.strip() == '': # blank lines and commented lines will create blank lines in the output
                line_tuples.append(('', ''))
                continue
            newline = False
            for char in line:
                if char == '\t' or char == ' ':
                    line_list = line.split(char)
                    if line_list[0].upper().strip() not in self._opcodes: # first thing in line must be opcode
                        self._error = True
                        self.errors.append(f'Definition Error/File: {file}/Line: {line_num + offset + 1}/Invalid Opcode {line_list[0]}')
                    else:
                        line_tuples.append((line_list[0].strip().upper(), ''.join(line_list[1:]).strip()))
                    newline = True
                    break
            if newline == False:
                if line.upper() not in self._opcodes: # must be no operand instruction
                    self._error = True
                    self.errors.append(f'Definition Error/File: {file}/Line: {line_num + offset + 1}/Invalid Opcode {line_list[0]}')
                else: line_tuples.append((line.strip().upper(), ''))
        self._lines = line_tuples

        if self._error == False:
            self.macros.append(name.strip())


    def _check_valid(self, code):
        """
        Given a 'code'(a macro name or macro argument),
        checks whether the code is valid.
        Valid codes are not opcodes or existing macros, start with letters,
        and only contain letters and numbers(no special characters).
        Underscores are allowed

        Macro names and arguments are case sensitive.
        """
        opcodes = self._opcodes

        if code == '':
            return False

        # cannot have already been defined and cannot be an opcode, must start with letter
        if code.upper() in opcodes or code in self.macros or code[0].isalpha() == False:
            return False
        
        for letter in code:
            if letter.isalpha() == False and letter.isdigit() == False and letter != '_':
                return False
            
        return True
    

    def hex(self, arguments, instruction_num, symbols, labels, stack_init, bytes_table):
        """
        This method converts the macro to hex on the second pass when the argument inputs
        are given as well as necessary tables, the instruction number, and the state of the 
        stack. The function returns a tuple of a string of the hexed macro, and the integer
        number of the last instruction in the macro. If that number is greater than 0x1FFF(PC max),
        then it issues an error
        """
        lines = self._lines
        hex_output = ''

        if self._error == True:
            return ('ERROR\n', instruction_num)

        arguments = arguments.split(',')
        parameters = self._arguments
        instruction_num -= 1 # so that can continouisly inc in the loop
        for (offset, line) in enumerate(lines):
        # ensure that blank lines are outputted as blank lines
            if line[0] == '':
                hex_output += '\n'
                continue
            else:
                instruction_num += 1
                opcode = line[0]
                operands = line[1]

                # switch out the operands for the arguments
                if len(parameters) != len(arguments):
                    self._error = True
                    self.errors.append(f'Macro Error/File {self._file}/Line {self._line_num}/Invalid Macro Arg Count({len(arguments)}, Expected {len(parameters)})')
                    return ('ERROR', instruction_num)
                for (idx, param) in enumerate(parameters):
                    if parameters.count(param) != 1:
                        self.errors.append(f'Macro Error/File {self._file}/Line {self._line_num}/Duplicate Macro Arg "{param}"')
                    if param in operands: # param already stripped, case-sensitive
                        # need to ensure that it is not just a shorter version of actual operand
                        # ensure that other operands are not in there too
                        # instructions will handle other errors
                        go_next = False
                        for param2 in parameters[idx + 1:]:
                            if param2 in operands and len(param2) > len(param):
                                go_next = True
                                break
                        if go_next == True: continue

                        op_list = operands.split(param)
                        operands = op_list[0] + arguments[idx].strip() + op_list[1]

                if opcode in self.no_operand_instructions:
                    line = Instruction(opcode, operands, self._file, self._line_num + offset + 1)
                elif opcode in self.call_jmp_instructions:
                    line = CallJmpInstruction(opcode, operands, self._file, self._line_num + offset + 1)
                elif opcode in self.single_operand_instructions:
                    line = OperandInstruction(opcode, operands, self._file, self._line_num + offset + 1)
                elif opcode in self.multi_op_instructions:
                    line = MultiOpInstruction(opcode, operands, self._file, self._line_num + offset + 1)
                elif opcode in self.load_store_instructions:
                    line = LoadStoreInstruction(opcode, operands, self._file, self._line_num + offset + 1)
                else:
                    self.errors.append(f'Definition Error/File {self._file}/Line {self._line_num + offset + 1}/Invalid Opcode "{opcode}"')
                    self._error = True
                    return ('ERROR', instruction_num)
                # instruction num is the next instruction
                hex_line = line.hex(instruction_num, symbols, labels, stack_init, bytes_table)
                hex_output += f'{hex_line}\n'

        # ensure instruction_num < 0x1fff + 1 (PC max)
        if instruction_num > 8191:
            self._error = True
            self.errors.append(f'Range Error/File {self._file}/Line {self._line_num}/Exceeds Max Instruction Count 0x1FFF')
            return ('ERROR', -1)

        return (hex_output, instruction_num)

# # test macro with allocated memory and comments and spaces between operands
# arguments = "k1,    m3, o4,k6   ,o9,k11 "
# lines = [
# "ASR",
# "ORI k1; comment",
# "STI",
# "XOR m3",
# "XOR S, o4  ; comment",
# "NOP",
# "XORI k6",
# "INS",
# "JV label8  ; comment",
# "AND S, o9",
# "LSR",
# "SUBI k11",
# ]
# macro11 = Macro("macro11", arguments, lines, "test", 2)
# arguments = "0x1f,memory,0x3e,0x6d,0x30,0x87"
# instruction_num = 3592
# symbols = []
# labels = {
# 'label0': '0DD5',
# 'label1': '0E28',
# 'label2': '0E4D',
# 'label3': '0D9C',
# 'label4': '0E4A',
# 'label5': '0DEB',
# 'label6': '0E7B',
# 'label7': '0DD7',
# 'label8': '0E60',
# 'label9': '0E41',
# 'label10': '0DF8',
# 'label11': '0D9A',
# }
# print(macro11._error)
# print(macro11._lines)
# (hex, num) = macro11.hex(arguments, instruction_num, symbols, labels, False, {'memory': '91'})
