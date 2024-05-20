"""
This file is used by pytest to test the OperandInstruction class.
This class includes the instructions:
ADCI, ADDI, ANDI, CMPI, ORI, SBBI, SUBI, TSTI, XORI, LDI, LDD, STD, IN, OUT
"""

from Instructions.OperandInstructions.OperandInstruction import OperandInstruction

def test_opInstruction():
    # 01100011kkkkkkkk	ADCI	k

    instruction = OperandInstruction('ADCI', '-73', 'test', 131935)
    hex = instruction.hex(2018, [], [], False, [])
    assert hex == "07E2 63B7"
    assert instruction.error == False

    # 01101011kkkkkkkk	ADDI	k

    instruction = OperandInstruction('ADDI', '-13', 'test', 583370)
    hex = instruction.hex(1636, [], [], False, [])
    assert hex == "0664 6BF3"
    assert instruction.error == False

    # 01000111kkkkkkkk	ANDI	k

    instruction = OperandInstruction('ANDI', '169', 'test', 35952)
    hex = instruction.hex(5917, [], [], False, [])
    assert hex == "171D 47A9"
    assert instruction.error == False

    # 00110011kkkkkkkk	CMPI	k

    instruction = OperandInstruction('CMPI', '92', 'test', 837723)
    hex = instruction.hex(8150, [], [], False, [])
    assert hex == "1FD6 335C"
    assert instruction.error == False

    # 01110111kkkkkkkk	ORI	k

    instruction = OperandInstruction('ORI', '146', 'test', 804783)
    hex = instruction.hex(6849, [], [], False, [])
    assert hex == "1AC1 7792"
    assert instruction.error == False

    # 00011011kkkkkkkk	SBBI	k

    instruction = OperandInstruction('SBBI', '9', 'test', 104841)
    hex = instruction.hex(1743, [], [], False, [])
    assert hex == "06CF 1B09"
    assert instruction.error == False

    # 00010011kkkkkkkk	SUBI	k

    instruction = OperandInstruction('SUBI', '168', 'test', 67032)
    hex = instruction.hex(3012, [], [], False, [])
    assert hex == "0BC4 13A8"
    assert instruction.error == False

    # 01001111kkkkkkkk	TSTI	k

    instruction = OperandInstruction('TSTI', '13', 'test', 813328)
    hex = instruction.hex(47, [], [], False, [])
    assert hex == "002F 4F0D"
    assert instruction.error == False

    # 00110111kkkkkkkk	XORI	k

    instruction = OperandInstruction('XORI', '243', 'test', 694872)
    hex = instruction.hex(5493, [], [], False, [])
    assert hex == "1575 37F3"
    assert instruction.error == False

    # 10001001kkkkkkkk	LDI	k

    instruction = OperandInstruction('LDI', '42', 'test', 527944)
    hex = instruction.hex(966, [], [], False, [])
    assert hex == "03C6 892A"
    assert instruction.error == False

    # 10000000mmmmmmmm	LDD	m

    instruction = OperandInstruction('LDD', '0x6f', 'test', 217171)
    hex = instruction.hex(6354, [], [], False, [])
    assert hex == "18D2 806F"
    assert instruction.error == False

    # 10100000mmmmmmmm	STD	m

    instruction = OperandInstruction('STD', '0xc0', 'test', 323744)
    hex = instruction.hex(3497, [], [], False, [])
    assert hex == "0DA9 A0C0"
    assert instruction.error == False

    # 10010000pppppppp	IN	p

    instruction = OperandInstruction('IN', '0x1d', 'test', 589893)
    hex = instruction.hex(2266, [], [], False, [])
    assert hex == "08DA 901D"
    assert instruction.error == False

    # 10110000pppppppp	OUT	p

    instruction = OperandInstruction('OUT', '0x2b', 'test', 620387)
    hex = instruction.hex(2646, [], [], False, [])
    assert hex == "0A56 B02B"
    assert instruction.error == False
###############################################################################
    # test p < 0 => error
    instruction = OperandInstruction('OUT', '-0x2b', 'test', 620387)
    hex = instruction.hex(2646, [], [], False, [])
    assert instruction.error == True

    # test p not in hex => error
    instruction = OperandInstruction('OUT', '2', 'test', 620387)
    hex = instruction.hex(2646, [], [], False, [])
    assert instruction.error == True

    # test m < 0 => error
    instruction = OperandInstruction('STD', '-0xc0', 'test', 323744)
    hex = instruction.hex(3497, [], [], False, [])
    assert instruction.error == True

    # test m not in hex => error
    instruction = OperandInstruction('STD', '3', 'test', 323744)
    hex = instruction.hex(3497, [], [], False, [])
    assert instruction.error == True

    # test m not allocated => 
    instruction = OperandInstruction('STD', '3', 'test', 323744)
    hex = instruction.hex(3497, [], [], False, [])
    assert instruction.error == True

    # test m in bytes table
    instruction = OperandInstruction('STD', 'test', 'test', 323744)
    hex = instruction.hex(3497, [], [], False, {'test': 'FF'})
    assert hex == "0DA9 A0FF"
    assert instruction.error == False

    # test m in symbols table
    instruction = OperandInstruction('STD', 'test', 'test', 323744)
    hex = instruction.hex(3497, {'test': 'FF'}, [], False, {})
    assert hex == "0DA9 A0FF"
    assert instruction.error == False
    assert instruction.errors[len(instruction.errors) - 1][:6] == 'Memory'

    # test k in symbols table
    instruction = OperandInstruction('CMPI', 'test', 'test', 837723)
    hex = instruction.hex(8150, {'test': '5C'}, [], False, [])
    assert hex == "1FD6 335C"
    assert instruction.error == False

    # test k in bytes table
    instruction = OperandInstruction('CMPI', 'test', 'test', 837723)
    hex = instruction.hex(8150, [], [], False, {'test': '5C'})
    assert instruction.error == True

    # test p in symbols table
    instruction = OperandInstruction('OUT', 'test', 'test', 620387)
    hex = instruction.hex(2646, {'test': '2B'}, [], False, [])
    assert hex == "0A56 B02B"
    assert instruction.error == False

    # test p in bytes table
    instruction = OperandInstruction('OUT', 'test', 'test', 620387)
    hex = instruction.hex(2646, [], [], False, {'test': '2B'})
    assert instruction.error == True

    # test m > 255
    instruction = OperandInstruction('STD', '0x256', 'test', 323744)
    hex = instruction.hex(3497, [], [], False, [])
    assert instruction.error == True

    # test p > 255
    instruction = OperandInstruction('IN', '0x256', 'test', 323744)
    hex = instruction.hex(3497, [], [], False, [])
    assert instruction.error == True
