"""
This file implements the CALL and jump instructions for the Assembler.

Revision History:
    5/16/2024   Zachary Pestrikov   Implemented Class
"""

class CallJmpInstruction(): # TODO extends Operand Instruction
    """
    This class is call all jump instructions as well as 
    the CALL instruction. The CALL instruction generates a 
    warning if the stack has not been initialized.
    Jumps require labels.
    """

    errors = []  # extended from OperandInstruction

    def __init__(self, opcode, operands, file, line_num): # extended from OperandInstruction
        self._opcode = opcode
        self._operands = operands
        self._file = file
        self._line_num = line_num
        self._error = False
        self._operand_list = self._validate_operands()
        self._hexadecimal_opcode = self._hex_opcode()

    def _validate_operands(self):
        pass
    def _hex_opcode(self):
        pass
    def hex(self, instruction_num, symbols, labels, stack_init):
        pass
