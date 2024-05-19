"""
This class implements all instructions with no operands.
It is the superclass for all instructions.

Revision History
    5/17/2024   Zachary Pestrikov   Wrote File
"""

class Instruction():
    """
    Implements all instructions that take no operands.
    All other instructions are extensions 
    of this class.
    The class assumes the opcode is correct.
    """

    errors = [] 

    def __init__(self, opcode, operands, file, line_num):
        self._opcode = opcode
        self._operands = operands
        self._file = file
        self._line_num = line_num
        self.error = False
        self._operand_list = self._validate_operands()
        self._hexadecimal_opcode = self._hex_opcode()

    def _validate_operands(self):
        """
        Operands come in stripped.
        Checks if the instruction contains no operands. 
        
        Returns the operands contained in the instruction.
        If there are no operands(as there should be), returns ''
        If there is an operand, an error will be issued.
        """
        operands = self._operands
        error = f'Operand Error/File {self._file}/Line {str(self._line_num)}/{self._opcode} Expects No Operands/Recieved "{self._operands}"'
        
        if operands != '':
            self.error = True
            self.errors.append(error)
        
        return operands

        
    
    
    def _hex_opcode(self):
        """
        This private method translates the instruction's opcode to 
        hex if there are no errors. The method assumes that the instruction's 
        opcode is correct, stripped, and uppercase.
        """
        instructions = {
            'ASR': '0111000100000001',
            'DEC': '0111101100000000',
            'INC': '0000000000000000',
            'LSL': '0101100000000000',
            'LSR': '0111000100000000',
            'NEG': '0010011100000000',
            'NOT': '0010110100000000',
            'RLC': '0101000000000000',
            'ROL': '0101001000000000',
            'ROR': '0111000100000010',
            'RRC': '0111000100000011',
            'STI': '0111111110000001',
            'CLI': '0000011101101001',
            'STU': '0111111100100010',
            'CLU': '0000011111001010',
            'STC': '0111111100001100',
            'CLC': '0000011111100100',
            'TAX': '0000011110000000',
            'TXA': '0110011100000001',
            'INX': '0000010110000000',
            'DEX': '0000110110000000',
            'TAS': '0000011101010000',
            'TSA': '0110011100000000',
            'INS': '0000011001000000',
            'DES': '0000111001000000',
            'NOP': '0001111110000000',
            'RTS': '0001111100000000',
            'POPF': '0000001000000000',
            'PUSHF': '0000111000000000'
        }

        if self.error == True:
            return 'ERROR'
        

        hex_op = hex(int(instructions[self._opcode], 2))[2:]
        hex_op = '0' * (4 - len(hex_op)) + hex_op
        return hex_op
    
    
    def hex(self, instruction_num, symbols, labels, stack_init, bytes_table):
        """
        This function returns the hex version of the opcode.
        It also handles stack warnings.
        """  
        opcode = self._opcode

        # handle stack warnings
        stack_instructions = ['RTS', 'POPF', 'PUSHF']
        if opcode in stack_instructions and stack_init == False:
            self.errors.append(f'Stack Warning/File {self._file}/Line{str(self._line_num)}/Stack Not Initialized')
        
        instruction_num = hex(instruction_num)[2:]
        instruction_num = '0' * (4 - len(instruction_num)) + instruction_num

        return f'{instruction_num.upper()} {self._hexadecimal_opcode.upper()}'