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
from OperandInstructions.HexOffset import hex_offset
from Instruction import Instruction

class OperandInstruction(Instruction):
    """
    Implements all instructions whose opcodes can take only
    take one operand: ADCI, ADDI, ANDI, CMPI, 
    ORI, SBBI, SUBI, TSTI, XORI, LDI, LDD, STD, IN, OUT.
    All other instructions that take operands are extensions 
    of this class.
    The class assumes the opcode is correct.
    """

    def _validate_operands(self):
        """
        Operands come in stripped.
        Checks if the instruction operands are valid. 
        Valid Operands include:
            - (m) - constant(could be defined), single operand, hex memory address
            - (p) - constant(could be defined), single operand, I/O hex port address
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
            if len(operands) > 3 and operands != '':
                if operands[:2] != '0x' and operands[0].isalpha() == False :
                    self.errors.append(error)
                    self._error = True
                    return operand_list
                if opcode in memory_instructions[0:2]:
                    operand_list['memory'] = True
            elif len(operands) < 3 and operands != '' and operands[0].isalpha() == False:
                self.errors.append(error)
                self._error = True
                return operand_list
        
        operand_list['offset'] = operands
        return operand_list

        
    
    
    def _hex_opcode(self):
        """
        This private method is given a dict(operand_list), 
        which contains the operands [memory, offset].
        It returns ERROR if the operands are invalid. Otherwise,
        it converts the opcode to hex based on the operands.
        The method assumes that the opcode is correct.
        """
        instructions = {
            'ADCI': '01100011',
            'ADDI': '01101011',
            'ANDI': '01000111',
            'CMPI': '00110011',
            'ORI': '01110111',
            'SBBI': '00011011',
            'SUBI': '00010011',
            'TSTI': '01001111',
            'XORI': '00110111',
            'LDI': '10001001',
            'LDD': '10000000',
            'STD': '10100000',
            'IN': '10010000',
            'OUT': '10110000',
        }

        if self._error == True:
            return 'ERROR'

        hex_op = instructions[self._opcode]
        return hex(int(hex_op, 2))[2:]
    
    
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
    

# # for debugging purposes:
# instruction = OperandInstruction('OUT', 'test', 'test', 620387)
# hex = instruction.hex(2646, [], [], False, {'test': '2B'})