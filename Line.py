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
    pseudo-op, blank line, or commented line, then the line class issues an error.
    """
    include_files = []
    org = False
    seg = -1  # -1 => neither, 0=> data, 1=> code
    symbols = {}
    macros = []
    errors = []
    instructions = 0
    data = [] # list of lists for data alloc handled at the end
    preOrg = [] # for code that was found and not in org

    def __init__(self, line, file, line_num, macro_lines):
        """
        Initializes the line, validates it,
        and turns in into an instruction if necessary.

        the input 'line' is a stripped string.
        If a macro is identified, then line will be the macro
        definition, and lines will be the instructions in the macro.
        Lines, file names, macro lines all come in stripped
        """
        # self._ismacro
        self._line = line
        self._ismacro = False
        self._file = file
        self._line_num = line_num
        self._macro_lines = macro_lines

        # remove comments
        if ';' in line:
            idx = line.index(';')
            line = line[:5].strip()
            self._line = line
        # if line is blank, then want to print blank line
        if line == '':
            return
        # first check if pseudo-op and handle if it is
        if line.startswith('#'): self._handle_pseudo_op()
        # next, check if origin has been found yet, if not then add the line to preOrg
        else:
            if self.org == False:
                self.preOrg.append(line, file, line_num, macro_lines)
            else:
                if self.seg 
        # if origin found check if data, else, add to data
        # if origin found and code
            # split into label, opcode, operand
            # add label to table
            # distribute instruction (if not a valid opcode, then macro, so check if have (), andset ismacro to true)
    
    def handle_data(self):
        pass

    def handle_preOrg(self):
        pass

    def _handle_pseudo_op(self):
        pass

    def hex(self):
        # if self._line is '', return '\n'
        #if hex.strip!= '' instruction_num ++
        pass


    

