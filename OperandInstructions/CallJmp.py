"""
This file implements the CALL and jump instructions for the Assembler.

Revision History:
    5/16/2024   Zachary Pestrikov   Implemented Class
"""
from OperandInstructions.OperandInstruction import OperandInstruction

class CallJmpInstruction(OperandInstruction): 
    """
    This class is call all jump instructions as well as 
    the CALL instruction. The CALL instruction generates a 
    warning if the stack has not been initialized.
    Jumps require labels.
    """

    def _validate_operands(self):
        """
        Operands come in stripped.
        Checks if the Jump/call instruction's operands are valid. 
        Valid Operands consist of only a label with no spaces.
        This instruction does not check if the label is in the label
        table
        
        Returns the operand.
        """
        operands = self._operands
        error = f'Syntax Error/File {self._file}/Line {str(self._line_num)}/Invalid {self._opcode} Operands "{self._operands}"'

        if ' ' in operands or '\t' in operands or ',' in operands:
            self.errors.append(error)
            self._error = True
        return operands
        
    def _hex_opcode(self):
        """
        This private method converts the opcode to hex on the first pass for
        the relative jump instructions. If the instruction is an absolute
        jump or call, then it waits until the second pass to be transformed
        into hex. Opcodes come in uppercase.
        """
        opcode = self._opcode
        relative_jumps = {
            'JA': '10001000',
            'JAE': '10001100',
            'JNC': '10001100',
            'JB': '10001111',
            'JC': '10001111',
            'JBE': '10001011',
            'JE': '10011111',
            'JZ': '10011111',
            'JG': '10101111',	
            'JGE': '10111011',
            'JL': '10111000',
            'JLE': '10101100',
            'JNE': '10011100',
            'JNZ': '10011100',
            'JNS': '10011000',
            'JNU': '10111100',
            'JNV': '10101000',
            'JS': '10011011',
            'JU': '10111111',
            'JV': '10101011',
        }

        if self._error == True:
            return 'ERROR'

        if opcode in relative_jumps: hexop = hex(int(relative_jumps[opcode], 2))[2:]
        else: hexop = ''
        return hexop


    def hex(self, instruction_num, symbols, labels, stack_init, bytes_table):
        """
        This method is executed on the second pass of assembly.
        It converts the instruction completely to hex.
        If the stack is not initialized and the instruction is a CALL,
        a warning will be issued to let the user know that they cannot
        use too much stack space. If the label to jump to is not in
        the labels table, then an error will be issued. If the instruction
        is a relative jump and the label is too far, then an error will be issued.
        Opcodes come in upper case. Labels do not, and are case sensitive.
        Instruction_num is a decimal int
        """
        if self._error == True:
            return 'ERROR'
        opcode = self._opcode
        label = self._operand_list
        error = f'Operand Error/File {self._file}/Line {str(self._line_num)}/Invalid {self._opcode} Label "{self._operands}"'
        warning = f'Stack Warning/File {self._file}/Line{str(self._line_num)}/Stack Not Initialized'
        range_error = f'Range Error/File {self._file}/Line {str(self._line_num)}/Label "{self._operands}" Out of Range for RJMP'

        absolute = ['CALL', 'JMP']

        # handle jmp/call first
        if opcode in absolute:
            if label in labels:
                label_hex = labels[label]
                label_bin = bin(int(label_hex, 16))[2:]
                label_bin = '0' * (13 - len(label_bin)) + label_bin
            else:
                self.errors.append(error)
                self._error = True
                return 'ERROR'
            if opcode == 'CALL':
                if stack_init == False:
                    self.errors.append(warning)
                hex_op = hex(int('111' + label_bin, 2))[2:]
            else: hex_op = hex(int('110' + label_bin, 2))[2:]
        # handle relative jumps
        else:
            hex_op = self._hexadecimal_opcode
            # turn label into relative
            if label in labels:
                label_pc = int(labels[label], 16)
                offset = label_pc - instruction_num + 1 # exec on next instruction
                # problems: offset > 127, offset < 0, offset < -127 
                if offset > 127:
                    self.errors.append(range_error)
                    self._error = True
                    return 'ERROR'
                elif offset < 0:
                    offset -= 2 #  since label is before instruction, offset increases negatively
                    if offset < -127:
                        self.errors.append(range_error)
                        self._error = True
                        return 'ERROR'
                    else:
                        offset += 256
            else: # label DNE
                self.errors.append(error)
                self._error = True
                return 'ERROR'
            offset = hex(offset)[2:]
            offset = '0' * (2- len(offset)) + offset
            hex_op += offset

        instruction_num = str(hex(instruction_num))[2:] 
        instruction_num = '0' * (4 - len(instruction_num)) + instruction_num
        return f'{instruction_num.upper()} {hex_op.upper()}'
                

