"""
This file implements the line class for the asembler.

Revision History
    - 5/19/2024 Zachary Pestrikov   Wrote File
"""

from Macro import Macro
from Instructions.Instruction import Instruction
from Instructions.OperandInstructions.CallJmp import CallJmpInstruction
from Instructions.OperandInstructions.MultiOpInstructions.MultiOpInstruction import MultiOpInstruction
from Instructions.OperandInstructions.OperandInstruction import OperandInstruction
from Instructions.OperandInstructions.MultiOpInstructions.LoadStoreInstruction import LoadStoreInstruction

class Line():
    """
    This class implements the line class for the Caltech10
    assembler. Each line in each file is converted to a Line object.
    The line class then determines the instruction type.
    If the line is not an instruction, macro, 
    pseudo-op, blank line, or commented line the line class issues an error.
    """
    include_files = []
    org = -1
    code = False  # code segment - True, data segment - False
    symbols = {}
    macros = []
    errors = []
    instructions = 0
    data = [] # list of lists for data alloc handled at the end

    def __init__(self, line, file, line_num, macro_lines):
        """
        Initializes the line, validates it,
        and turns in into an instruction if necessary.

        the input 'line' is a stripped string.
        If a macro is identified, then line will be the macro
        definition, and lines will be the instructions in the macro.
        """
        self.error = False
        self._line = ''
        # split the line into labels, operands, and opcodes
        line = line.strip()
        if line == '':
            return
        elif line.lower() == '#code':
            self.code = True
            self._line = ''
        elif self.code == False:
            self.data.append([line, file, line_num, macro_lines])
            return
        elif line.lower().startswith('#macro'):
            if '(' not in line or ')' not in line or '{' not in line:
                self.error == True
                self.errors.append(f'Definition Error/File {file}/Line {line_num}/Invalide Macro Definition \n{line}')
                self._line = ''
            else:
                # get arguments
                line = line[6:].strip() # remove #macro
                line = line[:len(line) - 1].strip() # remove {
                line = line.split('(') # args in the second argument up to last char
                macro_name = line[0].strip()
                self._line = Macro(macro_name, line[1][:len(line[1]) - 1], macro_lines, file, line_num)
                if self._line.error == False:
                    self.macros[macro_name] = self._line
        elif line.lower().startswith('#include'):
            line = line[8:] # remove #include
            self.include_files.append(line.strip())
            self._line = ''
        elif line.lower() == '#org':
            org = line_num

            
            # #macro (args) {macro_lines}


        pseudo_opcodes = ['#INCLUDE', '#ORG', '#CODE', '#DATA', '#=', 
                   '#MACRO', '#BYTE', '#WORD', '#STACK']
        
        # get operands into a list
        # can be split by tab or space
        operands = list(operands)


        # handle the pseudo_op's operands based off its opcode
        if opcode == 'INCLUDE':
            include(operands, file, line_num)
        elif opcode == 'ORG':
            org(operands, file, line_num)
        
        


    

