"""
This is the top level file for
the Caltech10 Assembler.
"""

import sys
from AssemblyFile import AssemblyFile

def assemble():
    """
    This method begins assembly.
    """
    args = sys.argv

    # main_file = args[1]
    main_file = 'gcdEuclidCaltech10.asm'#removewhendone
    file = AssemblyFile(main_file, 0)
    with open('out.txt', 'w') as out:
        out.write(file.hex().strip()) 



if __name__ == '__main__':
    assemble()