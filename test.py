def _validate_operands(operands):
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
        error = f'bruh'
        operand_list = {
            'register': '',
            '+/-': '',
            'pre/post': '',
            'offset': ''
        }
        # first character is either +,-,X,S
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
                    operand_list['operand'] = operands[1:]
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

        print(error)

_validate_operands('+X+4')