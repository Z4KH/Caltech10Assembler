"""
This is the top level file for
the Caltech10 Assembler.
"""

import sys
from AssemblyFile import AssemblyFile
from Lines.Line import Line
from Lines.Macro import Macro
from Lines.Instructions.Instruction import Instruction
from AssemblyFile import hex
import os

def assemble():
    """
    This method begins assembly.
    """
    files = [] #files to hex
    args = sys.argv

    if len(args) != 2:
        print(f'File Error/Unspecified Assembly File')
        return
    main_file_name = args[1]
    files.append(AssemblyFile(main_file_name))

    # get main_file_name
    if files[0].error == False:
        cwd = os.getcwd()
        out_file = f'{os.path.relpath(main_file_name, cwd)}.obj'
    else: # files must have the .
        print(f'\n{AssemblyFile.errors[0]}\n')
        return

    org = Line.org
    if org == True:
        files[0].handle_preOrg()
    # handle includes
    while(len(files) < len(Line.include_files)):
        files.append(AssemblyFile(Line.include_files[len(files)]))
        if AssemblyFile.errors != [] or Line.errors != [] or Macro.errors != []: 
            # if the file has errors, dont loop forever
            break
        test = Line.org
        if Line.org == True and org == False:
            files[0].handle_preOrg()
            org = True

    #hex all files and output
    hex_output = hex()

    with open(out_file, 'w') as out:
        out.write(f'{hex_output.strip()}\n')
    
    print('\n')
    # now print all errors
    for error in AssemblyFile.errors:
        print(error.strip())
    for error in Line.errors:
        print(error.strip())
    for error in Instruction.errors:
        print(error.strip())
    for error in Macro.errors:
        print(error.strip())

    # print addresses of bytes allocated
    print('\n')
    if Line.bytes != {}:
        print('Bytes Allocated:')
        for (byte, addr) in Line.bytes.items():
            if byte.startswith('$') == False:
                print(f'Byte {byte}: {addr}')
        print('\n')
    print(f'Assembled Obj File at "{out_file}"')

    



if __name__ == '__main__':
    try: assemble()
    except: print('Assembly Failed')