def hex_offset(offset, symbols):
    """
    Given an offset(either a symbol or constant) and a symbols tabel,
    returns the offset in hex if it is proper syntax. Else, it returns
    'ERROR'. This function accounts for negative offsets.

    If the offset is in the symbol table, it assumes that it is already in 
    the proper format(hex without '0x'). Returns a warning if the offset will
    be truncated.
    """
    warning = False
    error = False
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
    elif offset in symbols:
        offset = symbols[offset]
    else:
        # handle converting constant offset to hex
        # cases for offset are dec, hex (0x...), bin(0b...), char, truncation
        if offset[0:2].lower() == '0x':
            try: 
                offset = int(offset, 16)
            except ValueError:
                offset = 'ERROR'
        elif offset[0:2].upper() == '0b':
            try:
                offset = int(offset, 2)
            except ValueError:
                offset = 'ERROR'
        elif offset[0] == "'" or offset[0] == '"':
            if len(offset) != 3:
                offset = 'ERROR'
            else: 
                offset = ord(offset[1])
        else:
            try:
                offset = int(offset)
                if offset < 0:
                    if offset < -128:
                        offset = -128
                        warning = True
                    offset+=256
            except ValueError: # final line of defense against invalide operands
                offset = 'ERROR'
                error = True 
        if offset != 'ERROR':
            if offset > 255:
                offset = 255
                warning = True
            offset = str(hex(offset))[2:]
            offset = '0' * (2-len(offset)) + offset
    return (offset, warning, error)