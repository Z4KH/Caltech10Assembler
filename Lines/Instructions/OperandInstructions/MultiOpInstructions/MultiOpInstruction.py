"""
This class implements instructions with opcodes
that can take multiple operands.
These instructions include ADC, ADD, AND, CMP, OR, 
SUBB, SUB, TST, XOR. Load and store instructions
extend this class.

Revision History
    5/16/2024   Zachary Pestrikov   Wrote File
"""
from Lines.Instructions.OperandInstructions.HexOffset import hex_offset
from Lines.Instructions.OperandInstructions.OperandInstruction import OperandInstruction

class MultiOpInstruction(OperandInstruction): # TODO extends OperandInstruction
    """
    Implements all instructions whose opcodes can take multiple
    operands. 
    ADC, ADD, AND, CMP, OR, SUBB, SUB, TST, XOR
    Load and store instructions with multiple operands
    are an extension of this class.
    The class assumes the opcode is correct.
    """

    def _validate_operands(self):
        """
        Operands come in stripped.
        Checks if the instruction operands are valid. 
        Valid Operands include:
            - (m) - constant(could be defined), single operand, memory address
            - X or S - single operand register, 0 offset assumed
            - X or S, o or -o - double operand reg+o or reg-o
        If there are two operands, they must be separated by a comma.
        If there is only one operand, there must not be any commas on the line.
        Constant definitions cannot include commas.
        
        Returns a dictionary of the operands:
        [Memory, Register, Offset].
        If the specified dictionary key is not used it will be ''.
        If the offset is negative, the '-' will be the first char.
        """
        operand_list = {
            'memory': False,
            'register': '',
            'offset': ''    # if 0, then left blank
        }
        operands = self._operands
        error = f'Operand Error/File {self._file}/Line {str(self._line_num)}/Invalid {self._opcode} Operands "{self._operands}"'
        

        # ensure operands are not blank
        if operands == '':
            operand_list['memory'] = True
            MultiOpInstruction.errors.append(f'Blank Operand Warning/File {self._file}/Line {str(self._line_num)}/Invalid {self._opcode} Operands "{self._operands}"')
            return operand_list
        
        # determine whether register or memory
        if operands[0].upper() == 'X' or operands[0] == 'S': # operand is register
            operand_list['register'] = operands[0].upper() 
            # deal with offset
            # cases 'X' 'X,' 'X , ' 'X, o' same for S
            if operands == operands[0]: # 'X' or 'S'
                return operand_list
            operands = operands[1:].strip()
            if operands[0] == ',':
                if operands == ',':
                    return operand_list
                operand_list['offset'] = operands[1:].strip()
                return operand_list
            elif operands[0] == '':
                return operand_list
            else:
                MultiOpInstruction.errors.append(error)
                self.error = True
        else: # operand is memory address
            if ' ' not in operands:
                # do not allow negative memory address
                if operands.startswith('-'):
                    self.error = True
                    MultiOpInstruction.errors.append(error)
                else:
                    operand_list['offset'] = operands
                    operand_list['memory'] = True
                return operand_list
        
        # anything else is an error
        self.error = True
        MultiOpInstruction.errors.append(error)
        return operand_list
    
    
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
        if self.error == True:
            return 'ERROR'
        
        
        # addressing 00 is memory, 01 is X, 10 is S
        if operand_list['memory'] == True:
            addressing = '00'
        elif operand_list['register'] == 'X':
            addressing = '01'
        elif operand_list['register'] == 'S':
            addressing = '10'
        else: # error that didn't get caught
            self.error = True
            MultiOpInstruction.errors.append(error)
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
        if self.error == True:
            return 'ERROR'
        operand_list = self._operand_list
        error = f'Operand Error/File {self._file}/Line {str(self._line_num)}/Invalid {self._opcode} Operands "{self._operands}"'
        
        (offset, warning, invalid) = hex_offset(operand_list['offset'], symbols, operand_list['memory'], bytes_table)
        if warning == True and operand_list['memory'] == False:
            MultiOpInstruction.errors.append(f'Operand Warning/File {self._file}/Line {str(self._line_num)}/Truncation "{self._operands}"')
        if warning == True and operand_list['memory'] == True:
            MultiOpInstruction.errors.append(f'Memory Access Warning/File {self._file}/Line {str(self._line_num)}/Byte "{self._operands}" Not Allocated')
        if invalid == True:
            MultiOpInstruction.errors.append(error)
            self.error = True

        # convert instruction to hex
        instruction_num = str(hex(instruction_num))[2:] 
        self._hexadecimal_opcode = '0' * (2-len(self._hexadecimal_opcode)) + self._hexadecimal_opcode 
        instruction_num = '0' * (4 - len(instruction_num)) + instruction_num
        hex_op = self._hexadecimal_opcode + offset
        return f'{instruction_num.upper()} {hex_op.upper()}'
    


  
