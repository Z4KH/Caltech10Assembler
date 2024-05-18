"""
This file is used by pytest to test the Macro class.
"""

from Macro import Macro

def test_macro():
    
    arguments = "p2,o4"
    lines = [
    "DEC",
    "JS label1",
    "IN p2",
    "RLC",
    "SUB X, o4",
    "CLC",
    "JB label6",
    ]
    macro = Macro("macro", arguments, lines, "test", 2)
    arguments = ["0x5f","0x37","0x2b","0xbd"]
    instruction_num = 92
    symbols = []
    labels = {
    'label0': '1D',
    'label1': '5F',
    'label2': '37',
    'label3': '12',
    'label4': '2B',
    'label5': '47',
    'label6': '43',
    }
    hex = macro.hex(arguments, instruction_num, symbols, labels, False, [])
    assert hex == """
    005C 7B00
    005D 9B5F
    005E 9037
    005F 5000
    0060 112B
    0061 07E4
    0062 8FBD
    """

    assert macro._error == False

################################################################################

    # test macro with LD St instructions

    # test macro with jmp call

    # test macro with hex args

    # test macro with symbol table args

    # test macro with non-existent label => error

    # test macro with errors in opcodes => error

    # test macro with errors in arguments => errors

    # test macro with negative memory address => error

    # test macro with char args

    # test macro with allocated memory

    # test macro with non existent allocated memory => error

    # test label in macro => error

    # test final instruction num > 1fff => error



