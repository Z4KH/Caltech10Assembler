"""
This file is used by pytest to test the Macro class.
"""

from Lines.Macro import Macro

hex1 = """067E A855
067F 5000
0680 AF65
0681 3286
0682 7100
0683 18AC
0684 A860
0685 34F4
"""

hex2 = """1502 4E04
1503 6700
1504 5000
1505 181C
1506 90FB
1507 07E4
1508 3722
1509 11D6
150A 779F
150B BF04
150C 7102
150D 7102
150E B0D9
150F A00A
1510 46C4
1511 9CEF
"""

hex3 = """0336 7F0C
0337 80E8
0338 4F9D
0339 7101

033A 7F81
033B 1815
"""

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
    assert hex == hex1
    assert macro.error == False
    assert num == 1669



    arguments = "o0,m3,p4,k6,o7,k8,p12,m13,o14"
    lines = [
    "TST S, o0",
    "TSA",
    "RLC",
    "SBB m3",
    "IN p4",
    "CLC",
    "XORI k6",
    "SUB X, o7",
    "ORI k8",
    "JU label9",
    "ROR",
    "ROR",
    "OUT p12",
    "STD m13",
    "AND S, o14",
    "JNE label15",
    ]
    macro = Macro("macro2", arguments, lines, "test", 2)
    arguments = "0x04,0x1c,0xfb,0x22,0xd6,0x9f,0xd9,0x0a,0xc4"
    instruction_num = 5378
    symbols = []
    labels = {
    'label0': '1506',
    'label1': '14A8',
    'label2': '14BA',
    'label3': '1521',
    'label4': '1501',
    'label5': '1510',
    'label6': '152A',
    'label7': '14DF',
    'label8': '14A9',
    'label9': '1510',
    'label10': '1550',
    'label11': '14E0',
    'label12': '14E7',
    'label13': '1519',
    'label14': '14D4',
    'label15': '1501',
    }
    (hex, num) = macro.hex(arguments, instruction_num, symbols, labels, False, [])
    assert hex == hex2

    assert macro.error == False
    assert num == instruction_num + 15


    arguments = "o0,o2"
    lines = [
    "SBB X, o0",
    "NOT",
    "TST X, o2",
    "RRC",
    "JBE label4",
    "JNV label5",
    ]
    macro = Macro("macro3", arguments, lines, "test", 2)
    arguments = "0x55,0xec"
    instruction_num = 6798
    symbols = []
    labels = {
    'label0': '1AE3',
    'label1': '1AB0',
    'label2': '1A7C',
    'label3': '1A9D',
    'label4': '1AAE',
    'label5': '1AC1',
    }
    (hex, num) = macro.hex(arguments, instruction_num, symbols, labels, False, [])
    assert hex == """1A8E 1955
1A8F 2D00
1A90 4DEC
1A91 7103
1A92 8B1B
1A93 A82D
"""

    assert macro.error == False
    assert num == instruction_num + 5


#################################################################################

    # test macro with blank line outputs blank line
    arguments = "m1,k2,m5"
    lines = [
    "STC",
    "LDD m1",
    "TSTI k2",
    "ASR",
    "",
    "STI",
    "SBB m5",
    ]
    macro = Macro("macro4", arguments, lines, "test", 2)
    arguments = "0xe8,0x9d,0x15"
    instruction_num = 822
    symbols = []
    labels = {
    'label0': '02F1',
    'label1': '031F',
    'label2': '02D5',
    'label3': '02FB',
    'label4': '032E',
    'label5': '0350',
    }
    (hex, num) = macro.hex(arguments, instruction_num, symbols, labels, False, [])
    assert hex == hex3

    assert macro.error == False
    assert num == instruction_num + 5

    # test macro with LD St instructions
    arguments = "o3,k5,o6,o7"
    lines = [
    "JNE label0",
    "PUSHF",
    "JNU label2",
    "XOR S, o3",
    "JGE label4",
    "LDI k5",
    "CMP S, o6",
    "OR X, o7",
    "LD X + o7"
    ]
    macro5 = Macro("macro5", arguments, lines, "test", 2)
    arguments = "0x90,0x76,0xdd,0x01"
    instruction_num = 7797
    symbols = []
    labels = {
    'label0': '1EBF',
    'label1': '1E49',
    'label2': '1EF4',
    'label3': '1E08',
    'label4': '1ED3',
    'label5': '1EF0',
    'label6': '1E58',
    'label7': '1E7D',
    }
    (hex, num) = macro5.hex(arguments, instruction_num, symbols, labels, False, [])
    assert hex == """1E75 9C49
1E76 0E00
1E77 BC7C
1E78 3690
1E79 BB59
1E7A 8976
1E7B 32DD
1E7C 7501
1E7D 9701
"""

    assert macro.error == False
    assert num == instruction_num + 8

    # test macro with jmp call
    arguments = "m0,k4,o6"
    lines = [
    "TST m0",
    "INX",
    "RLC",
    "NOP",
    "ORI k4",
    "JNS label5",
    "XOR S, o6",
    "DEX",
    "JMP label7",
    "CALL label0"
    ]
    macro6 = Macro("macro6", arguments, lines, "test", 2)
    arguments = "0x41,0x6e,0x9e"
    instruction_num = 673
    symbols = []
    labels = {
    'label0': '02E2',
    'label1': '0241',
    'label2': '0263',
    'label3': '027D',
    'label4': '0313',
    'label5': '0236',
    'label6': '0245',
    'label7': '029A',
    }
    (hex, num) = macro6.hex(arguments, instruction_num, symbols, labels, False, [])
    assert hex == """02A1 4C41
02A2 0580
02A3 5000
02A4 1F80
02A5 776E
02A6 988F
02A7 369E
02A8 0D80
02A9 C29A
02AA E2E2
"""

    assert macro6.error == False
    assert num == instruction_num + 9


    # test macro without hex args
    arguments = "o0,o1,m5,o10,m12"
    lines = [
    "CMP X, o0",
    "SBB S, o1",
    "JL label2",
    "CLU",
    "JE label4",
    "OR m5",
    "STC",
    "LSR",
    "RTS",
    "POPF",
    "XOR X, o10",
    "PUSHF",
    "OR m12",
    "POPF",
    "NEG",
    ]
    macro7 = Macro("macro7", arguments, lines, "test", 2)
    arguments = "'Ð',13,0x81,0b00111010,0xd4"
    instruction_num = 6255
    symbols = []
    labels = {
    'label0': '183F',
    'label1': '187D',
    'label2': '180A',
    'label3': '18C9',
    'label4': '1887',
    'label5': '17F5',
    'label6': '18D9',
    'label7': '182D',
    'label8': '18E0',
    'label9': '18B1',
    'label10': '18B3',
    'label11': '186F',
    'label12': '184F',
    'label13': '18AB',
    'label14': '1880',
    }
    (hex, num) = macro7.hex(arguments, instruction_num, symbols, labels, False, [])
    assert hex == """186F 31D0
1870 1A0D
1871 B898
1872 07CA
1873 9F13
1874 7481
1875 7F0C
1876 7100
1877 1F00
1878 0200
1879 353A
187A 0E00
187B 74D4
187C 0200
187D 2700
"""

    assert macro.error == False
    assert instruction_num + 14 == num

    # test macro with symbol table args => should choose macro arg, not symbol 
    arguments = "m0,o1,m4,m5"
    lines = [
    "SBB m0",
    "SBB S, o1",
    "TAS",
    "TSA",
    "CMP m4",
    "CMP m5",
    "JU label6",
    ]
    macro8 = Macro("macro8", arguments, lines, "test", 2)
    arguments = "0x22,0x05,0x27,0xf3"
    instruction_num = 5662
    symbols = {'m0': '00'}
    labels = {
    'label0': '1640',
    'label1': '1624',
    'label2': '1607',
    'label3': '1605',
    'label4': '1649',
    'label5': '1616',
    'label6': '160B',
    }
    (hex, num) = macro8.hex(arguments, instruction_num, symbols, labels, False, [])
    assert hex == """161E 1822
161F 1A05
1620 0750
1621 6700
1622 3027
1623 30F3
1624 BFE6
"""

    assert macro8.error == False
    assert num == instruction_num + 6

    # test macro with errors in opcodes => error
    arguments = "k1,k2,p5,m6,o8,o9"
    lines = [
    "NEG",
    "SBBI k1",
    "ORIW k2",
    "INS",
    "NEG",
    "OUT p5",
    "OR m6",
    "JB label7",
    "OR S, o8",
    "OR S, o9",
    "LSL",
    ]
    macro9 = Macro("macro9", arguments, lines, "test", 2)
    arguments = "0x6b,0x04,0x47,0x7f,0x44,0x01"
    instruction_num = 1733
    symbols = []
    labels = {
    'label0': '06A5',
    'label1': '0731',
    'label2': '06CB',
    'label3': '06E8',
    'label4': '0693',
    'label5': '0711',
    'label6': '074A',
    'label7': '06BE',
    'label8': '0711',
    'label9': '06CF',
    'label10': '06AE',
    }
    (hex, num) = macro9.hex(arguments, instruction_num, symbols, labels, False, [])

    assert macro9.error == True

    # test macro with duplicate init arguments => errors
    arguments = "o4,o4"
    lines = [
    "JLE label0",
    "STC",
    "JGE label2",
    "OR S, o3",
    "XOR S, o4",
    "CLU",
    ]
    macro10 = Macro("macro10", arguments, lines, "test", 2)
    arguments = "0x0e,0x94"
    instruction_num = 4096
    symbols = []
    labels = {
    'label0': '0FF4',
    'label1': '0F8F',
    'label2': '1001',
    'label3': '1011',
    'label4': '0F98',
    'label5': '1063',
    }
    (hex, num) = macro10.hex(arguments, instruction_num, symbols, labels, False, [])

    assert macro10.error == True

    # test macro with allocated memory and comments and spaces between operands
    arguments = "k1,    m3, o4,k6   ,o9,k11 "
    lines = [
    "ASR",
    "ORI k1; comment",
    "STI",
    "XOR m3",
    "XOR S, o4  ; comment",
    "NOP",
    "XORI k6",
    "INS",
    "JV label8  ; comment",
    "AND S, o9",
    "LSR",
    "SUBI k11",
    ]
    macro11 = Macro("macro11", arguments, lines, "test", 2)
    arguments = "0x1f,memory,0x3e,0x6d,0x30,0x87"
    instruction_num = 3592
    symbols = []
    labels = {
    'label0': '0DD5',
    'label1': '0E28',
    'label2': '0E4D',
    'label3': '0D9C',
    'label4': '0E4A',
    'label5': '0DEB',
    'label6': '0E7B',
    'label7': '0DD7',
    'label8': '0E60',
    'label9': '0E41',
    'label10': '0DF8',
    'label11': '0D9A',
    }
    print(macro11.error)
    print(macro11._lines)
    (hex, num) = macro11.hex(arguments, instruction_num, symbols, labels, False, {'memory': '91'})
    assert hex == """0E08 7101
0E09 771F
0E0A 7F81
0E0B 3491
0E0C 363E
0E0D 1F80
0E0E 376D
0E0F 0640
0E10 AB4F
0E11 4630
0E12 7100
0E13 1387
"""

    assert macro11.error == False
    assert num == instruction_num + 11

    # test label in macro => error
    arguments = "m0,o3,o5,m10,o11,o12"
    lines = [
    "AND m0",
    "ROR",
    "INC",
    "SUB S, o3",
    "LSR",
    "XOR S, o5",
    "label: RRC",
    "POPF",
    "POPF",
    "JA label9",
    "CMP m10",
    "SUB S, o11",
    "SUB S, o12",
    "DES",
    ]
    macro12 = Macro("macro12", arguments, lines, "test", 2)
    arguments = "0x92,0xb2,0xea,0x60,0x7d,0x8b"
    instruction_num = 7871
    symbols = []
    labels = {
    'label0': '1E51',
    'label1': '1F24',
    'label2': '1E94',
    'label3': '1E74',
    'label4': '1EC0',
    'label5': '1EAE',
    'label6': '1EF2',
    'label7': '1F18',
    'label8': '1EAE',
    'label9': '1E7C',
    'label10': '1F29',
    'label11': '1F47',
    'label12': '1E56',
    'label13': '1E4C',
    }
    (hex, num) = macro12.hex(arguments, instruction_num, symbols, labels, False, [])


    assert macro12.error == True


    # test final instruction num > 1fff => error
    arguments = "m5,o6"
    lines = [
    "CLC",
    "RRC",
    "INC",
    "STD m5",
    "TST S, o6",
    ]
    macro = Macro("macro", arguments, lines, "test", 2)
    arguments = "0xe5,0xe1"
    instruction_num = 8989
    symbols = []
    labels = {
    'label0': '0DE0',
    'label1': '0DF9',
    'label2': '0E71',
    'label3': '0E44',
    'label4': '0E5B',
    'label5': '0E2E',
    'label6': '0E2B',
    'label7': '0DE6',
    }
    (hex, num) = macro.hex(arguments, instruction_num, symbols, labels, False, [])

    assert macro.error == True



