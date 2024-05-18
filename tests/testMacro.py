"""
This file is used by pytest to test the Macro class.
"""

from Macro import Macro

def test_macro():
    
    arguments = "o4,o5,o6,o8,m10"
    lines = [
    "INX",
    "DES",
    "JU label2",
    "DEX",
    "SUB X, o4",
    "OR S, o5",
    "XOR S, o6",
    "LSL",
    "AND X, o8",
    "NOT",
    "LDD m10",
    "CLI",
    "PUSHF",
    "STC",
    ]
    macro = Macro("macro", arguments, lines, "test", 2)
    arguments = ["e2","96","e5","d4","7b","d5"]
    instruction_num = 1635
    symbols = []
    labels = {
    'label0': '32',
    'label1': '23',
    'label2': '1E',
    'label3': '33',
    'label4': '6A',
    'label5': '1B',
    'label6': '2C',
    'label7': '78',
    'label8': '7B',
    'label9': '12',
    'label10': '2B',
    'label11': '03',
    'label12': '2E',
    'label13': '79',
    }
    hex = macro.hex(arguments, instruction_num, symbols, labels, False, [])
    assert hex == """
    0664 0580
    0665 0E40
    0666 BFE2
    0667 0D80
    0668 1196
    0669 76E5
    066A 36D4
    066B 5800
    066C 457B
    066D 2D00
    066E 80D5
    066F 0769
    0670 0E00
    0671 7F0C
    """
    assert macro._error == False

    arguments = "o2,o4,m5,k6,m7,p8,o9,m10,o11,o12,m14,m15"
    lines = [
    "JV label0",
    "INC",
    "OR X, o2",
    "JNU label3",
    "SUB S, o4",
    "STD m5",
    "TSTI k6",
    "SUB m7",
    "IN p8",
    "OR S, o9",
    "OR m10",
    "SUB S, o11",
    "TST S, o12",
    "TXA",
    "OR m14",
    "STD m15",
    "RRC",
    ]
    macro = Macro("macro", arguments, lines, "test", 2)
    arguments = ["4f","39","79","46","fa","41","7d","69","f8","e4","f0","73","cb","48"]
    instruction_num = 1831
    symbols = []
    labels = {
    'label0': '4F',
    'label1': '1B',
    'label2': '39',
    'label3': '79',
    'label4': '46',
    'label5': 'X6',
    'label6': '41',
    'label7': '7D',
    'label8': '69',
    'label9': 'X8',
    'label10': '1C',
    'label11': '10',
    'label12': '73',
    'label13': '7D',
    'label14': '35',
    'label15': '48',
    'label16': '7A',
    }
    hex = macro.hex(arguments, instruction_num, symbols, labels, False, [])
    assert hex == """
    0728 AB4F
    0729 0000
    072A 7539
    072B BC79
    072C 1246
    072D A0FA
    072E 4F41
    072F 107D
    0730 9069
    0731 76F8
    0732 74E4
    0733 12F0
    0734 4E73
    0735 6701
    0736 74CB
    0737 A048
    0738 7103
    """
    assert macro._error == False

    arguments = "o0,m1"
    lines = [
    "XOR S, o0",
    "XOR m1",
    "JG label2",
    "PUSHF",
    "JS label4",
    "INS",
    "JAE label6",
    "NOT",
    ]
    macro = Macro("macro", arguments, lines, "test", 2)
    arguments = ["06","a6","4c","97","cd"]
    instruction_num = 7700
    symbols = []
    labels = {
    'label0': '06',
    'label1': '5A',
    'label2': '4C',
    'label3': '26',
    'label4': '69',
    'label5': '24',
    'label6': '33',
    'label7': 'X5',
    }
    hex = macro.hex(arguments, instruction_num, symbols, labels, False, [])
    assert hex == """
    1E15 3606
    1E16 34A6
    1E17 AF4C
    1E18 0E00
    1E19 9B97
    1E1A 0640
    1E1B 8CCD
    1E1C 2D00
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

