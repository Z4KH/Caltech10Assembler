"""
This file is used by pytest to test the Macro class.
"""

from Macro import Macro

def test_macro():
    
    arguments = "o3,m5,m7"
    lines = [
    "JNV label0",
    "RLC",
    "JG label2",
    "CMP S, o3",
    "LSR",
    "SBB m5",
    "JNV label6",
    "XOR m7",
    ]
    macro = Macro("macro", arguments, lines, "test", 2)
    arguments = '0x86,0xac,0xf4'
    instruction_num = 1662
    symbols = []
    labels = {
    'label0': '06D4',
    'label1': '060F',
    'label2': '06E6',
    'label3': '0607',
    'label4': '0645',
    'label5': '062F',
    'label6': '06E5',
    'label7': '0679',
    }
    (hex, num) = macro.hex(arguments, instruction_num, symbols, labels, False, [])
    assert hex == """067E A855
067F 5000
0680 AF65
0681 3286
0682 7100
0683 18AC
0684 A860
0685 34F4
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



