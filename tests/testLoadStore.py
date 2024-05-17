from MultiOpInstruction.LoadStoreInstruction import LoadStoreInstruction

"""
This file is used to test the LoadStoreInstruction class through pytest.

Revision History:
    Zachary Pestrikov 5/15/2024 Wrote Tests
"""

def test_load_store():
    """
    Function called by pytest to determine whether the LoadStoreInstruction
    class functions properly
    """
    # 10010111oooooooo	LD	X + o
    instruction = LoadStoreInstruction('LD', 'X+4', 'test', 1)
    hex = instruction.hex(42, {}, [], False)
    assert hex == '002A 9704'
    assert instruction._error == False

    # 10010110oooooooo	LD	X+ + o
    instruction = LoadStoreInstruction('LD', 'X++10', 'test', 3)
    hex = instruction.hex(21, {}, [], False)
    assert hex == '0015 960A'
    assert instruction._error == False

    # 10011110oooooooo	LD	X- + o
    instruction = LoadStoreInstruction('LD', 'X- +21', 'test', 3)
    hex = instruction.hex(2, {}, [], False)
    assert hex == '0002 9E15'
    assert instruction._error == False

    # 10000110oooooooo	LD	+X + o
    instruction = LoadStoreInstruction('LD', '+     X  +     21', 'test', 3)
    hex = instruction.hex(255, {'test': 'test'}, [], False)
    assert hex == '00FF 8615'
    assert instruction._error == False

    # 10001110oooooooo	LD	-X + o
    instruction = LoadStoreInstruction('LD', '-     x  +     300', 'test', 3)
    hex = instruction.hex(255, {'test': 'test'}, [], False)
    assert hex == '00FF 8EFF'
    assert instruction._error == False

    # 10010011oooooooo	LD	S + o
    instruction = LoadStoreInstruction('LD', 's  +     100', 'test', 3)
    hex = instruction.hex(255, {'test': 'test'}, [], False)
    assert hex == '00FF 9364'
    assert instruction._error == False

    # 10010010oooooooo	LD	S+ + o
    instruction = LoadStoreInstruction('LD', 'S  +   -  100', 'test', 3)
    hex = instruction.hex(255, {'test': 'test'}, [], False)
    assert hex == '00FF 929C'
    assert instruction._error == False

    # 10011010oooooooo	LD	S- + o
    instruction = LoadStoreInstruction('LD', 'S  -   -  100', 'test', 3)
    hex = instruction.hex(255, {'test': 'test'}, [], False)
    assert hex == '00FF 9A9C'
    assert instruction._error == False
    
    # 10000010oooooooo	LD	+S + o
    instruction = LoadStoreInstruction('LD', '+S +  100', 'test', 3)
    hex = instruction.hex(255, {'test': 'test'}, [], False)
    assert hex == '00FF 8264'
    assert instruction._error == False

    # 10001010oooooooo	LD	-S + o
    instruction = LoadStoreInstruction('LD', '-s + 0x42', 'test', 3)
    hex = instruction.hex(37330, {'test': 'test'}, [], False)
    assert hex == '91D2 8A42'
    assert instruction._error == False

    # 10110111oooooooo	ST	X + o
    instruction = LoadStoreInstruction('ST', 'x + "C"', 'test', 3)
    hex = instruction.hex(37330, {'test': 'test'}, [], False)
    assert hex == '91D2 B743'
    assert instruction._error == False

    # 10110111oooooooo	ST	X + o
    instruction = LoadStoreInstruction('ST', "x + 'c'", 'test', 3)
    hex = instruction.hex(37330, {'test': 'test'}, [], False)
    assert hex == '91D2 B763'
    assert instruction._error == False

    # 10110110oooooooo	ST	X+ + o
    instruction = LoadStoreInstruction('ST', 'X + -240', 'test', 3)
    hex = instruction.hex(37330, {'test': 'test'}, [], False)
    assert hex == '91D2 B680'
    assert instruction._error == False

    # 10111110oooooooo	ST	X- + o
    instruction = LoadStoreInstruction('ST', 'X - -240', 'test', 3)
    hex = instruction.hex(37330, {'test': 'test'}, [], False)
    assert hex == '91D2 BE80'
    assert instruction._error == False

    # 10100110oooooooo	ST	+X + o
    instruction = LoadStoreInstruction('ST', '+X + -240', 'test', 3)
    hex = instruction.hex(37330, {'test': 'test'}, [], False)
    assert hex == '91D2 A680'
    assert instruction._error == False

    # 10101110oooooooo	ST	-X + o
    instruction = LoadStoreInstruction('ST', '-X + test', 'test', 3)
    hex = instruction.hex(37330, {'test': '80'}, [], False)
    assert hex == '91D2 AE80'
    assert instruction._error == False

    # 10110011oooooooo	ST	S + o
    instruction = LoadStoreInstruction('ST', 'S + test', 'test', 3)
    hex = instruction.hex(37330, {'test': '80'}, [], False)
    assert hex == '91D2 B380'
    assert instruction._error == False

    # 10110010oooooooo	ST	S+ + o
    instruction = LoadStoreInstruction('ST', 'S + - test', 'test', 3)
    hex = instruction.hex(37330, {'test': '80'}, [], False)
    assert hex == '91D2 B280'
    assert instruction._error == False

    # 10111010oooooooo	ST	S- + o
    instruction = LoadStoreInstruction('ST', 'S - - test', 'test', 3)
    hex = instruction.hex(37330, {'test': '80'}, [], False)
    assert hex == '91D2 BA80'
    assert instruction._error == False

    # 10100010oooooooo	ST	+S + o
    instruction = LoadStoreInstruction('ST', '+S + test', 'test', 3)
    hex = instruction.hex(37330, {'test': '80'}, [], False)
    assert hex == '91D2 A280'
    assert instruction._error == False

    # 10101010oooooooo	ST	-S + 0
    instruction = LoadStoreInstruction('ST', '-S', 'test', 3)
    hex = instruction.hex(37330, {'test': '80'}, [], False)
    assert hex == '91D2 AA00'
    assert instruction._error == False

    # test errors
    instruction = LoadStoreInstruction('ST', '+S+++', 'test', 3)
    hex = instruction.hex(37330, {'test': '80'}, [], False)
    assert instruction._error == True

    instruction = LoadStoreInstruction('ST', 'gfjgfgf', 'test', 3)
    hex = instruction.hex(37330, {'test': '80'}, [], False)
    assert instruction._error == True

    instruction = LoadStoreInstruction('ST', 'S++-5', 'test', 3)
    hex = instruction.hex(37330, {'test': '80'}, [], False)
    assert instruction._error == False
    assert hex == '91D2 B2FB'

    instruction = LoadStoreInstruction('ST', '', 'test', 3)
    hex = instruction.hex(37330, {'test': '80'}, [], False)
    assert instruction._error == True

    instruction = LoadStoreInstruction('ST', 'S+', 'test', 3)
    hex = instruction.hex(37330, {'test': '80'}, [], False)
    assert hex == '91D2 B200'
    assert instruction._error == False

    instruction = LoadStoreInstruction('ST', '+S', 'test', 3)
    hex = instruction.hex(37330, {'test': '80'}, [], False)
    assert hex == '91D2 A200'
    assert instruction._error == False

    # case sensitive definitions
    instruction = LoadStoreInstruction('ST', '-X + Test', 'test', 3)
    hex = instruction.hex(37330, {'test': '80'}, [], False)
    assert instruction._error == True

    # operand count < 6
    instruction = LoadStoreInstruction('ST', '-X + -Test 5', 'test', 3)
    hex = instruction.hex(37330, {'test': '80'}, [], False)
    assert instruction._error == True

