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
from Instructions.OperandInstructions.HexOffset import hex_offset

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
    macros = {}
    errors = []
    instructions = 0
    data = [] # list of lists for data alloc handled at the end
    preOrg = [] # for code that was found and not in org
    bytes = [] # bytes allocated
    instructions_hexed = 0 # for PC
    labels = {} # label: instruction_num(4 digit hex)
    next_byte = 1 # addr of next byte allocated
    stack = False # whether the stack has been initialized

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
        self.error = False

        # remove comments
        if ';' in line:
            idx = line.index(';')
            line = line[:5].strip()
            self._line = line
        # if line is blank, then want to print blank line
        if line == '':
            self._line = '\n'
            return
        # first check if pseudo-op and handle if it is
        if line.startswith('#'): 
            self._handle_pseudo_op(line)
            self._line = ''
        # next, check if origin has been found yet, if not then add the line to preOrg
        else:
            if self.org == False:
                self.preOrg.append((line, file, line_num, macro_lines))
                self._line = ''
            else:
                if self.seg == 0: # if origin found, then must be pseudo-op
                    self._handle_pseudo_op(self, line)
                    self._line = ''
                else:# if origin found and code
                    self._handle_code(line)

    def _handle_code(self, line):
        """
        This method handles a line in the code segment.
        """
        # split into label, opcode, operand
        if ':' in line:
            line = line.split(':')
            label = line[0].strip()
            instruction = ''.join(line[1:])
            validation = self._handle_label(label)
            if validation == False:
                self.error = True
                self.errors.append(f'LabelError/File {self._file}/Line {self._line_num}/Duplicate Label "{label}"')
                self._line = ''
                return
        self._handle_instruction(instruction.strip())
        # comments, blanks, pseudo-ops, instructions all considered - all possible lines
                    

                    # distribute instruction (if not a valid opcode, then macro, so check if have (), andset ismacro to true)
    
    def _handle_instruction(self, line):
        """
        This private method handles a line if it contains an
        instruction. It validates the instruction, changes
        the instruction number, and assigns it to 
        self._line. If the instruction is a macro,
        it sets self._ismacro to True for the macro
        to be turned into hex on the second pass.
        If the instruction opcode is invalid, it sets
        self.error to True and will output an error message.
        """
        # ensure no error somehow go through
        if self.error == True:
            self._line = ''
            return

        # if blank line, then print blank line
        if line == '':
            self._line = '\n'
            return
        # check if valid macro, only time parantheses are allowed
        if '(' in line and ')' in line: 
            self._ismacro = True
            line = line.split('(')
            # get rid of closing )
            try: idx = line[1].index(')')
            except ValueError:
                self.error = True
                self.errors.append(f'Macro Error/File {self._file}/Line {self._line_num}/Invalid Args ({line[1]}')
                self._line = ''
                return
            args = line[1][:idx].strip()
            name = line[0].strip()
            self._line = (name, args)
            # add to instructions
            self.instructions += self._line.num_instructions()
            return
        # if not macro then must be instruction
        # first check for no operand instructions
        if line in Macro.no_operand_instructions:
            self._line = Instruction(line, '', self._file, self._line_num)
            return
        # now know that there must be operands => separate by space or tab
        if ' ' in line:
            line = line.split(' ')
            self._distribute_instruction(line)
        elif '\t' in line:
            line = line.split('\t')
            self._distribute_instruction(line)
        else: # invalid line
            self.errors.append(f'Syntax Error/File {self._file}/Line {self._line}/Invalid Instruction "{line}"')
            self._line = ''

    def _distribute_instruction(self, line):
        """
        This private method is given a list [opcode, operands]
        and distributes it into its approprate class.

        The method does not deal with NOP instructions
        """
        opcode = line[0].strip()
        operands = ''.join(line[1:]).strip()

        if opcode in Macro.call_jmp_instructions:
            self._line = CallJmpInstruction(opcode, operands, self._file, self._line_num)
        elif opcode in Macro.single_operand_instructions:
            self._line = OperandInstruction(opcode, operands, self._file, self._line_num)
        elif opcode in Macro.multi_op_instructions:
            self._line = MultiOpInstruction(opcode, operands, self._file, self._line_num)
        elif opcode in Macro.load_store_instructions:
            self._line = LoadStoreInstruction(opcode, operands, self._file, self._line_num)
        else:
            self.errors.append(f'Definition Error/File {self._file}/Line {self._line_num}/Invalid Opcode "{opcode}"')
            self.error = True
            self._line = ''
            return
        self.instructions += 1

        


    def _handle_label(self, label):
        """
        Private method that handles new labels.
        Validates the label and determines its 
        instruction number, which is just the next instruction.

        Labels come in stripped, blank labels are not allowed.
        Labels must start with a letter and contain only letters,
        numbers, and underscores.
        """

        # ensure no errors somehow got through
        if self.error == True:
            return False
        
        if label in self.labels:
            return False
        
        # check if label valid
        if label == '':
            return False

        # cannot have already been defined and cannot be an opcode, must start with letter
        if label.upper() in Macro.opcodes or label in self.macros or label[0].isalpha() == False:
            return False
        
        for letter in label:
            if letter.isalpha() == False and letter.isdigit() == False and letter != '_':
                return False
        
        label_hex = hex(self.instructions + 1)[2:]
        label_hex = '0' * (4 - len(label_hex)[2:]) + label_hex
        self.labels[label] = label_hex
        return True
        
    
    def handle_data(self):
        """
        This method handles all assembly in the data
        segments. Every line in here must be a pseudo-op.
        Thus, this method simply validates that each line is
        a pseudo-op, and calls the handle_pseudo_op method
        for each valid line
        """

        for line in self.data:
            if line.startswith('#'):
                self._handle_pseudo_op(line)


    def _handle_pseudo_op(self, pseudo_instruction):

        pseudo_instruction = pseudo_instruction.strip()
        if pseudo_instruction == '':
            return
        if pseudo_instruction.startswith('#') == False:
            self.error = True
            self.errors.append(f'Data Seg Error/File {self._file}/Line {self._line_num}/Invalid Data "{pseudo_instruction}"')

        no_operand_pseudos = [
            '#org',
            '#code',
            '#data'
        ]

        # check if operands
        if pseudo_instruction.lower() in no_operand_pseudos:
            if pseudo_instruction.lower() == '#org':
                if self.org == False: self.org = True
                else:  # no duplicate orgs
                    self.errors.append(f'Origin Error/File {self._file}/Line {self._line}/Duplicate Origin')
                    self.error = True
            elif pseudo_instruction.lower() == '#code':
                self.seg = 1
            elif pseudo_instruction.lower() == '#data':
                self.seg = 0
        else:
            # get pseudo-op code and operands
            if ' ' in pseudo_instruction: 
                pseudo_instruction = pseudo_instruction.split(' ')
                self._handle_operand_pseudo_ops(pseudo_instruction[0].strip(), ''.join(pseudo_instruction[1:].strip()))
            elif '\t' in pseudo_instruction:
                pseudo_instruction = pseudo_instruction.split('\t')
                self._handle_operand_pseudo_ops(pseudo_instruction[0].strip(), ''.join(pseudo_instruction[1:].strip()))
            else: 
                self.error = True
                self.errors.append(f'PseudoOp Error/File {self._file}/Line {self._line_num}/Invalid PseudoOp "{pseudo_instruction}"')


    def _handle_operand_pseudo_ops(self, pseudo_opcode, operands, byte_addr=''):
        """
        This private method handles pseudoOps with operands.
        Operands and opcode come in stripped.
        """


        opcodes = [
            '#include',
            '#=',
            '#macro',
            '#byte',
            '#word',
            '#stack'
        ]

        if pseudo_opcode.lower() not in opcodes or operands == '':
            self.error = True
            self.errors.append(f'PseudoOp Error/File {self._file}/Line {self._line_num}/Invalid PseudoOp "{pseudo_opcode} {operands}"')
            return
        
        if pseudo_opcode.lower() == '#include':
            if '"' in operands:
                operands = operands.split('"')
                try: self.include_files.append(operands[1])
                except IndexError:
                    self.error = True
                    self.errors.append(f'PseudoOp Error/File {self._file}/Line {self._line_num}/Invalid File {operands}')
                    return
            elif "'" in operands:
                operands = operands.split("'")
                try: self.include_files.append(operands[1])
                except IndexError:
                    self.error = True
                    self.errors.append(f'PseudoOp Error/File {self._file}/Line {self._line_num}/Invalid File {operands}')
                    return
            else: 
                self.error = True
                self.errors.append(f'PseudoOp Error/File {self._file}/Line {self._line_num}/Invalid File {operands}')
                return
        elif pseudo_opcode.lower() == '#=':
            try: 
                operands = operands[2:].strip()
                operands = operands.split('<-')
                symbol = operands[0].strip()
                self._validate_name(symbol)

                definition = hex_offset(operands[1].strip(), {}, {}, {})
                if definition[2] == True: raise ValueError
                self.symbols[operands[0].strip()] = definition[0]
            except:
                self.error = True
                self.errors.append(f'PseudoOp Error/File {self._file}/Line {self._line_num}/Invalid Definition {operands}')
                return
        elif pseudo_opcode.lower() == '#macro':
            if '(' in operands and ')' in operands: 
                operands = operands.split('(')
                # get rid of closing )
                try: idx = operands[1].index(')')
                except ValueError:
                    self.error = True
                    self.errors.append(f'Macro Error/File {self._file}/Line {self._line_num}/Invalid Args ({line[1]}')
                    return
                args = operands[1][:idx].strip()
                name = operands[0].strip()
                macro = Macro(name, args, self._macro_lines, self._file, self._line_num)
                self.macros[name] = macro
        elif pseudo_opcode.lower() == '#byte':
            allocated_bytes = list(self.bytes.keys())
            try: 
                self._validate_name(operands) 
                if operands in allocated_bytes or f'{operands}[LOW]' in allocated_bytes or f'{operands}[HIGH]' in allocated_bytes: raise ValueError
            except:
                self.error = True
                self.errors.append(f'PseudoOp Error/File {self._file}/Line {self._line_num}/Invalid Byte Name "{operands}"')
                return
            # get address
            if byte_addr != '':
                if self.next_byte == 256:
                    self.error = True
                    self.errors.append(f'Allocation Error/File {self._file}/Line {self._line_num}/Memory Overflow')
                    return
                addr = self.next_byte
                self.next_byte += 1
                addr = hex(addr)[2:]
                addr = '0' * (2 - len(addr)) + addr
                if addr in list(self.bytes.values()):
                    self.error = True
                    self.errors.append(f'Allocation Error/File {self._file}/Line {self._line_num}/Memory Overflow')
                    return
                self.bytes[operands] = addr
            else:
                addr = byte_addr
                if addr in list(self.bytes.values()):
                    self.error = True
                    self.errors.append(f'Allocation Error/File {self._file}/Line {self._line_num}/Memory Overflow')
                    return
                self.bytes[operands] = addr 
        elif pseudo_opcode.lower() == '#word':
            self._handle_operands('#byte', f'{operands}[LOW]')
            self._handle_operands('#byte', f'{operands}[HIGH]')
        else: # must be #stack
            try: 
                stack_size = int(operands)
                if stack_size > 255 or stack_size < 1: raise ValueError
                for byte in range(stack_size - 1):
                    byte_addr = hex(255 - byte)
                    byte_addr = '0' * (2- len(byte_addr)) + byte_addr
                    self._handle_operand_pseudo_ops('#byte', f'$tack{byte}', byte_addr)
                self.stack = True
            except ValueError: 
                self.error = True
                self.errors.append(f'Allocation Error/File {self._file}/Line {self._line_num}/Invalid Stack {operands}')
                return
            
    def _validate_name(self, name):
        """
        Validates the name of a constant.
        """
        if name.upper() in Macro.opcodes or name in self.macros or name[0].isalpha() == False:
            raise ValueError
        for letter in name:
            if letter.isalpha() == False and letter.isdigit() == False and letter != '_':
                raise ValueError


    def hex(self):
        """
        This method converts every line to hex on the second
        pass, and returns it
        """
        if self.error == True:
            return 'ERROR'
        if self._line == '' or self._line == '\n':
            return self._line

        # first check if the line is a macro
        if self._ismacro == True:
            name = self._line[0]
            args = self._line[1]
            if name not in self.macros:
                self.error = True
                self.errors.append(f'Syntax Error/File {self._file}/Line {self._line_num}/Invalid Macro "{name}"')
                return 'ERROR'
            else:
                (hex, num) = self.macros[name].hex(args, self.instructions_hexed, 
                                      self.symbols, self.labels, self.stack, self.bytes)
                self.instructions_hexed = num + 1 # last instruction in macro hexed = num
        else:
            hex = self._line.hex(self.instructions_hexed, self.symbols, 
                                 self.labels, self.stack, self.bytes)
            self.instructions_hexed += 1
        return f'{hex}\n'





    

