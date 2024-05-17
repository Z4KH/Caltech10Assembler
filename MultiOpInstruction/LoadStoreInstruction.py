"""
This file implements the Load Store Instruction as a class for the Caltech10
Assembler. It is a subclass of the multi operand instruction class.

Revision History:
    5/13/2024   Zachary Pestrikov   Drafted Class
    5/14/2024   Zachary Pestrikov   Implemented Hexing Procedures
    5/15/2024   Zachary Pestrikov   Added Error Handling
    5/16/2024   Zachary Pestrikov   Finalized Class
"""
from MultiOpInstruction.MultiOpInstruction import MultiOpInstruction

class LoadStoreInstruction(MultiOpInstruction): # TODO extends multioperand instruction
    """
    Handles all instructions with the opcode LD or ST.
    Assumes that the opcode is correct and in uppercase
    Extends the MultiOperandInstruction class.
    Initialized with opcode, operands(str), file, line_num.
    Initialized with self._error = False
    """

    def _validate_operands(self):
        """
        Operands come in stripped.
        Checks if the Ld/St instruction's operands are valid. 
        Valid Operands include:
            - +X, X+, -X, X-, X
            - +S, S+, -S, S-, S
            - +o, -o for some offset o (default is 0)
        Lack of spaces is accounted for.
        
        Returns a dictionary of the operands
        [Register, +/-, pre/post, offset]
        +/i, pre/post will be empty string if reg unchanged
        If no offset, offset will return as ''
        """
        error = f'Operand Error/File {self._file}/Line {str(self._line_num)}/Invalid LD/ST Operands "{self._operands}"'
        operands = self._operands
        operand_list = {
            'register': '',
            '+/-': '',
            'pre/post': '',
            'offset': '', # leaves in '-' if offset negative
        }
        if operands == '':
            self.errors.append(error)
            self._error = True
            return operand_list
        # first character is either +,-,X,S
        if operands[0] == '+' or operands[0] == '-':
            operand_list['pre/post'] = 'pre'
            operand_list['+/-'] = operands[0]
            try: operands = operands[1:].strip() # find reg
            except: 
                    self.errors.append(error)
                    self._error = True
            operands = operands[0].upper() + operands[1:]
            if operands[0] == 'X' or operands[0] == 'S':
                operand_list['register'] = operands[0]
                # check for offset
                if operands == operands[0]: # no offset
                    return operand_list
                operands = operands[1:].strip()
                if operands[0] == '+':
                    try: operand_list['offset'] = operands[1:].strip()
                    except: pass # 0 offset
                    return operand_list
                elif operands[0] == '-': #subtraction
                    try: operand_list['offset'] = '-' + operands[1:].strip()
                    except: pass # 0 offset
                    return operand_list
                # some other thing is there, so its an error
            # no register, or no proper offset is found, so error
        elif operands[0].upper() == 'X' or operands[0].upper() == 'S':
            operand_list['register'] = operands[0].upper()
            if operands.strip() == operands[0]:
                return operand_list
            # find +/- (next non-space char)
            operands = operands[1:].strip()
            if operands[0] == '-': #x-+o, x-o, x-,
                operands = operands[1:].strip()
                if operands[0] == '+': # x-+offset
                    operand_list['+/-'] = '-'
                    operand_list['pre/post'] = 'post'
                    try: operand_list['offset'] = operands[1:]
                    except: pass
                elif operands[0] == '-': #x--offset:
                    operand_list['+/-'] = '-'
                    operand_list['pre/post'] = 'post'
                    try: operand_list['offset'] = '-' + operands[1:].strip()
                    except: pass
                elif operands == '': # x-
                    operand_list['+/-'] = '-'
                    operand_list['pre/post'] = 'post'
                else: # x-offset
                    operand_list['offset'] = '-' + operands.strip()
                return operand_list
            # could be X++o, or X+o, or X+, or X+-o
            elif operands[0] == '+':
                if operands[0] == operands.strip(): # x+
                    operand_list['+/-'] = '+'
                    operand_list['pre/post'] = 'post'
                    return operand_list
                operands = operands[1:].strip()
                if operands[0] == '+': # x++offset
                    operand_list['+/-'] = '+'
                    operand_list['pre/post'] = 'post'
                    try: operand_list['offset'] = operands[1:]
                    except: pass
                elif operands[0] == '-': #x+-offset:
                    operand_list['+/-'] = '+'
                    operand_list['pre/post'] = 'post'
                    try: operand_list['offset'] = '-' + operands[1:].strip()
                    except: pass
                else: # x+offset
                    operand_list['offset'] = operands
                return operand_list
        self.errors.append(error)
        self._error = True



    def _hex_opcode(self):
        """
        This private method is given a dict(operand_list), 
        which contains the operands [register, +/-, pre/post, offset].
        It returns ERROR if the operands are invalid. Otherwise,
        it converts the opcode to hex based on the operands
        """
        operand_list = self._operand_list
        if self._error == True:
            return 'ERROR'
        ldst = '00'
        prepost = '0'
        incdec = '0'
        sx = '0'
        select = '0'
        if self._opcode == 'ST':
            ldst = '01'
        if operand_list['pre/post'] == 'post' or operand_list['pre/post'] == '':
            prepost = '1'
        if operand_list['+/-'] == '-':
            incdec = '1'
        if operand_list['register'] == 'X':
            sx = '1'
        if operand_list['pre/post'] == '':
            select = '1'
        opcode_binary = ['1',ldst,prepost,incdec,sx,'1',select]
        return str(hex(int(''.join(opcode_binary), 2)))[2:].upper()
    

# For debugger:
# instruction = LoadStoreInstruction('ST', 'S++-5', 'test', 3)
#hex = instruction.hex(37330, {'test': '80'})
    


