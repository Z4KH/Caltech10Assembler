"""
This file is used to test the CallJmpInstruction Class

Revision History
    5/16/2024   Zachary Pestrikov   Added Initial Tests
"""

from Lines.Instructions.OperandInstructions.CallJmp import CallJmpInstruction

def test_callJmp():
    """
    This function is called by pytest to test the CallJmpInstruction
    class.
    """
    # 10001000rrrrrrrr	JA	r

    instruction = CallJmpInstruction('JA', 'label', 'test', 111039)
    hex = instruction.hex(6059, [],{'label': '1C7B'}, False, [])
    assert instruction.error == True


    # 10001100rrrrrrrr	JAE	r

    instruction = CallJmpInstruction('JAE', 'label', 'test', 670726)
    hex = instruction.hex(1696, [],{'label': '0C05'}, False, [])
    assert instruction.error == True


    # 10001111rrrrrrrr	JB	r

    instruction = CallJmpInstruction('JB', 'label', 'test', 318025)
    hex = instruction.hex(2536, [],{'label': '0A11'}, False, [])
    assert hex == "09E8 8F28"
    assert instruction.error == False


    # 10001011rrrrrrrr	JBE	r

    instruction = CallJmpInstruction('JBE', 'label', 'test', 882829)
    hex = instruction.hex(2886, [],{'label': '165E'}, False, [])
    assert instruction.error == True


    # 10011111rrrrrrrr	JE	r

    instruction = CallJmpInstruction('JE', 'label', 'test', 788429)
    hex = instruction.hex(1294, [],{'label': '054A'}, False, [])
    assert hex == "050E 9F3B"
    assert instruction.error == False


    # 10101111rrrrrrrr	JG	r

    instruction = CallJmpInstruction('JG', 'label', 'test', 988640)
    hex = instruction.hex(4548, [],{'label': '116A'}, False, [])
    assert hex == "11C4 AFA5"
    assert instruction.error == False


    # 10111011rrrrrrrr	JGE	r

    instruction = CallJmpInstruction('JGE', 'label', 'test', 802612)
    hex = instruction.hex(5025, [],{'label': '1E36'}, False, [])
    assert instruction.error == True


    # 10111000rrrrrrrr	JL	r

    instruction = CallJmpInstruction('JL', 'label', 'test', 455700)
    hex = instruction.hex(1574, [],{'label': '1BBD'}, False, [])
    assert instruction.error == True


    # 10101100rrrrrrrr	JLE	r

    instruction = CallJmpInstruction('JLE', 'label', 'test', 109675)
    hex = instruction.hex(4786, [],{'label': '1D73'}, False, [])
    assert instruction.error == True


    # 10011100rrrrrrrr	JNE	r

    instruction = CallJmpInstruction('JNE', 'label', 'test', 994064)
    hex = instruction.hex(5029, [],{'label': '1398'}, False, [])
    assert hex == "13A5 9CF2"
    assert instruction.error == False


    # 10011000rrrrrrrr	JNS	r

    instruction = CallJmpInstruction('JNS', 'label', 'test', 85374)
    hex = instruction.hex(2780, [],{'label': '0A62'}, False, [])
    assert hex == "0ADC 9885"
    assert instruction.error == False


    # 10111100rrrrrrrr	JNU	r

    instruction = CallJmpInstruction('JNU', 'label', 'test', 83006)
    hex = instruction.hex(2962, [],{'label': '0BE6'}, False, [])
    assert hex == "0B92 BC53"
    assert instruction.error == False


    # 10101000rrrrrrrr	JNV	r

    instruction = CallJmpInstruction('JNV', 'label', 'test', 346182)
    hex = instruction.hex(2933, [],{'label': '0B58'}, False, [])
    assert hex == "0B75 A8E2"
    assert instruction.error == False


    # 10011011rrrrrrrr	JS	r

    instruction = CallJmpInstruction('JS', 'label', 'test', 427849)
    hex = instruction.hex(6853, [],{'label': '1E1C'}, False, [])
    assert instruction.error == True


    # 10111111rrrrrrrr	JU	r

    instruction = CallJmpInstruction('JU', 'label', 'test', 158364)
    hex = instruction.hex(1825, [],{'label': '0733'}, False, [])
    assert hex == "0721 BF11"
    assert instruction.error == False


    # 10101011rrrrrrrr	JV	r
    instruction = CallJmpInstruction('JV', 'label', 'test', 561070)
    hex = instruction.hex(7348, [],{'label': '1F41'}, False, [])
    assert instruction.error == True



#########################################################################
    # label DNE
    instruction = CallJmpInstruction('JV', 'label', 'test', 310415)
    hex = instruction.hex(5410, [],{}, False, {})
    assert instruction.error == True

    # jmp
    instruction = CallJmpInstruction('JMP', 'label', 'test', 310415)
    hex = instruction.hex(5410, [],{'label': '1597'}, False, {})
    assert hex == "1522 D597"
    assert instruction.error == False

    # call
    instruction = CallJmpInstruction('CALL', 'label', 'test', 310415)
    hex = instruction.hex(5410, [],{'label': '1597'}, True, {})
    assert hex == "1522 F597"
    assert instruction.error == False

    # call no stack
    instruction = CallJmpInstruction('CALL', 'label', 'test', 310415)
    hex = instruction.hex(5410, [],{'label': '1597'}, False, {})
    assert instruction.errors[len(instruction.errors) - 1][0] == 'S'

    # call pc
    instruction = CallJmpInstruction('CALL', '$', 'test', 310415)
    hex = instruction.hex(3, [],{'label': '1597'}, False, {})
    assert hex == '0003 E003'

    # JMP pc
    instruction = CallJmpInstruction('JMP', '$', 'test', 310415)
    hex = instruction.hex(2, [],{'label': '1597'}, False, {})
    assert hex == '0002 C002'

    # RJMP pc
    instruction = CallJmpInstruction('JZ', '$', 'test', 310415)
    hex = instruction.hex(0, [],{'label': '1597'}, False, {})
    assert hex == '0000 9FFF'
