"""
This file is used to test the CallJmpInstruction Class

Revision History
    5/16/2024   Zachary Pestrikov   Added Initial Tests
"""

from CallJmp import CallJmpInstruction

def test_callJmp():
    """
    This function is called by pytest to test the CallJmpInstruction
    class.
    """
    # 10001000rrrrrrrr	JA	r
    instruction = CallJmpInstruction('JA', 'label', 'test', 481510)
    hex = instruction.hex(5555, [],{'label': '153C'}, False)
    assert hex == "15B3 8888"
    assert instruction._error == False


    # 10001100rrrrrrrr	JAE / JNC	r

    instruction = CallJmpInstruction('JAE / JNC', 'label', 'test', 803626)
    hex = instruction.hex(2388, [],{'label': '09CD'}, False)
    assert hex == "0954 8C7A"
    assert instruction._error == False


    # 10001111rrrrrrrr	JB / JC	r

    instruction = CallJmpInstruction('JB / JC', 'label', 'test', 838206)
    hex = instruction.hex(3141, [],{'label': '0BDE'}, False)
    assert hex == "0C45 8F98"
    assert instruction._error == False


    # 10001011rrrrrrrr	JBE	r

    instruction = CallJmpInstruction('JBE', 'label', 'test', 512139)
    hex = instruction.hex(4592, [],{'label': '1D5A'}, False)
    assert instruction._error == True


    # 10011111rrrrrrrr	JE / JZ	r

    instruction = CallJmpInstruction('JE / JZ', 'label', 'test', 772087)
    hex = instruction.hex(7461, [],{'label': '1D5E'}, False)
    assert hex == "1D25 9F3A"
    assert instruction._error == False


    # 10101111rrrrrrrr	JG	r

    instruction = CallJmpInstruction('JG', 'label', 'test', 609803)
    hex = instruction.hex(5089, [],{'label': '1BE4'}, False)
    assert instruction._error == True


    # 10111011rrrrrrrr	JGE	r

    instruction = CallJmpInstruction('JGE', 'label', 'test', 994583)
    hex = instruction.hex(7531, [],{'label': '1DBE'}, False)
    assert hex == "1D6B BB54"
    assert instruction._error == False


    # 10111000rrrrrrrr	JL	r

    instruction = CallJmpInstruction('JL', 'label', 'test', 258451)
    hex = instruction.hex(4175, [],{'label': '1027'}, False)
    assert hex == "104F B8D7"
    assert instruction._error == False


    # 10101100rrrrrrrr	JLE	r

    instruction = CallJmpInstruction('JLE', 'label', 'test', 529085)
    hex = instruction.hex(466, [],{'label': '1B9B'}, False)
    assert instruction._error == True


    # 10011100rrrrrrrr	JNE / JNZ	r

    instruction = CallJmpInstruction('JNE / JNZ', 'label', 'test', 652384)
    hex = instruction.hex(6044, [],{'label': '1CC1'}, False)
    assert instruction._error == True


    # 10011000rrrrrrrr	JNS	r

    instruction = CallJmpInstruction('JNS', 'label', 'test', 256610)
    hex = instruction.hex(660, [],{'label': '0ED9'}, False)
    assert instruction._error == True


    # 10111100rrrrrrrr	JNU	r

    instruction = CallJmpInstruction('JNU', 'label', 'test', 737903)
    hex = instruction.hex(4442, [],{'label': '1193'}, False)
    assert hex == "115A BC3A"
    assert instruction._error == False


    # 10101000rrrrrrrr	JNV	r

    instruction = CallJmpInstruction('JNV', 'label', 'test', 801259)
    hex = instruction.hex(2755, [],{'label': '0ADE'}, False)
    assert hex == "0AC3 A81C"
    assert instruction._error == False


    # 10011011rrrrrrrr	JS	r

    instruction = CallJmpInstruction('JS', 'label', 'test', 553769)
    hex = instruction.hex(572, [],{'label': '0241'}, False)
    assert hex == "023C 9B06"
    assert instruction._error == False


    # 10111111rrrrrrrr	JU	r

    instruction = CallJmpInstruction('JU', 'label', 'test', 994917)
    hex = instruction.hex(152, [],{'label': '0079'}, False)
    assert hex == "0098 BFE0"
    assert instruction._error == False


    # 10101011rrrrrrrr	JV	r
    instruction = CallJmpInstruction('JV', 'label', 'test', 310415)
    hex = instruction.hex(5410, [],{'label': '1597'}, False)
    assert hex == "1522 AB76"
    assert instruction._error == False

    # label DNE
    instruction = CallJmpInstruction('JV', 'label', 'test', 310415)
    hex = instruction.hex(5410, [],{}, False)
    assert instruction._error == True

    # jmp
    instruction = CallJmpInstruction('JMP', 'label', 'test', 310415)
    hex = instruction.hex(5410, [],{'label': '1597'}, False)
    assert hex == "D597"
    assert instruction._error == False

    # call
    instruction = CallJmpInstruction('CALL', 'label', 'test', 310415)
    hex = instruction.hex(5410, [],{'label': '1597'}, True)
    assert hex == "F597"
    assert instruction._error == False

    # call no stack
    instruction = CallJmpInstruction('CALL', 'label', 'test', 310415)
    hex = instruction.hex(5410, [],{'label': '1597'}, False)
    assert instruction._error == True