# class TestClass():
#     def __init__(self, opcode, operands, file, line_num):
#         self._opcode = opcode
#         self._operands = operands
#         self._file = file
#         self._line_num = line_num
#         self._error = False
#         self._operand_list = self._validate_operands()
#         self._opcode = self._hex_opcode(self._operand_list)

#     def _validate_operands(self):
#         return []
#     def _hex_opcode(self):
#         return ''
#     def hex(self):
#         pass

class LoadStoreInstruction(): # TODO extends multioperand instruction
    """
    Handles all instructions with the opcode LD or ST.
    Assumes that the opcode is correct and in uppercase
    Extends the MultiOperandInstruction class.
    Initialized with opcode, operands(str), file, line_num.
    Initialized with self._error = False
    """

    errors = [] # accessible outside class, holds all errors discovered in this class

    def _validate_operands(self):
        """
        Operands come in stripped, and uppercase.
        Checks if the Ld/St instruction's operands are valid. 
        Valid Operands include:
            - +X, X+, -X, X-, X
            - +S, S+, -S, S-, S
            - +o for some offset o (default is 0)
        Lack of spaces is accounted for.
        
        Returns a dictionary of the operands
        [Register, +/-, pre/post, offset]
        +/i, pre/post will be empty string if reg unchanged
        If no offset, offset will return as ''
        """
        error = f'Syntax Error/File {self._file}/Line {str(self._line_num)}/Invalid LD/ST Operands'
        operands = self._operands
        operand_list = {
            'register': '',
            '+/-': '',
            'pre/post': '',
            'offset': ''
        }
        # first character is either +,-,X,S
        if operands[0] == '+' or operands[0] == '-':
            operand_list['pre/post'] = 'pre'
            operand_list['+/-'] = operands[0]
            operands = operands[1:].strip() # find reg
            if operands[0] == 'X' or operands[0] == 'S':
                operand_list['register'] = operands[0]
                # check for offset
                operands = operands[1:].strip()
                if operands == '': # no offset
                    return operand_list
                elif operands[0] == '+':
                    operand_list['offset'] = operands[1:]
                    return operand_list
                # some other thing is there, so its an error
            # no register, or no proper offset is found, so error
        elif operands[0].upper() == 'X' or operands[0].upper() == 'S':
            operand_list['register'] = operands[0].upper()
            # find +/- (next non-space char)
            operands = operands[1:].strip()
            if operands[0] == '-' and operands[1:] == '': #x-
                operand_list['+/-'] == '-'
                operand_list['pre/post'] = 'post'
                return operand_list
            # could be X++o, or X+o, or X+
            elif operands[0] == '+':
                operands = operands[1:].strip()
                if operands[0] == '+': # x++offset
                    operand_list['+/-'] = '+'
                    operand_list['pre/post'] = 'post'
                    operand_list['offset'] = operands[1:]
                elif operands == '': # x+
                    operand_list['+/-'] = '+'
                    operand_list['pre/post'] = 'post'
                else: # x+offset
                    operand_list['offset'] = operands
                return operand_list
            # if there's no +/i, then offset is 0, and reg unchanged
            elif operands == '':
                return operand_list

        self.errors.append(error)
        self._error = True



    def _hex_opcode(self, operand_list):
        """
        This private method is given a dict(operand_list), 
        which contains the operands [register, +/-, pre/post, offset].
        It returns ERROR if the operands are invalid. Otherwise,
        it converts the opcode to hex based on the operands
        """
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


    def hex(self, instruction_num, symbols):
        """
        This function takes in the symbol table, instruction number,
        and list of operands for the instruction. It then finalizes and returns
        the hexadecimal version of the instruction for the output file.
        """
        if self._error == True:
            return 'ERROR'
        operand_list = self._operand_list
        error = f'Syntax Error/File {self._file}/Line {str(self._line_num)}/Invalid LD/ST Operands'
        
        offset = operand_list['offset']
        if offset in symbols:
            offset = symbols[offset]
        else:
            # handle converting offset to hex
            # cases for offset are dec, hex (0x...), bin(0b...), char, truncation
            if offset[0:2].upper() == '0x':
                try: 
                    offset = int(offset, 16)
                except ValueError:
                    self._error = True
                    self.errors.append(error)
                    return 'ERROR'
            elif offset[0:2].upper() == '0b':
                try:
                    offset = int(offset, 2)
                except ValueError:
                    self._error = True
                    self.errors.append(error)
                    return 'ERROR'
            elif offset[0] == "'" :
                if len(offset) != 3:
                    self._error = True
                    self.errors.append(error)
                    return 'ERROR'
                offset = ord(offset)
            else:
                try:
                    offset = int(offset)
                    if offset < 0:
                        if offset < -128:
                            offset = -128
                        offset+=256
                except ValueError:
                    self._error = True
                    self.errors.append(f'Syntax Error/File {self._file}/Line {str(self._line_num)}/Symbol Not Defined')
                    return 'ERROR'

        if offset > 255:
            offset = 255

        # now instruction is in dec
        # convert instruction to hex
        instruction_num = str(hex(instruction_num))[2:] 
        self._opcode = '0' * (2-len(self._opcode)) + self._opcode 
        offset = str(hex(offset))[2:]
        offset = '0' * (2-len(offset)) + offset
        instruction_num = '0' * (4 - len(instruction_num)) + instruction_num
        hex_op = self._opcode + offset
        return f'{instruction_num.upper()} {hex_op.upper()}'
    



        
    


