"""
This class implements instructions with opcodes
that can only take one operand.
These instructions include ADCI, ADDI, ANDI, CMPI, 
ORI, SBBI, SUBI, TSTI, XORI, LDI, LDD, STD, IN, OUT.
All other operand instructions are subclasses of this
class.

Revision History
    5/17/2024   Zachary Pestrikov   Wrote File
"""
from HexOffset import hex_offset

class OperandInstruction(): # TODO extends Instruction
    """
    Implements all instructions whose opcodes can take only
    take one operand: ADCI, ADDI, ANDI, CMPI, 
    ORI, SBBI, SUBI, TSTI, XORI, LDI, LDD, STD, IN, OUT.
    All other instructions that take operands are extensions 
    of this class.
    The class assumes the opcode is correct.
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
        """
        Operands come in stripped.
        Checks if the instruction operands are valid. 
        Valid Operands include:
            - (m) - constant(could be defined), single operand, memory address
            - (p) - constant(could be defined), single operand, I/O port address
            -  k  - constant(could be defined), single operand
        
        Returns the operand
        [Memory, Register, Offset].
        If the specified dictionary key is not used it will be ''.
        If the offset is negative, the '-' will be the first char.
        If the operand is blank, then 0 is assumed to be the operand.
        """
        operand_list = {
            'memory': False,
            'offset': ''    # if 0, then left blank
        }
        operands = self._operands
        opcode = self._opcode
        error = f'Operand Error/File {self._file}/Line {str(self._line_num)}/Invalid {self._opcode} Operands "{self._operands}"'
        
        # only one operand
        if '\t' in operands or ' ' in operands or ',' in operands:
            self.errors.append(error)
            self._error = True

        memory_instructions = ['LDD', 'STD', 'IN', 'OUT']
        # for ports and memory instructions, ensure that it is either a symbol/byte or hex
        if opcode in memory_instructions:
            if operands[:2] != '0x' and operands[0].isalpha == False and operands != '':
                self.errors.append(error)
                self._error = True
            if opcode in memory_instructions[0:2]:
                operand_list['memory'] == True
        
    
    
    def _hex_opcode(self):
        """
        This private method is given a dict(operand_list), 
        which contains the operands [memory, register, offset].
        It returns ERROR if the operands are invalid. Otherwise,
        it converts the opcode to hex based on the operands.
        The method assumes that the opcode is correct.
        """
        opcode_bin = { # first 6 bits of opcode binary
            'ADC': '011000',
            'ADD': '011010',
            'AND': '010001',
            'CMP': '001100',
            'OR': '011101',
            'SBB': '000110',
            'SUB': '000100',
            'TST': '010011',
            'XOR': '001101'
        }

        error = f'Operand Error/File {self._file}/Line {str(self._line_num)}/Invalid {self._opcode} Operands "{self._operands}"'
        operand_list = self._operand_list
        opcode = self._opcode
        if self._error == True:
            return 'ERROR'
        
        
        # addressing 00 is memory, 01 is X, 10 is S
        if operand_list['memory'] == True:
            addressing = '00'
        elif operand_list['register'] == 'X':
            addressing = '01'
        elif operand_list['register'] == 'S':
            addressing = '10'
        else: # error that didn't get caught
            self._error = True
            self.errors.append(error)
            return 'ERROR'
        
        bin = opcode_bin[opcode] + addressing
        opcode_hex = hex(int(bin, 2))[2:]
        return opcode_hex
    
    
    def hex(self, instruction_num, symbols, labels, stack_init, bytes_table):
        """
        This function takes in the symbol table, instruction number,
        and list of operands for the instruction. It then finalizes and returns
        the hexadecimal version of the instruction for the output file.
        The function assumes that instruction_num is positive and less than 1FFF (PC max).
        The instruction number should be in decimal.
        """
        if self._error == True:
            return 'ERROR'
        operand_list = self._operand_list
        error = f'Operand Error/File {self._file}/Line {str(self._line_num)}/Invalid {self._opcode} Operands "{self._operands}"'
        
        (offset, warning, invalid) = hex_offset(operand_list['offset'], symbols, operand_list['memory'], bytes_table)
        if warning == True and operand_list['memory'] == False:
            self.errors.append(f'Operand Warning/File {self._file}/Line {str(self._line_num)}/Truncation "{self._operands}"')
        if warning == True and operand_list['memory'] == True:
            self.errors.append(f'Memory Access Warning/File {self._file}/Line {str(self._line_num)}/Byte "{self._operands}" Not Allocated')
        if invalid == True:
            self.errors.append(error)
            self._error = True

        # convert instruction to hex
        instruction_num = str(hex(instruction_num))[2:] 
        self._hexadecimal_opcode = '0' * (2-len(self._hexadecimal_opcode)) + self._hexadecimal_opcode 
        instruction_num = '0' * (4 - len(instruction_num)) + instruction_num
        hex_op = self._hexadecimal_opcode + offset
        return f'{instruction_num.upper()} {hex_op.upper()}'