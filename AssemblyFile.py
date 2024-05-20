"""
This file implements the AssemblyFile class
"""

import os
from Lines.Line import Line

class AssemblyFile():
    """
    All files included in the program are
    AssemblyFile objects
    """

    errors = []
    lines = []

    def __init__(self, file, start_line):
        """
        Given the path to the main file, 
        this method initializes every line in 
        the file. 
        """
        self._file = file
        self.error = False
        lines = start_line

        # ensure that the file exists
        if os.path.exists(file) == False:
            AssemblyFile.errors.append(f'File Error/File "{file}" Not Found')
            self.error = True
            return

        in_macro = False
        macro_line_ctr = 0
        macro_header = ''
        macro_lines = []
        with open(file) as file:
            for line in file:
                line = line.strip()
                if line.startswith('#macro') or in_macro == True:
                    in_macro == True
                    #handle macro
                    # handle header
                    if macro_line_ctr == 0:
                        macro_header = line
                        macro_line_ctr += 1
                    elif line != '}':
                        macro_lines.append(line)
                        macro_line_ctr += 1
                    else: #end of macro
                        this_line = Line(macro_header, file, lines, macro_lines)
                        AssemblyFile.lines.append(this_line)
                        lines += macro_line_ctr + 1
                        in_macro = False
                        macro_line_ctr = 0
                        macro_lines = []
                    continue
                this_line = Line(line, file, lines, [])
                AssemblyFile.lines.append(this_line)
                lines += 1
        
        self.end_line = lines
    
    def hex(self):

        if self.error == True:
            return 'ERROR'
        output = ''
        for line in AssemblyFile.lines:
            line = line.hex()
            if line == '\n':
                output += line
            else:
                output += f'{line}\n'
        return output