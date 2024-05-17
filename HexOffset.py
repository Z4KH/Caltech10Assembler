"""
This file contains the function to turn offsets into hexadecimal.

Revision History
    Zachary Pestrikov 5/15/2024 Wrote first draft
    Zachary Pestrikov 5/16/2024 Added Error Handling
    Zachary Pestrikov 5/16/2024 Added support for negative hex/bin offsets with sign extension
"""


def hex_offset(offset, symbols, memory, bytes_table):
    """
    Given an offset(either a symbol or constant) and a symbols tabel,
    returns the offset in hex if it is proper syntax. Else, it returns
    'ERROR'. This function accounts for negative offsets.

    If the offset is in the symbol table, it assumes that it is already in 
    the proper format(hex without '0x'). Returns a warning if the offset will
    be truncated. The function requires that if an offset  is a memory address,
    it is in hex '0x...', and it will issue a warning because the
    user is accessing memory that has not been allocated.
    """
    warning = False
    error = False
    if memory == True and offset[:2].lower() != '0x' and offset not in bytes_table:
        error = True
    if offset == '':
        offset = '00'
    elif offset[0] == '-' and offset[1:] in symbols:
        binary = bin(int(symbols[offset[1:]], 16))[2:] # offset in hex needs invert+1
        offset = ''
        for bit in binary:
            if bit == '0':
                offset += '1'
            else:
                offset += '0'
        offset = hex(int(offset, 2) + 1)[2:]
        offset = '0' * (2-len(offset)) + offset
    elif offset in symbols and memory == False:
        offset = symbols[offset]
    elif offset in bytes_table and memory == True: # it must be either X or S or memory
        offset = bytes_table[offset]
    else:
        # handle converting constant offset to hex
        # cases for offset are dec, hex (0x...), bin(0b...), char, truncation
        if offset[0:2].lower() == '0x': # add hex
            # sign extend
            if memory == True:
                warning = True
            if len(offset) > 2 and len(offset) < 5:
                if int(offset[2], 16) > 7:
                    sign = 'F'
                else:
                    sign = '0'
                offset = '0x' + (sign * (2 - len(offset[2:]))) + offset[2:]
                try: offset = int(offset, 16)
                except ValueError:
                    offset = 'ERROR'
                    error = True
            else:
                offset = 'ERROR'
                error = True
        elif offset[0:3].lower() == '-0x':# subtract hex
            # sign extend
            if len(offset) > 3 and len(offset) < 5:
                if int(offset[3], 16) > 7:
                    sign = 'F'
                else:
                    sign = '0'
                offset = '-0x' + (sign * (2 - len(offset[3:]))) + offset[3:]
                try: 
                    offset = int(offset, 16)
                    offset += 256 # flip bits
                except ValueError:
                    offset = 'ERROR'
                    error = True
            else:
                offset = 'ERROR'
                error = True
        elif offset[0:2].lower() == '0b':
            # sign extend
            if len(offset) > 2 and len(offset) < 11:
                sign = offset[2]
                offset = '0b' + (sign * (8 - len(offset[2:]))) + offset[2:]
                try: offset = int(offset, 2)
                except ValueError:
                    offset = 'ERROR'
                    error = True
            else:
                offset = 'ERROR'
                error = True
        elif offset[0:3].lower() == '-0b':
            # sign extend
            if len(offset) > 3 and len(offset) < 12:
                sign = offset[3]
                offset = '-0b' + (sign * (8 - len(offset[3:]))) + offset[3:]
                # need to flip bits
                try: 
                    offset = int(offset, 2)
                    offset += 256
                except ValueError:
                    offset = 'ERROR'
                    error = True
            else:
                offset = 'ERROR'
                error = True
        elif offset[0] == "'" or offset[0] == '"':
            if len(offset) != 3:
                offset = 'ERROR'
                error = True
            else: 
                offset = ord(offset[1])
        else:
            try:
                offset = int(offset)
            except ValueError: # final line of defense against invalide operands
                offset = 'ERROR'
                error = True 
        if offset != 'ERROR':
            if offset < 0:
                if offset < -128:
                    offset = -128
                    warning = True
                offset+=256
            if offset > 255:
                offset = 255
                warning = True
            offset = str(hex(offset))[2:]
            offset = '0' * (2-len(offset)) + offset
    return (offset, warning, error)