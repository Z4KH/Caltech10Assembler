"""
This file is used by pytest to test the Line class.
"""

from Lines.Line import Line

def test_line():
    labels = {
    'label0': '0BC0',
    'label1': '0BF6',
    'label2': '0C6A',
    'label3': '0BE1',
    'label4': '0BDF',
    'label5': '0C13',
    'label6': '0BE4',
    'label7': '0C2D',
    'label8': '0B86',
    'label9': '0BA1',
    'label10': '0BA0',
    'label11': '0C51',
    'label12': '0BF2',
    'label13': '0C67',
    'label14': '0C29',
    'label15': '0C84',
    'label16': '0C73',
    'label17': '0C7C',
    'label18': '0C41',
    'label19': '0C78',
    'label20': '0C24',
    'label21': '0C55',
    'label22': '0BBE',
    'label23': '0C6E',
    'label24': '0B96',
    'label25': '0C0D',
    'label26': '0BAD',
    'label27': '0C93',
    'label28': '0C50',
    'label29': '0BCF',
    'label30': '0C6D',
    'label31': '0C5F',
    'label32': '0C2A',
    'label33': '0C7F',
    'label34': '0BE4',
    'label35': '0BD1',
    'label36': '0BD1',
    'label37': '0BD1',
    'label38': '0C97',
    'label39': '0C29',
    'label40': '0BEC',
    'label41': '0BE5',
    'label42': '0C4C',
    'label43': '0C97',
    'label44': '0C0E',
    'label45': '0C37',
    'label46': '0C94',
    'label47': '0C07',
    'label48': '0BAB',
    'label49': '0C65',
    'label50': '0BAE',
    'label51': '0CA2',
    'label52': '0BDA',
    'label53': '0BEB',
    'label54': '0BC1',
    'label55': '0BB3',
    'label56': '0C60',
    'label57': '0C0E',
    'label58': '0C4F',
    'label59': '0CAA',
    'label60': '0BE7',
    'label61': '0C55',
    'label62': '0C9D',
    'label63': '0C39',
    'label64': '0BE7',
    'label65': '0C4C',
    'label66': '0C15',
    'label67': '0BCE',
    'label68': '0C73',
    'label69': '0C9B',
    'label70': '0C30',
    'label71': '0BEF',
    'label72': '0C9D',
    'label73': '0BDB',
    'label74': '0BCD',
    'label75': '0C4E',
    'label76': '0C83',
    'label77': '0C67',
    'label78': '0C63',
    'label79': '0BD5',
    'label80': '0C48',
    'label81': '0C1C',
    'label82': '0BFF',
    'label83': '0C7C',
    'label84': '0C51',
    'label85': '0CAC',
    'label86': '0C14',
    'label87': '0C36',
    'label88': '0BD5',
    'label89': '0C3C',
    'label90': '0C54',
    'label91': '0C9E',
    'label92': '0CCC',
    'label93': '0C06',
    'label94': '0C34',
    'label95': '0C48',
    'label96': '0BFF',
    'label97': '0CCC',
    'label98': '0CA1',
    'label99': '0C75',
    'label100': '0C99',
    'label101': '0BFE',
    'label102': '0C52',
    'label103': '0CC8',
    'label104': '0C65',
    'label105': '0C6B',
    'label106': '0CBF',
    'label107': '0C66',
    'label108': '0C97',
    'label109': '0CAE',
    'label110': '0CA6',
    'label111': '0C12',
    'label112': '0C29',
    'label113': '0BF6',
    'label114': '0CB7',
    'label115': '0BF9',
    'label116': '0C08',
    'label117': '0C6D',
    'label118': '0CC6',
    'label119': '0CB1',
    'label120': '0CE2',
    'label121': '0C49',
    'label122': '0CB2',
    'label123': '0C58',
    'label124': '0C89',
    'label125': '0C50',
    'label126': '0CC7',
    'label127': '0C94',
    'label128': '0CAE',
    'label129': '0CD6',
    'label130': '0C45',
    'label131': '0C31',
    'label132': '0C3C',
    'label133': '0C30',
    'label134': '0CC5',
    'label135': '0C0E',
    'label136': '0CBB',
    'label137': '0CA8',
    'label138': '0CBA',
    'label139': '0C76',
    'label140': '0C69',
    'label141': '0CA7',
    'label142': '0C7D',
    'label143': '0D02',
    'label144': '0CA9',
    'label145': '0CBE',
    'label146': '0C5D',
    'label147': '0CAF',
    'label148': '0C21',
    'label149': '0CB4',
    'label150': '0C27',
    'label151': '0C94',
    'label152': '0C33',
    'label153': '0CC5',
    'label154': '0CFD',
    'label155': '0CC0',
    'label156': '0C2F',
    'label157': '0C66',
    'label158': '0CD5',
    'label159': '0CCA',
    'label160': '0C62',
    'label161': '0CDA',
    'label162': '0CDC',
    'label163': '0CC7',
    'label164': '0D17',
    'label165': '0D18',
    'label166': '0C4A',
    'label167': '0C55',
    'label168': '0C2D',
    'label169': '0CB1',
    'label170': '0CC3',
    'label171': '0D11',
    'label172': '0C3D',
    'label173': '0CD1',
    'label174': '0CDA',
    'label175': '0C66',
    'label176': '0CB4',
    'label177': '0D23',
    'label178': '0CC3',
    'label179': '0CC1',
    'label180': '0CFB',
    'label181': '0D0E',
    'label182': '0D15',
    'label183': '0C7C',
    'label184': '0D2D',
    'label185': '0C77',
    'label186': '0CD7',
    'label187': '0C5A',
    'label188': '0CE1',
    'label189': '0C7A',
    'label190': '0CB5',
    'label191': '0D19',
    'label192': '0C96',
    'label193': '0C9F',
    'label194': '0CB0',
    'label195': '0CE7',
    'label196': '0D35',
    'label197': '0CBC',
    'label198': '0C72',
    'label199': '0D27',
    }
    Line.labels = labels

    # code
    text = "#code"
    line_code = Line(text, "test", 2, [])
    #assert result == f"{} 8C1C"
    assert line_code.error == False
    assert Line.seg == 1
    assert line_code.hex() == ''

    # data in code seg => error
    text = "#byte TestByte"
    line_datacseg = Line(text, "test", 2, [])
    #assert result == f"{} 8C1C"
    assert Line.bytes == {}
    assert line_datacseg.error == True
    assert line_datacseg.hex() == 'ERROR'

    # instructions before org
    text = "NOP;comment"
    line_1 = Line(text, "test", 2, [])
    assert line_1.error == False
    assert len(Line.preOrg) == 1

    text = "NOP"
    line_2 = Line(text, "test", 2, [])
    assert line_2.error == False
    assert len(Line.preOrg) == 2

    # 01110110oooooooo OR S, o
    text = "OR S, 252"
    line_3 = Line(text, "test", 2, [])
    #assert result == "0BFC 76FC"
    assert line_3.error == False
    assert len(Line.preOrg) == 3

    # data seg
    text = "#data ;dataseg"
    dataseg = Line(text, "test", 2, [])
    assert Line.seg == 0
    assert dataseg.hex() == ''

    # stack init
    text = "#stack 100"
    stack = Line(text, "test", 2, [])
    assert Line.stack == True 
    assert stack.hex() == ''

    # code seg
    text = "#code ;codeseg"
    codeseg = Line(text, "test", 2, [])
    assert Line.seg == 1
    assert codeseg.hex() == ''

    # test #org first
    text = "#org"
    org = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    result = org.hex()
    assert result == ""
    assert org.error == False
    assert Line.org == True

##############################################################################

    Line.instructions_hexed = 3065
    Line.instructions = 3065


        # 0111000100000011 RRC 
    # 10011000rrrrrrrr JNS r
    text = "JNS label0"
    line0 = Line(text, "test", 2, [])
    result = line0.hex()
    assert result == "0BF9 98C6"
    assert line0.error == False

    # 0101000000000000 RLC 
    text = "RLC"
    line1 = Line(text, "test", 2, [])
    result = line1.hex()
    assert result == "0BFA 5000"
    assert line1.error == False

    # 0111111100100010 STU 
    text = "STU"
    line2 = Line(text, "test", 2, [])
    result = line2.hex()
    assert result == "0BFB 7F22"
    assert line2.error == False

    # 0001111110000000 NOP 
    text = "NOP"
    line3 = Line(text, "test", 2, [])
    result = line3.hex()
    assert result == "0BFC 1F80"
    assert line3.error == False

    # 00010001oooooooo SUB X, o
    text = "SUB X, 226"
    line4 = Line(text, "test", 2, [])
    result = line4.hex()
    assert result == "0BFD 11E2"
    assert line4.error == False

    # 00011001oooooooo SBB X, o
    text = "SBB X, 21"
    line5 = Line(text, "test", 2, [])
    result = line5.hex()
    assert result == "0BFE 1915"
    assert line5.error == False

    # 0001111100000000 RTS 
    text = "RTS"
    line6 = Line(text, "test", 2, [])
    result = line6.hex()
    assert result == "0BFF 1F00"
    assert line6.error == False

    # 10101100rrrrrrrr JLE r
    text = "JLE label7"
    line7 = Line(text, "test", 2, [])
    result = line7.hex()
    assert result == "0C00 AC2C"
    assert line7.error == False

    # 0000011001000000 INS 
    text = "INS"
    line8 = Line(text, "test", 2, [])
    result = line8.hex()
    assert result == "0C01 0640"
    assert line8.error == False

    # 0000011101010000 TAS 
    text = "TAS"
    line9 = Line(text, "test", 2, [])
    result = line9.hex()
    assert result == "0C02 0750"
    assert line9.error == False

    # 10001011rrrrrrrr JBE r
    text = "JBE label10"
    line10 = Line(text, "test", 2, [])
    result = line10.hex()
    assert result == "0C03 8B9C"
    assert line10.error == False

    # 10101111rrrrrrrr JG r
    text = "JG label11"
    line11 = Line(text, "test", 2, [])
    result = line11.hex()
    assert result == "0C04 AF4C"
    assert line11.error == False

    # 10001011rrrrrrrr JBE r
    text = "JBE label12"
    line12 = Line(text, "test", 2, [])
    result = line12.hex()
    assert result == "0C05 8BEC"
    assert line12.error == False

    # 00110001oooooooo CMP X, o
    text = "CMP X, 97"
    line13 = Line(text, "test", 2, [])
    result = line13.hex()
    assert result == "0C06 3161"
    assert line13.error == False

    # 01001101oooooooo TST X, o
    text = "TST X, 34"
    line14 = Line(text, "test", 2, [])
    result = line14.hex()
    assert result == "0C07 4D22"
    assert line14.error == False

    # 10101000rrrrrrrr JNV r
    text = "JNV label15"
    line15 = Line(text, "test", 2, [])
    result = line15.hex()
    assert result == "0C08 A87B"
    assert line15.error == False

    # 0111101100000000 DEC 
    text = "DEC"
    line16 = Line(text, "test", 2, [])
    result = line16.hex()
    assert result == "0C09 7B00"
    assert line16.error == False

    # 0111000100000000 LSR 
    text = "LSR"
    line17 = Line(text, "test", 2, [])
    result = line17.hex()
    assert result == "0C0A 7100"
    assert line17.error == False

    # 0111111100001100 STC 
    text = "STC"
    line18 = Line(text, "test", 2, [])
    result = line18.hex()
    assert result == "0C0B 7F0C"
    assert line18.error == False

    # 01000100mmmmmmmm AND m
    text = "AND 0x6c"
    line19 = Line(text, "test", 2, [])
    result = line19.hex()
    assert result == "0C0C 446C"
    assert line19.error == False

    # 0010110100000000 NOT 
    text = "NOT"
    line20 = Line(text, "test", 2, [])
    result = line20.hex()
    assert result == "0C0D 2D00"
    assert line20.error == False

    # 0000011111100100 CLC 
    text = "CLC"
    line21 = Line(text, "test", 2, [])
    result = line21.hex()
    assert result == "0C0E 07E4"
    assert line21.error == False

    # 10001000rrrrrrrr JA r
    text = "JA label22"
    line22 = Line(text, "test", 2, [])
    result = line22.hex()
    assert result == "0C0F 88AE"
    assert line22.error == False

    # 0010011100000000 NEG 
    text = "NEG"
    line23 = Line(text, "test", 2, [])
    result = line23.hex()
    assert result == "0C10 2700"
    assert line23.error == False

    # 10101111rrrrrrrr JG r
    text = "JG label24"
    line24 = Line(text, "test", 2, [])
    result = line24.hex()
    assert result == "0C11 AF84"
    assert line24.error == False

    # 01001101oooooooo TST X, o
    text = "TST X, 251"
    line25 = Line(text, "test", 2, [])
    result = line25.hex()
    assert result == "0C12 4DFB"
    assert line25.error == False

    # 01110101oooooooo OR X, o
    text = "OR X, 154"
    line26 = Line(text, "test", 2, [])
    result = line26.hex()
    assert result == "0C13 759A"
    assert line26.error == False

    # 01110100mmmmmmmm OR m
    text = "OR 0x7f"
    line27 = Line(text, "test", 2, [])
    result = line27.hex()
    assert result == "0C14 747F"
    assert line27.error == False

    # 00011000mmmmmmmm SBB m
    text = "SBB 0x3b"
    line28 = Line(text, "test", 2, [])
    result = line28.hex()
    assert result == "0C15 183B"
    assert line28.error == False

    # 0000011111001010 CLU 
    text = "CLU"
    line29 = Line(text, "test", 2, [])
    result = line29.hex()
    assert result == "0C16 07CA"
    assert line29.error == False

    # 0000111001000000 DES 
    text = "DES"
    line30 = Line(text, "test", 2, [])
    result = line30.hex()
    assert result == "0C17 0E40"
    assert line30.error == False

    # 10001111rrrrrrrr JB r
    text = "JB label31"
    line31 = Line(text, "test", 2, [])
    result = line31.hex()
    assert result == "0C18 8F46"
    assert line31.error == False

    # 0000111001000000 DES 
    text = "DES"
    line32 = Line(text, "test", 2, [])
    result = line32.hex()
    assert result == "0C19 0E40"
    assert line32.error == False

    # 01000111kkkkkkkk ANDI k
    text = "ANDI 101"
    line33 = Line(text, "test", 2, [])
    result = line33.hex()
    assert result == "0C1A 4765"
    assert line33.error == False

    # 0000011111100100 CLC 
    text = "CLC"
    line34 = Line(text, "test", 2, [])
    result = line34.hex()
    assert result == "0C1B 07E4"
    assert line34.error == False

    # 10001111rrrrrrrr JB r
    text = "JB label35"
    line35 = Line(text, "test", 2, [])
    result = line35.hex()
    assert result == "0C1C 8FB4"
    assert line35.error == False

    # 0111111100100010 STU 
    text = "STU"
    line36 = Line(text, "test", 2, [])
    result = line36.hex()
    assert result == "0C1D 7F22"
    assert line36.error == False

    # 10101000rrrrrrrr JNV r
    text = "JNV label37"
    line37 = Line(text, "test", 2, [])
    result = line37.hex()
    assert result == "0C1E A8B2"
    assert line37.error == False

    # 0000011111001010 CLU 
    text = "CLU"
    line38 = Line(text, "test", 2, [])
    result = line38.hex()
    assert result == "0C1F 07CA"
    assert line38.error == False

    # 00010001oooooooo SUB X, o
    text = "SUB X, 9"
    line39 = Line(text, "test", 2, [])
    result = line39.hex()
    assert result == "0C20 1109"
    assert line39.error == False

    # 00110101oooooooo XOR X, o
    text = "XOR X, 203"
    line40 = Line(text, "test", 2, [])
    result = line40.hex()
    assert result == "0C21 35CB"
    assert line40.error == False

    # 00110000mmmmmmmm CMP m
    text = "CMP 0xc3"
    line41 = Line(text, "test", 2, [])
    result = line41.hex()
    assert result == "0C22 30C3"
    assert line41.error == False

    # 0000011110000000 TAX 
    text = "TAX"
    line42 = Line(text, "test", 2, [])
    result = line42.hex()
    assert result == "0C23 0780"
    assert line42.error == False

    # 0101001000000000 ROL 
    text = "ROL"
    line43 = Line(text, "test", 2, [])
    result = line43.hex()
    assert result == "0C24 5200"
    assert line43.error == False

    # 0111000100000000 LSR 
    text = "LSR"
    line44 = Line(text, "test", 2, [])
    result = line44.hex()
    assert result == "0C25 7100"
    assert line44.error == False

    # 00010011kkkkkkkk SUBI k
    text = "SUBI 17"
    line45 = Line(text, "test", 2, [])
    result = line45.hex()
    assert result == "0C26 1311"
    assert line45.error == False

    # 00110100mmmmmmmm XOR m
    text = "XOR 0x6d"
    line46 = Line(text, "test", 2, [])
    result = line46.hex()
    assert result == "0C27 346D"
    assert line46.error == False

    # 0010011100000000 NEG 
    text = "NEG"
    line47 = Line(text, "test", 2, [])
    result = line47.hex()
    assert result == "0C28 2700"
    assert line47.error == False

    # 01000100mmmmmmmm AND m
    text = "AND 0x82"
    line48 = Line(text, "test", 2, [])
    result = line48.hex()
    assert result == "0C29 4482"
    assert line48.error == False

    # 0010011100000000 NEG 
    text = "NEG"
    line49 = Line(text, "test", 2, [])
    result = line49.hex()
    assert result == "0C2A 2700"
    assert line49.error == False

    # 10011111rrrrrrrr JE r
    text = "JE label50"
    line50 = Line(text, "test", 2, [])
    result = line50.hex()
    assert result == "0C2B 9F82"
    assert line50.error == False

    # 10111011rrrrrrrr JGE r
    text = "JGE label51"
    line51 = Line(text, "test", 2, [])
    result = line51.hex()
    assert result == "0C2C BB75"
    assert line51.error == False

    # 10101111rrrrrrrr JG r
    text = "JG label52"
    line52 = Line(text, "test", 2, [])
    result = line52.hex()
    assert result == "0C2D AFAC"
    assert line52.error == False

    # 0000011101101001 CLI 
    text = "CLI"
    line53 = Line(text, "test", 2, [])
    result = line53.hex()
    assert result == "0C2E 0769"
    assert line53.error == False

    # 10001011rrrrrrrr JBE r
    text = "JBE label54"
    line54 = Line(text, "test", 2, [])
    result = line54.hex()
    assert result == "0C2F 8B91"
    assert line54.error == False

    # 0000011001000000 INS 
    text = "INS"
    line55 = Line(text, "test", 2, [])
    result = line55.hex()
    assert result == "0C30 0640"
    assert line55.error == False

    # 0010110100000000 NOT 
    text = "NOT"
    line56 = Line(text, "test", 2, [])
    result = line56.hex()
    assert result == "0C31 2D00"
    assert line56.error == False

    # 10111011rrrrrrrr JGE r
    text = "JGE label57"
    line57 = Line(text, "test", 2, [])
    result = line57.hex()
    assert result == "0C32 BBDB"
    assert line57.error == False

    # 0101001000000000 ROL 
    text = "ROL"
    line58 = Line(text, "test", 2, [])
    result = line58.hex()
    assert result == "0C33 5200"
    assert line58.error == False

    # 00110100mmmmmmmm XOR m
    text = "XOR 0x76"
    line59 = Line(text, "test", 2, [])
    result = line59.hex()
    assert result == "0C34 3476"
    assert line59.error == False

    # 00110110oooooooo XOR S, o
    text = "XOR S, 178"
    line60 = Line(text, "test", 2, [])
    result = line60.hex()
    assert result == "0C35 36B2"
    assert line60.error == False

    # 01000100mmmmmmmm AND m
    text = "AND 0x1f"
    line61 = Line(text, "test", 2, [])
    result = line61.hex()
    assert result == "0C36 441F"
    assert line61.error == False

    # 01110110oooooooo OR S, o
    text = "OR S, 102"
    line62 = Line(text, "test", 2, [])
    result = line62.hex()
    assert result == "0C37 7666"
    assert line62.error == False

    # 0000011101010000 TAS 
    text = "TAS"
    line63 = Line(text, "test", 2, [])
    result = line63.hex()
    assert result == "0C38 0750"
    assert line63.error == False

    # 10010000pppppppp IN p
    text = "IN 0xae"
    line64 = Line(text, "test", 2, [])
    result = line64.hex()
    assert result == "0C39 90AE"
    assert line64.error == False

    # 00110101oooooooo XOR X, o
    text = "XOR X, 18"
    line65 = Line(text, "test", 2, [])
    result = line65.hex()
    assert result == "0C3A 3512"
    assert line65.error == False

    # 00110000mmmmmmmm CMP m
    text = "CMP 0xda"
    line66 = Line(text, "test", 2, [])
    result = line66.hex()
    assert result == "0C3B 30DA"
    assert line66.error == False

    # 10111011rrrrrrrr JGE r
    text = "JGE label67"
    line67 = Line(text, "test", 2, [])
    result = line67.hex()
    assert result == "0C3C BB91"
    assert line67.error == False

    # 00010011kkkkkkkk SUBI k
    text = "SUBI 54"
    line68 = Line(text, "test", 2, [])
    result = line68.hex()
    assert result == "0C3D 1336"
    assert line68.error == False

    # 0111101100000000 DEC 
    text = "DEC"
    line69 = Line(text, "test", 2, [])
    result = line69.hex()
    assert result == "0C3E 7B00"
    assert line69.error == False

    # 10101100rrrrrrrr JLE r
    text = "JLE label70"
    line70 = Line(text, "test", 2, [])
    result = line70.hex()
    assert result == "0C3F ACF0"
    assert line70.error == False

    # 01110110oooooooo OR S, o
    text = "OR S, 175"
    line71 = Line(text, "test", 2, [])
    result = line71.hex()
    assert result == "0C40 76AF"
    assert line71.error == False

    # 01110101oooooooo OR X, o
    text = "OR X, 92"
    line72 = Line(text, "test", 2, [])
    result = line72.hex()
    assert result == "0C41 755C"
    assert line72.error == False

    # 0000111001000000 DES 
    text = "DES"
    line73 = Line(text, "test", 2, [])
    result = line73.hex()
    assert result == "0C42 0E40"
    assert line73.error == False

    # 0000010110000000 INX 
    text = "INX"
    line74 = Line(text, "test", 2, [])
    result = line74.hex()
    assert result == "0C43 0580"
    assert line74.error == False

    # 0000011111001010 CLU 
    text = "CLU"
    line75 = Line(text, "test", 2, [])
    result = line75.hex()
    assert result == "0C44 07CA"
    assert line75.error == False

    # 10110000pppppppp OUT p
    text = "OUT 0x3e"
    line76 = Line(text, "test", 2, [])
    result = line76.hex()
    assert result == "0C45 B03E"
    assert line76.error == False

    # 10000000mmmmmmmm LDD m
    text = "LDD 0x21"
    line77 = Line(text, "test", 2, [])
    result = line77.hex()
    assert result == "0C46 8021"
    assert line77.error == False

    # 01001111kkkkkkkk TSTI k
    text = "TSTI 28"
    line78 = Line(text, "test", 2, [])
    result = line78.hex()
    assert result == "0C47 4F1C"
    assert line78.error == False

    # 10111100rrrrrrrr JNU r
    text = "JNU label79"
    line79 = Line(text, "test", 2, [])
    result = line79.hex()
    assert result == "0C48 BC8C"
    assert line79.error == False

    # 00011010oooooooo SBB S, o
    text = "SBB S, 255"
    line80 = Line(text, "test", 2, [])
    result = line80.hex()
    assert result == "0C49 1AFF"
    assert line80.error == False

    # 10101100rrrrrrrr JLE r
    text = "JLE label81"
    line81 = Line(text, "test", 2, [])
    result = line81.hex()
    assert result == "0C4A ACD1"
    assert line81.error == False

    # 00110000mmmmmmmm CMP m
    text = "CMP 0xb4"
    line82 = Line(text, "test", 2, [])
    result = line82.hex()
    assert result == "0C4B 30B4"
    assert line82.error == False

    # 0110011100000001 TXA 
    text = "TXA"
    line83 = Line(text, "test", 2, [])
    result = line83.hex()
    assert result == "0C4C 6701"
    assert line83.error == False

    # 00110100mmmmmmmm XOR m
    text = "XOR 0x4"
    line84 = Line(text, "test", 2, [])
    result = line84.hex()
    assert result == "0C4D 3404"
    assert line84.error == False

    # 10111000rrrrrrrr JL r
    text = "JL label85"
    line85 = Line(text, "test", 2, [])
    result = line85.hex()
    assert result == "0C4E B85D"
    assert line85.error == False

    # 10010000pppppppp IN p
    text = "IN 0xc5"
    line86 = Line(text, "test", 2, [])
    result = line86.hex()
    assert result == "0C4F 90C5"
    assert line86.error == False

    # 0101000000000000 RLC 
    text = "RLC"
    line87 = Line(text, "test", 2, [])
    result = line87.hex()
    assert result == "0C50 5000"
    assert line87.error == False

    # 00110101oooooooo XOR X, o
    text = "XOR X, 132"
    line88 = Line(text, "test", 2, [])
    result = line88.hex()
    assert result == "0C51 3584"
    assert line88.error == False

    # 0000000000000000 INC 
    text = "INC"
    line89 = Line(text, "test", 2, [])
    result = line89.hex()
    assert result == "0C52 0000"
    assert line89.error == False

    # 00110101oooooooo XOR X, o
    text = "XOR X, 1"
    line90 = Line(text, "test", 2, [])
    result = line90.hex()
    assert result == "0C53 3501"
    assert line90.error == False

    # 10000000mmmmmmmm LDD m
    text = "LDD 0x4a"
    line91 = Line(text, "test", 2, [])
    result = line91.hex()
    assert result == "0C54 804A"
    assert line91.error == False

    # 0001111100000000 RTS 
    text = "RTS"
    line92 = Line(text, "test", 2, [])
    result = line92.hex()
    assert result == "0C55 1F00"
    assert line92.error == False

    # 10001100rrrrrrrr JAE r
    text = "JAE label93"
    line93 = Line(text, "test", 2, [])
    result = line93.hex()
    assert result == "0C56 8CAF"
    assert line93.error == False

    # 10111000rrrrrrrr JL r
    text = "JL label94"
    line94 = Line(text, "test", 2, [])
    result = line94.hex()
    assert result == "0C57 B8DC"
    assert line94.error == False

    # 10111100rrrrrrrr JNU r
    text = "JNU label95"
    line95 = Line(text, "test", 2, [])
    result = line95.hex()
    assert result == "0C58 BCEF"
    assert line95.error == False

    # 01001101oooooooo TST X, o
    text = "TST X, 166"
    line96 = Line(text, "test", 2, [])
    result = line96.hex()
    assert result == "0C59 4DA6"
    assert line96.error == False

    # 0101100000000000 LSL 
    text = "LSL"
    line97 = Line(text, "test", 2, [])
    result = line97.hex()
    assert result == "0C5A 5800"
    assert line97.error == False

    # 0110011100000000 TSA 
    text = "TSA"
    line98 = Line(text, "test", 2, [])
    result = line98.hex()
    assert result == "0C5B 6700"
    assert line98.error == False

    # 01110111kkkkkkkk ORI k
    text = "ORI 25"
    line99 = Line(text, "test", 2, [])
    result = line99.hex()
    assert result == "0C5C 7719"
    assert line99.error == False

    # 0000000000000000 INC 
    text = "INC"
    line100 = Line(text, "test", 2, [])
    result = line100.hex()
    assert result == "0C5D 0000"
    assert line100.error == False

    # 0000011111001010 CLU 
    text = "CLU"
    line101 = Line(text, "test", 2, [])
    result = line101.hex()
    assert result == "0C5E 07CA"
    assert line101.error == False

    # 00011010oooooooo SBB S, o
    text = "SBB S, 243"
    line102 = Line(text, "test", 2, [])
    result = line102.hex()
    assert result == "0C5F 1AF3"
    assert line102.error == False

    # 0111000100000011 RRC 
    text = "RRC"
    line103 = Line(text, "test", 2, [])
    result = line103.hex()
    assert result == "0C60 7103"
    assert line103.error == False

    # 00010001oooooooo SUB X, o
    text = "SUB X, 4"
    line104 = Line(text, "test", 2, [])
    result = line104.hex()
    assert result == "0C61 1104"
    assert line104.error == False

    # 00010011kkkkkkkk SUBI k
    text = "SUBI 9"
    line105 = Line(text, "test", 2, [])
    result = line105.hex()
    assert result == "0C62 1309"
    assert line105.error == False

    # 0000011111001010 CLU 
    text = "CLU"
    line106 = Line(text, "test", 2, [])
    result = line106.hex()
    assert result == "0C63 07CA"
    assert line106.error == False

    # 10111011rrrrrrrr JGE r
    text = "JGE label107"
    line107 = Line(text, "test", 2, [])
    result = line107.hex()
    assert result == "0C64 BB01"
    assert line107.error == False

    # 01110111kkkkkkkk ORI k
    text = "ORI 50"
    line108 = Line(text, "test", 2, [])
    result = line108.hex()
    assert result == "0C65 7732"
    assert line108.error == False

    # 00010011kkkkkkkk SUBI k
    text = "SUBI 72"
    line109 = Line(text, "test", 2, [])
    result = line109.hex()
    assert result == "0C66 1348"
    assert line109.error == False

    # 00010010oooooooo SUB S, o
    text = "SUB S, 63"
    line110 = Line(text, "test", 2, [])
    result = line110.hex()
    assert result == "0C67 123F"
    assert line110.error == False

    # 0000001000000000 POPF 
    text = "POPF"
    line111 = Line(text, "test", 2, [])
    result = line111.hex()
    assert result == "0C68 0200"
    assert line111.error == False

    # 0010011100000000 NEG 
    text = "NEG"
    line112 = Line(text, "test", 2, [])
    result = line112.hex()
    assert result == "0C69 2700"
    assert line112.error == False

    # 00110110oooooooo XOR S, o
    text = "XOR S, 140"
    line113 = Line(text, "test", 2, [])
    result = line113.hex()
    assert result == "0C6A 368C"
    assert line113.error == False

    # 0000111001000000 DES 
    text = "DES"
    line114 = Line(text, "test", 2, [])
    result = line114.hex()
    assert result == "0C6B 0E40"
    assert line114.error == False

    # 0000111001000000 DES 
    text = "DES"
    line115 = Line(text, "test", 2, [])
    result = line115.hex()
    assert result == "0C6C 0E40"
    assert line115.error == False

    # 0000011001000000 INS 
    text = "INS"
    line116 = Line(text, "test", 2, [])
    result = line116.hex()
    assert result == "0C6D 0640"
    assert line116.error == False

    # 0000011110000000 TAX 
    text = "TAX"
    line117 = Line(text, "test", 2, [])
    result = line117.hex()
    assert result == "0C6E 0780"
    assert line117.error == False

    # 0000001000000000 POPF 
    text = "POPF"
    line118 = Line(text, "test", 2, [])
    result = line118.hex()
    assert result == "0C6F 0200"
    assert line118.error == False

    # 01000111kkkkkkkk ANDI k
    text = "ANDI 65"
    line119 = Line(text, "test", 2, [])
    result = line119.hex()
    assert result == "0C70 4741"
    assert line119.error == False

    # 0000001000000000 POPF 
    text = "POPF"
    line120 = Line(text, "test", 2, [])
    result = line120.hex()
    assert result == "0C71 0200"
    assert line120.error == False

    # 0110011100000001 TXA 
    text = "TXA"
    line121 = Line(text, "test", 2, [])
    result = line121.hex()
    assert result == "0C72 6701"
    assert line121.error == False

    # 00011000mmmmmmmm SBB m
    text = "SBB 0x3f"
    line122 = Line(text, "test", 2, [])
    result = line122.hex()
    assert result == "0C73 183F"
    assert line122.error == False

    # 00110111kkkkkkkk XORI k
    text = "XORI 228"
    line123 = Line(text, "test", 2, [])
    result = line123.hex()
    assert result == "0C74 37E4"
    assert line123.error == False

    # 01110110oooooooo OR S, o
    text = "OR S, 20"
    line124 = Line(text, "test", 2, [])
    result = line124.hex()
    assert result == "0C75 7614"
    assert line124.error == False

    # 00010010oooooooo SUB S, o
    text = "SUB S, 218"
    line125 = Line(text, "test", 2, [])
    result = line125.hex()
    assert result == "0C76 12DA"
    assert line125.error == False

    # 10101011rrrrrrrr JV r
    text = "JV label126"
    line126 = Line(text, "test", 2, [])
    result = line126.hex()
    assert result == "0C77 AB4F"
    assert line126.error == False

    # 10001100rrrrrrrr JAE r
    text = "JAE label127"
    line127 = Line(text, "test", 2, [])
    result = line127.hex()
    assert result == "0C78 8C1B"
    assert line127.error == False

    # 01110101oooooooo OR X, o
    text = "OR X, 53"
    line128 = Line(text, "test", 2, [])
    result = line128.hex()
    assert result == "0C79 7535"
    assert line128.error == False

    # 0101000000000000 RLC 
    text = "RLC"
    line129 = Line(text, "test", 2, [])
    result = line129.hex()
    assert result == "0C7A 5000"
    assert line129.error == False

    # 0111000100000001 ASR 
    text = "ASR"
    line130 = Line(text, "test", 2, [])
    result = line130.hex()
    assert result == "0C7B 7101"
    assert line130.error == False

    # 10011111rrrrrrrr JE r
    text = "JE label131"
    line131 = Line(text, "test", 2, [])
    result = line131.hex()
    assert result == "0C7C 9FB4"
    assert line131.error == False

    # 00010011kkkkkkkk SUBI k
    text = "SUBI 191"
    line132 = Line(text, "test", 2, [])
    result = line132.hex()
    assert result == "0C7D 13BF"
    assert line132.error == False

    # 01000111kkkkkkkk ANDI k
    text = "ANDI 178"
    line133 = Line(text, "test", 2, [])
    result = line133.hex()
    assert result == "0C7E 47B2"
    assert line133.error == False

    # 10011000rrrrrrrr JNS r
    text = "JNS label134"
    line134 = Line(text, "test", 2, [])
    result = line134.hex()
    assert result == "0C7F 9845"
    assert line134.error == False

    # 10101100rrrrrrrr JLE r
    text = "JLE label135"
    line135 = Line(text, "test", 2, [])
    result = line135.hex()
    assert result == "0C80 AC8D"
    assert line135.error == False

    # 0110011100000000 TSA 
    text = "TSA"
    line136 = Line(text, "test", 2, [])
    result = line136.hex()
    assert result == "0C81 6700"
    assert line136.error == False

    # 01001101oooooooo TST X, o
    text = "TST X, 38"
    line137 = Line(text, "test", 2, [])
    result = line137.hex()
    assert result == "0C82 4D26"
    assert line137.error == False

    # 10111100rrrrrrrr JNU r
    text = "JNU label138"
    line138 = Line(text, "test", 2, [])
    result = line138.hex()
    assert result == "0C83 BC36"
    assert line138.error == False

    # 10001001kkkkkkkk LDI k
    text = "LDI 242"
    line139 = Line(text, "test", 2, [])
    result = line139.hex()
    assert result == "0C84 89F2"
    assert line139.error == False

    # 10000000mmmmmmmm LDD m
    text = "LDD 0xe4"
    line140 = Line(text, "test", 2, [])
    result = line140.hex()
    assert result == "0C85 80E4"
    assert line140.error == False

    # 01001110oooooooo TST S, o
    text = "TST S, 33"
    line141 = Line(text, "test", 2, [])
    result = line141.hex()
    assert result == "0C86 4E21"
    assert line141.error == False

    # 0001111100000000 RTS 
    text = "RTS"
    line142 = Line(text, "test", 2, [])
    result = line142.hex()
    assert result == "0C87 1F00"
    assert line142.error == False

    # 01000110oooooooo AND S, o
    text = "AND S, 122"
    line143 = Line(text, "test", 2, [])
    result = line143.hex()
    assert result == "0C88 467A"
    assert line143.error == False

    # 00010000mmmmmmmm SUB m
    text = "SUB 0x20"
    line144 = Line(text, "test", 2, [])
    result = line144.hex()
    assert result == "0C89 1020"
    assert line144.error == False

    # 01001111kkkkkkkk TSTI k
    text = "TSTI 52"
    line145 = Line(text, "test", 2, [])
    result = line145.hex()
    assert result == "0C8A 4F34"
    assert line145.error == False

    # 10111011rrrrrrrr JGE r
    text = "JGE label146"
    line146 = Line(text, "test", 2, [])
    result = line146.hex()
    assert result == "0C8B BBD1"
    assert line146.error == False

    # 10010000pppppppp IN p
    text = "IN 0x23"
    line147 = Line(text, "test", 2, [])
    result = line147.hex()
    assert result == "0C8C 9023"
    assert line147.error == False

    # 0111111110000001 STI 
    text = "STI"
    line148 = Line(text, "test", 2, [])
    result = line148.hex()
    assert result == "0C8D 7F81"
    assert line148.error == False

    # 0101100000000000 LSL 
    text = "LSL"
    line149 = Line(text, "test", 2, [])
    result = line149.hex()
    assert result == "0C8E 5800"
    assert line149.error == False

    # 0010011100000000 NEG 
    text = "NEG"
    line150 = Line(text, "test", 2, [])
    result = line150.hex()
    assert result == "0C8F 2700"
    assert line150.error == False

    # 10001100rrrrrrrr JAE r
    text = "JAE label151"
    line151 = Line(text, "test", 2, [])
    result = line151.hex()
    assert result == "0C90 8C03"
    assert line151.error == False

    # 01001101oooooooo TST X, o
    text = "TST X, 162"
    line152 = Line(text, "test", 2, [])
    result = line152.hex()
    assert result == "0C91 4DA2"
    assert line152.error == False

    # 0110011100000001 TXA 
    text = "TXA"
    line153 = Line(text, "test", 2, [])
    result = line153.hex()
    assert result == "0C92 6701"
    assert line153.error == False

    # 01110111kkkkkkkk ORI k
    text = "ORI 106"
    line154 = Line(text, "test", 2, [])
    result = line154.hex()
    assert result == "0C93 776A"
    assert line154.error == False

    # 00110111kkkkkkkk XORI k
    text = "XORI 44"
    line155 = Line(text, "test", 2, [])
    result = line155.hex()
    assert result == "0C94 372C"
    assert line155.error == False

    # 01000101oooooooo AND X, o
    text = "AND X, 154"
    line156 = Line(text, "test", 2, [])
    result = line156.hex()
    assert result == "0C95 459A"
    assert line156.error == False

    # 0001111110000000 NOP 
    text = "NOP"
    line157 = Line(text, "test", 2, [])
    result = line157.hex()
    assert result == "0C96 1F80"
    assert line157.error == False

    # 01110101oooooooo OR X, o
    text = "OR X, 62"
    line158 = Line(text, "test", 2, [])
    result = line158.hex()
    assert result == "0C97 753E"
    assert line158.error == False

    # 10010000pppppppp IN p
    text = "IN 0x32"
    line159 = Line(text, "test", 2, [])
    result = line159.hex()
    assert result == "0C98 9032"
    assert line159.error == False

    # 0001111100000000 RTS 
    text = "RTS"
    line160 = Line(text, "test", 2, [])
    result = line160.hex()
    assert result == "0C99 1F00"
    assert line160.error == False

    # 0000000000000000 INC 
    text = "INC"
    line161 = Line(text, "test", 2, [])
    result = line161.hex()
    assert result == "0C9A 0000"
    assert line161.error == False

    # 01000110oooooooo AND S, o
    text = "AND S, 65"
    line162 = Line(text, "test", 2, [])
    result = line162.hex()
    assert result == "0C9B 4641"
    assert line162.error == False

    # 00010001oooooooo SUB X, o
    text = "SUB X, 43"
    line163 = Line(text, "test", 2, [])
    result = line163.hex()
    assert result == "0C9C 112B"
    assert line163.error == False

    # 00010001oooooooo SUB X, o
    text = "SUB X, 122"
    line164 = Line(text, "test", 2, [])
    result = line164.hex()
    assert result == "0C9D 117A"
    assert line164.error == False

    # 10001011rrrrrrrr JBE r
    text = "JBE label165"
    line165 = Line(text, "test", 2, [])
    result = line165.hex()
    assert result == "0C9E 8B79"
    assert line165.error == False

    # 01001100mmmmmmmm TST m
    text = "TST 0xab"
    line166 = Line(text, "test", 2, [])
    result = line166.hex()
    assert result == "0C9F 4CAB"
    assert line166.error == False

    # 10111011rrrrrrrr JGE r
    text = "JGE label167"
    line167 = Line(text, "test", 2, [])
    result = line167.hex()
    assert result == "0CA0 BBB4"
    assert line167.error == False

    # 10101100rrrrrrrr JLE r
    text = "JLE label168"
    line168 = Line(text, "test", 2, [])
    result = line168.hex()
    assert result == "0CA1 AC8B"
    assert line168.error == False

    # 10101100rrrrrrrr JLE r
    text = "JLE label169"
    line169 = Line(text, "test", 2, [])
    result = line169.hex()
    assert result == "0CA2 AC0E"
    assert line169.error == False

    # 0111111100100010 STU 
    text = "STU"
    line170 = Line(text, "test", 2, [])
    result = line170.hex()
    assert result == "0CA3 7F22"
    assert line170.error == False

    # 0000110110000000 DEX 
    text = "DEX"
    line171 = Line(text, "test", 2, [])
    result = line171.hex()
    assert result == "0CA4 0D80"
    assert line171.error == False

    # 0101000000000000 RLC 
    text = "RLC"
    line172 = Line(text, "test", 2, [])
    result = line172.hex()
    assert result == "0CA5 5000"
    assert line172.error == False

    # 01001101oooooooo TST X, o
    text = "TST X, 43"
    line173 = Line(text, "test", 2, [])
    result = line173.hex()
    assert result == "0CA6 4D2B"
    assert line173.error == False

    # 01000101oooooooo AND X, o
    text = "AND X, 51"
    line174 = Line(text, "test", 2, [])
    result = line174.hex()
    assert result == "0CA7 4533"
    assert line174.error == False

    # 00110011kkkkkkkk CMPI k
    text = "CMPI 190"
    line175 = Line(text, "test", 2, [])
    result = line175.hex()
    assert result == "0CA8 33BE"
    assert line175.error == False

    # 00110110oooooooo XOR S, o
    text = "XOR S, 11"
    line176 = Line(text, "test", 2, [])
    result = line176.hex()
    assert result == "0CA9 360B"
    assert line176.error == False

    # 0110011100000001 TXA 
    text = "TXA"
    line177 = Line(text, "test", 2, [])
    result = line177.hex()
    assert result == "0CAA 6701"
    assert line177.error == False

    # 00010010oooooooo SUB S, o
    text = "SUB S, 24"
    line178 = Line(text, "test", 2, [])
    result = line178.hex()
    assert result == "0CAB 1218"
    assert line178.error == False

    # 0111000100000001 ASR 
    text = "ASR"
    line179 = Line(text, "test", 2, [])
    result = line179.hex()
    assert result == "0CAC 7101"
    assert line179.error == False

    # 10101011rrrrrrrr JV r
    text = "JV label180"
    line180 = Line(text, "test", 2, [])
    result = line180.hex()
    assert result == "0CAD AB4D"
    assert line180.error == False

    # 10010000pppppppp IN p
    text = "IN 0x60"
    line181 = Line(text, "test", 2, [])
    result = line181.hex()
    assert result == "0CAE 9060"
    assert line181.error == False

    # 10101011rrrrrrrr JV r
    text = "JV label182"
    line182 = Line(text, "test", 2, [])
    result = line182.hex()
    assert result == "0CAF AB65"
    assert line182.error == False

    # 10001000rrrrrrrr JA r
    text = "JA label183"
    line183 = Line(text, "test", 2, [])
    result = line183.hex()
    assert result == "0CB0 88CB"
    assert line183.error == False

    # 0000011111001010 CLU 
    text = "CLU"
    line184 = Line(text, "test", 2, [])
    result = line184.hex()
    assert result == "0CB1 07CA"
    assert line184.error == False

    # 01110100mmmmmmmm OR m
    text = "OR 0xc5"
    line185 = Line(text, "test", 2, [])
    result = line185.hex()
    assert result == "0CB2 74C5"
    assert line185.error == False

    # 0101100000000000 LSL 
    text = "LSL"
    line186 = Line(text, "test", 2, [])
    result = line186.hex()
    assert result == "0CB3 5800"
    assert line186.error == False

    # 10100000mmmmmmmm STD m
    text = "STD 0xa6"
    line187 = Line(text, "test", 2, [])
    result = line187.hex()
    assert result == "0CB4 A0A6"
    assert line187.error == False

    # 00010001oooooooo SUB X, o
    text = "SUB X, 44"
    line188 = Line(text, "test", 2, [])
    result = line188.hex()
    assert result == "0CB5 112C"
    assert line188.error == False

    # 10001100rrrrrrrr JAE r
    text = "JAE label189"
    line189 = Line(text, "test", 2, [])
    result = line189.hex()
    assert result == "0CB6 8CC3"
    assert line189.error == False

    # 00110000mmmmmmmm CMP m
    text = "CMP 0xfe"
    line190 = Line(text, "test", 2, [])
    result = line190.hex()
    assert result == "0CB7 30FE"
    assert line190.error == False

    # 0010011100000000 NEG 
    text = "NEG"
    line191 = Line(text, "test", 2, [])
    result = line191.hex()
    assert result == "0CB8 2700"
    assert line191.error == False

    # 01000101oooooooo AND X, o
    text = "AND X, 221"
    line192 = Line(text, "test", 2, [])
    result = line192.hex()
    assert result == "0CB9 45DD"
    assert line192.error == False

    # 10001100rrrrrrrr JAE r
    text = "JAE label193"
    line193 = Line(text, "test", 2, [])
    result = line193.hex()
    assert result == "0CBA 8CE4"
    assert line193.error == False

    # 0111000100000011 RRC 
    text = "RRC"
    line194 = Line(text, "test", 2, [])
    result = line194.hex()
    assert result == "0CBB 7103"
    assert line194.error == False

    # 0101000000000000 RLC 
    text = "RLC"
    line195 = Line(text, "test", 2, [])
    result = line195.hex()
    assert result == "0CBC 5000"
    assert line195.error == False

    # 01001110oooooooo TST S, o
    text = "TST S, 120"
    line196 = Line(text, "test", 2, [])
    result = line196.hex()
    assert result == "0CBD 4E78"
    assert line196.error == False

    # 0000011101101001 CLI 
    text = "CLI"
    line197 = Line(text, "test", 2, [])
    result = line197.hex()
    assert result == "0CBE 0769"
    assert line197.error == False

    # 0010110100000000 NOT 
    text = "NOT"
    line198 = Line(text, "test", 2, [])
    result = line198.hex()
    assert result == "0CBF 2D00"
    assert line198.error == False

    # 10011100rrrrrrrr JNE r
    text = "JNE label199"
    line199 = Line(text, "test", 2, [])
    result = line199.hex()
    assert result == "0CC0 9C66"
    assert line199.error == False
    #########################################################################

    # test labels
    text = "Label: JBE Label"
    line200 = Line(text, "test", 2, [])
    instruction_num = 3066
    symbols = []
    result = line200.hex()
    assert result == "0CC1 8BFF"
    assert line200.error == False

    # test pseudo-ops
    # #include
    text = "#include 'file.asm'"
    line201 = Line(text, "test", 2, [])
    instruction_num = 3066
    symbols = []
    result = line201.hex()
    assert result == ""
    assert line201.error == False
    assert Line.include_files == ['file.asm']

    # test dataseg
    text = "#data"
    line202 = Line(text, "test", 2, [])
    instruction_num = 3066
    symbols = []
    result = line202.hex()
    assert result == ""
    assert line202.error == False
    assert Line.seg == 0

    # test code in dataseg => error
    text = "SBB X, 233"
    line203 = Line(text, "test", 2, [])
    instruction_num = 3066
    symbols = []
    assert line203.error == True

    # test pseudo-ops with labels => error
    text = "Label: #data"
    line204 = Line(text, "test", 2, [])
    instruction_num = 3066
    symbols = []
    assert line204.error == True

    # definitions
    text = "#= k <- 5"
    line205 = Line(text, "test", 2, [])
    instruction_num = 3266
    assert Line.symbols['k'] == '05'
    assert line205.error == False

    # macro definitions
    text = "#macro macro(m0,o1,m4,m5) {"
    lines = [
    "SBB m0",
    "SBB S, o1",
    "TAS",
    "TSA",
    "CMP m4",
    "CMP m5",
    "JMP label6"
    ]
    macro = Line(text, "test", 2, lines)
    assert macro.error == False
    instruction_num = 3266
    assert len(Line.macros) == 1
    result = macro.hex() # should not return num
    assert result == ''
    instruction_num

    # cseg
    text = "#code"
    line_cseg2 = Line(text, "test", 2, [])
    result = line_cseg2.hex()
    assert result == ""
    assert line_cseg2.error == False
    assert Line.seg == 1

    # macro in code
    text = "macro(0x22,0x05,0x27,0xf3)"
    linecodemacro = Line(text, "test", 2, [])
    instruction_num = 3266
    symbols = []
    result = linecodemacro.hex()
    assert result == """0CC2 1822
0CC3 1A05
0CC4 0750
0CC5 6700
0CC6 3027
0CC7 30F3
0CC8 CBE4
"""
    assert linecodemacro.error == False

    #data
    text = "#data"
    line300 = Line(text, "test", 2, [])
    instruction_num = instruction_num + 7
    symbols = []
    result = line300.hex()
    assert result == ''
    assert line300.error == False
    assert Line.seg == 0

    #byte
    text = "#byte BYTE"
    byte = Line(text, "test", 2, [])
    symbols = []
    result = byte.hex()
    assert result == ''
    assert byte.error == False
    instruction_num
    assert len(Line.bytes) == 100 # account for stack

    # #word
    text = "#word WORD"
    word = Line(text, "test", 2, [])
    symbols = []
    result = word.hex()
    assert result == ''
    assert word.error == False
    instruction_num
    assert len(Line.bytes) == 102 # word is just two bytes
    assert result == ''

    # code
    text = "#code"
    line_code2 = Line(text, "test", 2, [])
    assert line_code2.error == False
    assert Line.seg == 1
    assert line_code2.hex() == ''

    # test second org => error
    text = "#ORG"
    org2 = Line(text, "test", 2, [])
    assert org2.error == True
    assert Line.seg == 1

    # test labels with no instructions
    text = "Labelnoinstruction: "
    labelnoinst = Line(text, "test", 2, [])
    assert labelnoinst.error == False
    assert Line.seg == 1
    assert labelnoinst.hex() == '\n'
    labelnoinstruction = hex(Line.instructions_hexed)[2:].upper() # line number = instructions_hexed - 1
    labelnoinstruction = '0' * (4 - len(labelnoinstruction)) + labelnoinstruction
    assert Line.labels['Labelnoinstruction'] == labelnoinstruction.upper()

    # test invalid opcodes
    text = "Label15498: InvalidOpcode"
    invalidopcode = Line(text, "test", 2, [])
    assert invalidopcode.error == True
    

    # test tabs and spaces between things
    text = "JV\tLabelnoinstruction"
    tabopcodeoperands = Line(text, "test", 2, [])
    assert tabopcodeoperands.error == False
    result = tabopcodeoperands.hex()
    assert result == '0CC9 ABFF' # executed on next instruction
    instruction_num += 1

    # test include same file twice => error
    text = "#INCLUDE 'testfile.asm'"
    once_include = Line(text, 'test', 2, [])
    assert once_include.error == False
    assert 'testfile.asm' in Line.include_files
    result = once_include.hex()
    assert result == ''
    twice_include = Line(text, 'test', 2, [])
    assert twice_include.error == True


    # test jmp pc
    text = "JV\t$"
    tabopcodeoperands = Line(text, "test", 2, [])
    assert tabopcodeoperands.error == False
    result = tabopcodeoperands.hex()
    assert result == '0CCA ABFF' # executed on next instruction

    text = "JMP\t$"
    tabopcodeoperands = Line(text, "test", 2, [])
    assert tabopcodeoperands.error == False
    result = tabopcodeoperands.hex()
    assert result == '0CCB CCCB' # executed on next instruction



if __name__ == '__main__':
    test_line()