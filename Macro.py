"""
This file implements the Macro class for the Caltech10 Assembler.

Revision History
    5/17/2024   Zachary Pestrikov   Wrote File
"""

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
            elif self._check_valid(argument) == True:
                self._arguments.append(argument)
            else:
                self.errors.append(f'Definition Error/File: {file}/Line: {line_num}/Invalid Argument Name {argument}')
                self._error = True
        
        # validate the lines don't have labels have opcodes and have
        # appropriate operands, and split them.
        # ensure that blank lines are kept in


    def _check_valid(self, code):
        """
        Given a 'code'(a macro name or macro argument),
        checks whether the code is valid.
        Valid codes are not opcodes or existing macros, start with letters,
        and only contain letters and numbers(no special characters).
        Underscores are allowed

        Macro names and arguments are case sensitive.
        """

        if code == '':
            return False

        opcodes = ['LDI', 'LDD', 'LD', 'STD', 'ST', 'JMP', 'JA', 'JAE', 'JNC',
                    'JB', 'JC', 'JBE', 'JE', 'JZ', 'JG', 'JGE', 'JL', 'JLE', 'JNE', 
                    'JNZ', 'JNS', 'JNU', 'JNV', 'JS', 'JU', 'JV', 'CALL', 'RTS', 'POPF', 
                    'PUSHF', 'IN', 'OUT', 'NOP', 'TAX', 'TXA', 'INX', 'DEX', 'TAS', 'TSA', 
                    'INS', 'DES', 'STI', 'CLI', 'STU', 'CLU', 'STC', 'CLC', 'AND', 'ANDI', 
                    'ASR', 'CMP', 'CMPI', 'DEC', 'INC', 'LSL', 'LSR', 'NEG', 'NOT', 'OR', 
                    'ORI', 'RLC', 'ROL', 'ROR', 'RRC', 'SBB', 'SBBI', 'SUB', 'SUBI', 'TST', 
                    'TSTI', 'XOR', 'XORI']

        # cannot have already been definied and cannot be an opcode, must start with letter
        if code.upper() in opcodes or code in self.macros or code[0].isalpha() == False:
            return False
        
        for letter in code:
            if letter.isalpha() == False and letter.isdigit() == False and letter != '_':
                return False
            
        return True
    

    def hex(self, arguments, instruction_num, symbols, labels, stack_init, bytes_table):
        # ensure that blank lines are outputted as blank lines
# ensure that instruction num doesnt go past 1fff
        pass
