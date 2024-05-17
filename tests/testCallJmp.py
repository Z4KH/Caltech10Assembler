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

    instruction = CallJmpInstruction('JA', 'label', 'test', 21100)
    hex = instruction.hex(1267, [],{'label': '0521'}, False, {})
    assert hex == "04F3 882F"
    assert instruction._error == False


    # 10001100rrrrrrrr	JAE / JNC	r

    instruction = CallJmpInstruction('JAE', 'label', 'test', 756755)
    hex = instruction.hex(787, [],{'label': '0649'}, False, {})
    assert instruction._error == True


    # 10001100rrrrrrrr	JAE / JNC	r

    instruction = CallJmpInstruction('JNC', 'label', 'test', 756755)
    hex = instruction.hex(787, [],{'label': '0649'}, False, {})
    assert instruction._error == True


    # 10001111rrrrrrrr	JB / JC	r

    instruction = CallJmpInstruction('JB', 'label', 'test', 724567)
    hex = instruction.hex(6568, [],{'label': '1976'}, False, {})
    assert hex == "19A8 8FCD"
    assert instruction._error == False


    # 10001111rrrrrrrr	JB / JC	r

    instruction = CallJmpInstruction('JC', 'label', 'test', 724567)
    hex = instruction.hex(6568, [],{'label': '1976'}, False, {})
    assert hex == "19A8 8FCD"
    assert instruction._error == False


    # 10001011rrrrrrrr	JBE	r

    instruction = CallJmpInstruction('JBE', 'label', 'test', 581778)
    hex = instruction.hex(1467, [],{'label': '1ECF'}, False, {})
    assert instruction._error == True


    # 10011111rrrrrrrr	JE / JZ	r

    instruction = CallJmpInstruction('JE', 'label', 'test', 801828)
    hex = instruction.hex(6548, [],{'label': '19F3'}, False, {})
    assert hex == "1994 9F60"
    assert instruction._error == False


    # 10011111rrrrrrrr	JE / JZ	r

    instruction = CallJmpInstruction('JZ', 'label', 'test', 801828)
    hex = instruction.hex(6548, [],{'label': '19F3'}, False, {})
    assert hex == "1994 9F60"
    assert instruction._error == False


    # 10101111rrrrrrrr	JG	r

    instruction = CallJmpInstruction('JG', 'label', 'test', 184235)
    hex = instruction.hex(4211, [],{'label': '10AF'}, False, {})
    assert hex == "1073 AF3D"
    assert instruction._error == False


    # 10111011rrrrrrrr	JGE	r

    instruction = CallJmpInstruction('JGE', 'label', 'test', 718494)
    hex = instruction.hex(3144, [],{'label': '1272'}, False, {})
    assert instruction._error == True


    # 10111000rrrrrrrr	JL	r

    instruction = CallJmpInstruction('JL', 'label', 'test', 397189)
    hex = instruction.hex(3591, [],{'label': '0E36'}, False, {})
    assert hex == "0E07 B830"
    assert instruction._error == False


    # 10101100rrrrrrrr	JLE	r

    instruction = CallJmpInstruction('JLE', 'label', 'test', 553833)
    hex = instruction.hex(522, [],{'label': '01DE'}, False, {})
    assert hex == "020A ACD3"
    assert instruction._error == False


    # 10011100rrrrrrrr	JNE / JNZ	r

    instruction = CallJmpInstruction('JNE', 'label', 'test', 625769)
    hex = instruction.hex(5126, [],{'label': '13B0'}, False, {})
    assert hex == "1406 9CA9"
    assert instruction._error == False


    # 10011100rrrrrrrr	JNE / JNZ	r

    instruction = CallJmpInstruction('JNZ', 'label', 'test', 625769)
    hex = instruction.hex(5126, [],{'label': '13B0'}, False, {})
    assert hex == "1406 9CA9"
    assert instruction._error == False


    # 10011000rrrrrrrr	JNS	r

    instruction = CallJmpInstruction('JNS', 'label', 'test', 938618)
    hex = instruction.hex(2892, [],{'label': '1AAA'}, False, {})
    assert instruction._error == True


    # 10111100rrrrrrrr	JNU	r

    instruction = CallJmpInstruction('JNU', 'label', 'test', 463622)
    hex = instruction.hex(1944, [],{'label': '07A4'}, False, {})
    assert hex == "0798 BC0D"
    assert instruction._error == False


    # 10101000rrrrrrrr	JNV	r

    instruction = CallJmpInstruction('JNV', 'label', 'test', 320947)
    hex = instruction.hex(970, [],{'label': '1DE1'}, False, {})
    assert instruction._error == True


    # 10011011rrrrrrrr	JS	r

    instruction = CallJmpInstruction('JS', 'label', 'test', 273668)
    hex = instruction.hex(7628, [],{'label': '1FE3'}, False, {})
    assert instruction._error == True


    # 10111111rrrrrrrr	JU	r

    instruction = CallJmpInstruction('JU', 'label', 'test', 324467)
    hex = instruction.hex(269, [],{'label': '010B'}, False, {})
    assert hex == "010D BFFD"
    assert instruction._error == False


    # 10101011rrrrrrrr	JV	r
    instruction = CallJmpInstruction('JV', 'label', 'test', 846373)
    hex = instruction.hex(8155, [],{'label': '1F85'}, False, {})
    assert hex == "1FDB ABA9"
    assert instruction._error == False

#########################################################################
    # label DNE
    instruction = CallJmpInstruction('JV', 'label', 'test', 310415)
    hex = instruction.hex(5410, [],{}, False, {})
    assert instruction._error == True

    # jmp
    instruction = CallJmpInstruction('JMP', 'label', 'test', 310415)
    hex = instruction.hex(5410, [],{'label': '1597'}, False, {})
    assert hex == "1522 D597"
    assert instruction._error == False

    # call
    instruction = CallJmpInstruction('CALL', 'label', 'test', 310415)
    hex = instruction.hex(5410, [],{'label': '1597'}, True, {})
    assert hex == "1522 F597"
    assert instruction._error == False

    # call no stack
    instruction = CallJmpInstruction('CALL', 'label', 'test', 310415)
    hex = instruction.hex(5410, [],{'label': '1597'}, False, {})
    assert instruction.errors[len(instruction.errors) - 1][0] == 'S'
