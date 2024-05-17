"""
This file is used by pytest to test the Instruction class.
This includes all instructions with no operands.
"""

from Instructions.Instruction import Instruction

def test_instruction():
    # 0111000100000001	ASR

    instruction = Instruction('ASR', '', 'test', 69862)
    hex = instruction.hex(4136, [], [], False, [])
    assert hex == "1028 7101"
    assert instruction._error == False

    # 0111101100000000	DEC

    instruction = Instruction('DEC', '', 'test', 93047)
    hex = instruction.hex(490, [], [], False, [])
    assert hex == "01EA 7B00"
    assert instruction._error == False

    # 0000000000000000	INC

    instruction = Instruction('INC', '', 'test', 848065)
    hex = instruction.hex(7201, [], [], False, [])
    assert hex == "1C21 0000"
    assert instruction._error == False

    # 0101100000000000	LSL

    instruction = Instruction('LSL', '', 'test', 8347)
    hex = instruction.hex(62, [], [], False, [])
    assert hex == "003E 5800"
    assert instruction._error == False

    # 0111000100000000	LSR

    instruction = Instruction('LSR', '', 'test', 843159)
    hex = instruction.hex(5450, [], [], False, [])
    assert hex == "154A 7100"
    assert instruction._error == False

    # 0010011100000000	NEG

    instruction = Instruction('NEG', '', 'test', 757070)
    hex = instruction.hex(501, [], [], False, [])
    assert hex == "01F5 2700"
    assert instruction._error == False

    # 0010110100000000	NOT

    instruction = Instruction('NOT', '', 'test', 758812)
    hex = instruction.hex(7252, [], [], False, [])
    assert hex == "1C54 2D00"
    assert instruction._error == False

    # 0101000000000000	RLC

    instruction = Instruction('RLC', '', 'test', 948199)
    hex = instruction.hex(3768, [], [], False, [])
    assert hex == "0EB8 5000"
    assert instruction._error == False

    # 0101001000000000	ROL

    instruction = Instruction('ROL', '', 'test', 505507)
    hex = instruction.hex(2976, [], [], False, [])
    assert hex == "0BA0 5200"
    assert instruction._error == False

    # 0111000100000010	ROR

    instruction = Instruction('ROR', '', 'test', 1472)
    hex = instruction.hex(8094, [], [], False, [])
    assert hex == "1F9E 7102"
    assert instruction._error == False

    # 0111000100000011	RRC

    instruction = Instruction('RRC', '', 'test', 762660)
    hex = instruction.hex(6657, [], [], False, [])
    assert hex == "1A01 7103"
    assert instruction._error == False

    # 0111111110000001	STI

    instruction = Instruction('STI', '', 'test', 527606)
    hex = instruction.hex(1703, [], [], False, [])
    assert hex == "06A7 7F81"
    assert instruction._error == False

    # 0000011101101001	CLI

    instruction = Instruction('CLI', '', 'test', 467250)
    hex = instruction.hex(6684, [], [], False, [])
    assert hex == "1A1C 0769"
    assert instruction._error == False

    # 0111111100100010	STU

    instruction = Instruction('STU', '', 'test', 230612)
    hex = instruction.hex(1698, [], [], False, [])
    assert hex == "06A2 7F22"
    assert instruction._error == False

    # 0000011111001010	CLU

    instruction = Instruction('CLU', '', 'test', 256356)
    hex = instruction.hex(708, [], [], False, [])
    assert hex == "02C4 07CA"
    assert instruction._error == False

    # 0111111100001100	STC

    instruction = Instruction('STC', '', 'test', 77933)
    hex = instruction.hex(3869, [], [], False, [])
    assert hex == "0F1D 7F0C"
    assert instruction._error == False

    # 0000011111100100	CLC

    instruction = Instruction('CLC', '', 'test', 719404)
    hex = instruction.hex(4856, [], [], False, [])
    assert hex == "12F8 07E4"
    assert instruction._error == False

    # 0000011110000000	TAX

    instruction = Instruction('TAX', '', 'test', 160679)
    hex = instruction.hex(4941, [], [], False, [])
    assert hex == "134D 0780"
    assert instruction._error == False

    # 0110011100000001	TXA

    instruction = Instruction('TXA', '', 'test', 291650)
    hex = instruction.hex(4943, [], [], False, [])
    assert hex == "134F 6701"
    assert instruction._error == False

    # 0000010110000000	INX

    instruction = Instruction('INX', '', 'test', 882149)
    hex = instruction.hex(1931, [], [], False, [])
    assert hex == "078B 0580"
    assert instruction._error == False

    # 0000110110000000	DEX

    instruction = Instruction('DEX', '', 'test', 109730)
    hex = instruction.hex(289, [], [], False, [])
    assert hex == "0121 0D80"
    assert instruction._error == False

    # 0000011101010000	TAS

    instruction = Instruction('TAS', '', 'test', 787718)
    hex = instruction.hex(5365, [], [], False, [])
    assert hex == "14F5 0750"
    assert instruction._error == False

    # 0110011100000000	TSA

    instruction = Instruction('TSA', '', 'test', 634772)
    hex = instruction.hex(7286, [], [], False, [])
    assert hex == "1C76 6700"
    assert instruction._error == False

    # 0000011001000000	INS

    instruction = Instruction('INS', '', 'test', 873341)
    hex = instruction.hex(5653, [], [], False, [])
    assert hex == "1615 0640"
    assert instruction._error == False

    # 0000111001000000	DES

    instruction = Instruction('DES', '', 'test', 226797)
    hex = instruction.hex(3193, [], [], False, [])
    assert hex == "0C79 0E40"
    assert instruction._error == False

    # 0001111110000000	NOP

    instruction = Instruction('NOP', '', 'test', 306267)
    hex = instruction.hex(5508, [], [], False, [])
    assert hex == "1584 1F80"
    assert instruction._error == False

    # 0001111100000000	RTS

    instruction = Instruction('RTS', '', 'test', 223761)
    hex = instruction.hex(6297, [], [], False, [])
    assert hex == "1899 1F00"
    assert instruction._error == False

    # 0000001000000000	POPF

    instruction = Instruction('POPF', '', 'test', 10908)
    hex = instruction.hex(5873, [], [], False, [])
    assert hex == "16F1 0200"
    assert instruction._error == False

    # 0000111000000000	PUSHF

    instruction = Instruction('PUSHF', '', 'test', 454006)
    hex = instruction.hex(681, [], [], False, [])
    assert hex == "02A9 0E00"
    assert instruction._error == False

######################################################################

    # test operands => error
    instruction = Instruction('NOP', '5', 'test', 540812)
    hex = instruction.hex(1203, [], [], False, [])
    assert instruction._error == True

    #	RTS warning

    instruction = Instruction('RTS', '', 'test', 223761)
    hex = instruction.hex(6297, [], [], False, [])
    assert hex == "1899 1F00"
    assert instruction._error == False
    assert instruction.errors[len(instruction.errors) - 1][:5] == 'Stack'

    # 	POPF warning

    instruction = Instruction('POPF', '', 'test', 10908)
    hex = instruction.hex(5873, [], [], False, [])
    assert hex == "16F1 0200"
    assert instruction._error == False
    assert instruction.errors[len(instruction.errors) - 1][:5] == 'Stack'

    # 	PUSHF warning
    instruction = Instruction('PUSHF', '', 'test', 454006)
    hex = instruction.hex(681, [], [], False, [])
    assert hex == "02A9 0E00"
    assert instruction._error == False
    assert instruction.errors[len(instruction.errors) - 1][:5] == 'Stack'

    length = len(instruction.errors)

     #	RTS no warning

    instruction = Instruction('RTS', '', 'test', 223761)
    hex = instruction.hex(6297, [], [], True, [])
    assert hex == "1899 1F00"
    assert instruction._error == False
    assert len(instruction.errors) == length

    # 	POPF no warning

    instruction = Instruction('POPF', '', 'test', 10908)
    hex = instruction.hex(5873, [], [], True, [])
    assert hex == "16F1 0200"
    assert instruction._error == False
    assert len(instruction.errors) == length

    # 	PUSHF no warning
    instruction = Instruction('PUSHF', '', 'test', 454006)
    hex = instruction.hex(681, [], [], True, [])
    assert hex == "02A9 0E00"
    assert instruction._error == False
    assert len(instruction.errors) == length


# add subroutine instructions