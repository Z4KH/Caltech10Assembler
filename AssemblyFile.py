"""
This file implements the AssemblyFile class
"""

import os
from Lines.Line import Line
from Lines.Instructions.Instruction import Instruction

class AssemblyFile():
    """
    All files included in the program are
    AssemblyFile objects
    """

    errors = []
    lines = []
    line_cnt = 1    # files are 1-indexed

    def __init__(self, file):
        """
        Given the path to the main file, 
        this method initializes every line in 
        the file. 
        """
        self._file = file
        self.error = False

        # ensure that the file exists
        if os.path.exists(file) == False:
            AssemblyFile.errors.append(f'File Error/File "{file}" Not Found')
            self.error = True
            return
        if file not in Line.include_files:
            Line.include_files.append(file) # the file exists
        in_macro = False
        macro_line_ctr = 0
        macro_header = ''
        macro_lines = []
        with open(file) as asm_file:
            for line in asm_file:
                line = line.strip()
                if line.startswith('#macro') or in_macro == True:
                    in_macro = True
                    #handle macro
                    # handle header
                    if macro_line_ctr == 0:
                        macro_header = line
                        macro_line_ctr += 1
                    elif line != '}':
                        macro_lines.append(line)
                        macro_line_ctr += 1
                    else: #end of macro
                        this_line = Line(macro_header, file, self.line_cnt, macro_lines)
                        AssemblyFile.lines.append(this_line)
                        self.line_cnt += macro_line_ctr + 1
                        in_macro = False
                        macro_line_ctr = 0
                        macro_lines = []
                    continue
                this_line = Line(line, file, self.line_cnt, [])
                AssemblyFile.lines.append(this_line)
                self.line_cnt += 1
        # must add no-op at end of each file in case of includes and jumps and preorg
        AssemblyFile.lines.append(Line('#code', '-1', -1, []))
        AssemblyFile.lines.append(Line('NOP', '-1', -1, []))
        self.line_cnt += 1
    
    def handle_preOrg(self):
        """
        This method is called after parsing the file
        with #org in it. It handles all
        lines before the orgin and addes them to 
        the lines array
        """
        Line.seg = 1 # all lines in here are instructions
        lines = self.lines[0].handle_preOrg()
        for line in lines:
            AssemblyFile.lines.append(line)
        # must add no-op at end of each file in case of includes and jumps and preorg
        AssemblyFile.lines.append(Line('#code', '-1', -1, []))
        AssemblyFile.lines.append(Line('NOP', '-1', -1, []))


def hex():
    if Line.org == False:
        AssemblyFile.errors.append(f'Origin Error/#ORG Unspecified')
        return 'ERROR'
    output = ''
    for line in AssemblyFile.lines:
        if line.error == True:
            output += 'ERROR'
        else:
            line = line.hex()
            if line == '\n':
                output += line
            elif line != '':
                output += f'{line.strip()}\n'

    if Instruction.ret == False:
        AssemblyFile.errors.append(f'Return Error/No Return in Program')
    # now hex the lines before org
    return output