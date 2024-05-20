"""
This file is used to test the MultiOpInstruction class through pytest.

Revision History:
    Zachary Pestrikov 5/16/2024 Wrote Tests
"""
from Instructions.OperandInstructions.MultiOpInstructions.MultiOpInstruction import MultiOpInstruction
    
def test_multiop():
    """
    Function called by pytest to test the MultiOpInstruction test
    """
    # 01100000mmmmmmmm	ADC	m
    instruction = MultiOpInstruction('ADC', '0xa4', 'test', 759164)
    hex = instruction.hex(7667, [], [], False, {})
    assert hex == "1DF3 60A4"
    assert instruction.error == False

    # 01100001oooooooo	ADC	X, o
    instruction = MultiOpInstruction('ADC', 'X, 13', 'test', 814416)
    hex = instruction.hex(1761, [], [], False, {})
    assert hex == "06E1 610D"
    assert instruction.error == False

    # 01100010oooooooo	ADC	S, o
    instruction = MultiOpInstruction('ADC', 'S, -17', 'test', 233882)
    hex = instruction.hex(2469, [], [], False, {})
    assert hex == "09A5 62EF"
    assert instruction.error == False

    # 01101000mmmmmmmm	ADD	m
    instruction = MultiOpInstruction('ADD', '0x7a', 'test', 404409)
    hex = instruction.hex(7947, [], [], False, {})
    assert hex == "1F0B 687A"
    assert instruction.error == False

    # 01101001oooooooo	ADD	X, o
    instruction = MultiOpInstruction('ADD', 'X, -69', 'test', 429689)
    hex = instruction.hex(5817, [], [], False, {})
    assert hex == "16B9 69BB"
    assert instruction.error == False

    # 01101010oooooooo	ADD	S, o
    instruction = MultiOpInstruction('ADD', 'S, -36', 'test', 623454)
    hex = instruction.hex(4921, [], [], False, {})
    assert hex == "1339 6ADC"
    assert instruction.error == False

    # 01000100mmmmmmmm	AND	m
    instruction = MultiOpInstruction('AND', '0x1d', 'test', 196146)
    hex = instruction.hex(6976, [], [], False, {})
    assert hex == "1B40 441D"
    assert instruction.error == False

    # 01000101oooooooo	AND	X, o
    instruction = MultiOpInstruction('AND', 'X, -87', 'test', 103076)
    hex = instruction.hex(5493, [], [], False, {})
    assert hex == "1575 45A9"
    assert instruction.error == False

    # 01000110oooooooo	AND	S, o
    instruction = MultiOpInstruction('AND', 'S, -72', 'test', 537288)
    hex = instruction.hex(6660, [], [], False, {})
    assert hex == "1A04 46B8"
    assert instruction.error == False

    # 00110000mmmmmmmm	CMP	m
    instruction = MultiOpInstruction('CMP', '0x78', 'test', 288188)
    hex = instruction.hex(5056, [], [], False, {})
    assert hex == "13C0 3078"
    assert instruction.error == False

    # 00110001oooooooo	CMP	X, o
    instruction = MultiOpInstruction('CMP', 'X, -89', 'test', 161429)
    hex = instruction.hex(6958, [], [], False, {})
    assert hex == "1B2E 31A7"
    assert instruction.error == False

    # 00110010oooooooo	CMP	S, o
    instruction = MultiOpInstruction('CMP', 'S, 21', 'test', 276778)
    hex = instruction.hex(7842, [], [], False, {})
    assert hex == "1EA2 3215"
    assert instruction.error == False

    # 01110100mmmmmmmm	OR	m
    instruction = MultiOpInstruction('OR', '0x20', 'test', 327577)
    hex = instruction.hex(6783, [], [], False, {})
    assert hex == "1A7F 7420"
    assert instruction.error == False

    # 01110101oooooooo	OR	X, o
    instruction = MultiOpInstruction('OR', 'X, 248', 'test', 944429)
    hex = instruction.hex(7499, [], [], False, {})
    assert hex == "1D4B 75F8"
    assert instruction.error == False

    # 01110110oooooooo	OR	S, o
    instruction = MultiOpInstruction('OR', 'S, -49', 'test', 551329)
    hex = instruction.hex(1321, [], [], False, {})
    assert hex == "0529 76CF"
    assert instruction.error == False

    # 00011000mmmmmmmm	SBB	m
    instruction = MultiOpInstruction('SBB', '0x7a', 'test', 954913)
    hex = instruction.hex(3722, [], [], False, {})
    assert hex == "0E8A 187A"
    assert instruction.error == False

    # 00011001oooooooo	SBB	X, o
    instruction = MultiOpInstruction('SBB', 'X, -103', 'test', 640771)
    hex = instruction.hex(2497, [], [], False, {})
    assert hex == "09C1 1999"
    assert instruction.error == False

    # 00011010oooooooo	SBB	S, o
    instruction = MultiOpInstruction('SBB', 'S, 135', 'test', 166833)
    hex = instruction.hex(2440, [], [], False, {})
    assert hex == "0988 1A87"
    assert instruction.error == False

    # 00010000mmmmmmmm	SUB	m
    instruction = MultiOpInstruction('SUB', '0xa4', 'test', 244261)
    hex = instruction.hex(3293, [], [], False, {})
    assert hex == "0CDD 10A4"
    assert instruction.error == False

    # 00010001oooooooo	SUB	X, o
    instruction = MultiOpInstruction('SUB', 'X, -55', 'test', 850289)
    hex = instruction.hex(738, [], [], False, {})
    assert hex == "02E2 11C9"
    assert instruction.error == False

    # 00010010oooooooo	SUB	S, o
    instruction = MultiOpInstruction('SUB', 'S, -83', 'test', 381492)
    hex = instruction.hex(6287, [], [], False, {})
    assert hex == "188F 12AD"
    assert instruction.error == False

    # 01001100mmmmmmmm	TST	m
    instruction = MultiOpInstruction('TST', '0x94', 'test', 375904)
    hex = instruction.hex(5404, [], [], False, {})
    assert hex == "151C 4C94"
    assert instruction.error == False

    # 01001101oooooooo	TST	X, o
    instruction = MultiOpInstruction('TST', 'X, -102', 'test', 283364)
    hex = instruction.hex(3803, [], [], False, {})
    assert hex == "0EDB 4D9A"
    assert instruction.error == False

    # 01001110oooooooo	TST	S, o
    instruction = MultiOpInstruction('TST', 'S, 191', 'test', 334978)
    hex = instruction.hex(273, [], [], False, {})
    assert hex == "0111 4EBF"
    assert instruction.error == False

    # 00110100mmmmmmmm	XOR	m
    instruction = MultiOpInstruction('XOR', '0xdd', 'test', 596254)
    hex = instruction.hex(40, [], [], False, {})
    assert hex == "0028 34DD"
    assert instruction.error == False

    # 00110101oooooooo	XOR	X, o
    instruction = MultiOpInstruction('XOR', 'X, 156', 'test', 259849)
    hex = instruction.hex(4500, [], [], False, {})
    assert hex == "1194 359C"
    assert instruction.error == False

    # 00110110oooooooo	XOR	S, o
    instruction = MultiOpInstruction('XOR', 'S, 121', 'test', 19171)
    hex = instruction.hex(2501, [], [], False, {})
    assert hex == "09C5 3679"
    assert instruction.error == False
##############################################################################
    # extra test
    instruction = MultiOpInstruction('XOR', 'X, 21', 'test', 10)
    hex = instruction.hex(10, [], [], False, {})
    assert hex == "000A 3515"
    assert instruction.error == False

    # test o > 256
    instruction = MultiOpInstruction('XOR', 'S, 3000', 'test', 959468)
    hex = instruction.hex(54, [], [], False, {})
    assert hex == "0036 36FF"
    assert instruction.error == False

    # test o < -128
    instruction = MultiOpInstruction('XOR', 'S, -129', 'test', 959468)
    hex = instruction.hex(54, [], [], False, {})
    assert hex == "0036 3680"
    assert instruction.error == False

    # test o is hex
    instruction = MultiOpInstruction('XOR', 'S, 0x2F', 'test', 959468)
    hex = instruction.hex(54, [], [], False, {})
    assert hex == "0036 362F"
    assert instruction.error == False

    # test o is char
    instruction = MultiOpInstruction('XOR', 'S, "a"', 'test', 959468)
    hex = instruction.hex(54, [], [], False, {})
    assert hex == "0036 3661"
    assert instruction.error == False

    # test o is binary
    instruction = MultiOpInstruction('XOR', 'S, -0b101001', 'test', 959468)
    hex = instruction.hex(54, [], [], False, {})
    assert hex == "0036 3617"
    assert instruction.error == False

    # test strange operand
    instruction = MultiOpInstruction('XOR', 'adsfhaksjfh', 'test', 959468)
    hex = instruction.hex(54, [], [], False, {})
    assert instruction.error == True

    # test const as o
    instruction = MultiOpInstruction('XOR', 'S, -test', 'test', 959468)
    hex = instruction.hex(54, {'test': 'F1'}, [], False, {})
    assert hex == "0036 360F"
    assert instruction.error == False

    # test blank o = 0
    instruction = MultiOpInstruction('XOR', 'S', 'test', 959468)
    hex = instruction.hex(54, {'test': 'F1'}, [], False, {})
    assert hex == "0036 3600"
    assert instruction.error == False

    # test operand count < 3
    instruction = MultiOpInstruction('XOR', 'S, test, 2', 'test', 959468)
    hex = instruction.hex(54, {'test': 'F1'}, [], False, {})
    assert instruction.error == True

    # test negative memory address
    instruction = MultiOpInstruction('CMP', '-0x8a', 'test', 307613)
    hex = instruction.hex(4281, [], [], False, {})
    assert instruction.error == True

    # test short memory address
    instruction = MultiOpInstruction('SBB', '0x7', 'test', 954913)
    hex = instruction.hex(3722, [], [], False, {})
    assert hex == "0E8A 1807"
    assert instruction.error == False

    # test memory address not in hex
    instruction = MultiOpInstruction('SBB', '0', 'test', 954913)
    hex = instruction.hex(3722, [], [], False, {})
    assert instruction.error == True

    # test memory address warning
    instruction = MultiOpInstruction('SBB', '0x0', 'test', 954913)
    hex = instruction.hex(3722, [], [], False, {})
    assert instruction.errors[len(instruction.errors) - 1][:6] == 'Memory'

    # test memory address byte
    instruction = MultiOpInstruction('SBB', 'test', 'test', 954913)
    hex = instruction.hex(3722, [], [], False, {'test': '07'})
    assert hex == "0E8A 1807"
    assert instruction.error == False

     # test memory not allocated, but used
    instruction = MultiOpInstruction('SBB', 'test', 'test', 954913)
    hex = instruction.hex(3722, [], [], False, {})
    assert instruction.error == True

    # test memory in symbols table => warning
    instruction = MultiOpInstruction('SBB', 'test', 'test', 954913)
    hex = instruction.hex(3722, {'test': '07'}, [], False, {})
    assert hex == "0E8A 1807"
    assert instruction.error == False
    assert instruction.errors[len(instruction.errors) - 1][:6] == 'Memory'

    # test memory not in hex => error
    instruction = MultiOpInstruction('SBB', '0b00000000', 'test', 954913)
    hex = instruction.hex(3722, {}, [], False, {})
    assert instruction.error == True

    # test memory blank => 0 and warning
    instruction = MultiOpInstruction('SBB', '', 'test', 954913)
    hex = instruction.hex(3722, {}, [], False, {})
    assert hex == "0E8A 1800"
    assert instruction.error == False
    assert instruction.errors[len(instruction.errors) - 1][:6] == 'Memory'