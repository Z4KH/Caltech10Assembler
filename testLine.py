"""
This file is used by pytest to test the Line class.
"""

from Line import Line

def test_line():
    labels = {
    'label0': '0C25',
    'label1': '0C17',
    'label2': '0BE2',
    'label3': '0BF8',
    'label4': '0B81',
    'label5': '0C68',
    'label6': '0BC9',
    'label7': '0BFD',
    'label8': '0BA0',
    'label9': '0C81',
    'label10': '0C67',
    'label11': '0C56',
    'label12': '0BA0',
    'label13': '0C05',
    'label14': '0C2E',
    'label15': '0C6F',
    'label16': '0B9F',
    'label17': '0BEC',
    'label18': '0C1E',
    'label19': '0C06',
    'label20': '0C2D',
    'label21': '0BD4',
    'label22': '0BBD',
    'label23': '0C3D',
    'label24': '0BEB',
    'label25': '0C90',
    'label26': '0C75',
    'label27': '0C76',
    'label28': '0C34',
    'label29': '0C80',
    'label30': '0B9D',
    'label31': '0C5D',
    'label32': '0C80',
    'label33': '0C29',
    'label34': '0C2A',
    'label35': '0C53',
    'label36': '0BC0',
    'label37': '0BA0',
    'label38': '0C63',
    'label39': '0C22',
    'label40': '0BFF',
    'label41': '0C2B',
    'label42': '0C52',
    'label43': '0C8D',
    'label44': '0BCF',
    'label45': '0BCC',
    'label46': '0BBB',
    'label47': '0C40',
    'label48': '0C44',
    'label49': '0C11',
    'label50': '0BAC',
    'label51': '0C94',
    'label52': '0C30',
    'label53': '0BDF',
    'label54': '0C78',
    'label55': '0C66',
    'label56': '0C2A',
    'label57': '0C40',
    'label58': '0BF9',
    'label59': '0CAB',
    'label60': '0C35',
    'label61': '0C84',
    'label62': '0C79',
    'label63': '0C08',
    'label64': '0C30',
    'label65': '0C05',
    'label66': '0C74',
    'label67': '0C08',
    'label68': '0C85',
    'label69': '0C1E',
    'label70': '0C0F',
    'label71': '0C54',
    'label72': '0BDB',
    'label73': '0C9E',
    'label74': '0BE9',
    'label75': '0C26',
    'label76': '0C80',
    'label77': '0BFE',
    'label78': '0C8C',
    'label79': '0BE4',
    'label80': '0BD3',
    'label81': '0BF5',
    'label82': '0C04',
    'label83': '0C24',
    'label84': '0CC8',
    'label85': '0C30',
    'label86': '0C82',
    'label87': '0C29',
    'label88': '0CC4',
    'label89': '0CC7',
    'label90': '0C53',
    'label91': '0C02',
    'label92': '0C25',
    'label93': '0CA0',
    'label94': '0C0D',
    'label95': '0BE7',
    'label96': '0CCC',
    'label97': '0C37',
    'label98': '0CD1',
    'label99': '0C13',
    'label100': '0C73',
    'label101': '0C4C',
    'label102': '0C95',
    'label103': '0C20',
    'label104': '0C7D',
    'label105': '0BF4',
    'label106': '0C91',
    'label107': '0BE8',
    'label108': '0C2F',
    'label109': '0CDC',
    'label110': '0BF9',
    'label111': '0C19',
    'label112': '0C3B',
    'label113': '0C40',
    'label114': '0C50',
    'label115': '0CDB',
    'label116': '0C5D',
    'label117': '0CD9',
    'label118': '0C92',
    'label119': '0CC3',
    'label120': '0CC3',
    'label121': '0CC9',
    'label122': '0C2D',
    'label123': '0CF1',
    'label124': '0C66',
    'label125': '0C92',
    'label126': '0C27',
    'label127': '0C55',
    'label128': '0C18',
    'label129': '0C49',
    'label130': '0C1C',
    'label131': '0CC3',
    'label132': '0C07',
    'label133': '0C19',
    'label134': '0C05',
    'label135': '0C78',
    'label136': '0C25',
    'label137': '0CBA',
    'label138': '0C13',
    'label139': '0C39',
    'label140': '0C9D',
    'label141': '0C77',
    'label142': '0C57',
    'label143': '0C22',
    'label144': '0CC1',
    'label145': '0C52',
    'label146': '0C4A',
    'label147': '0C1E',
    'label148': '0CCD',
    'label149': '0C79',
    'label150': '0C67',
    'label151': '0CFD',
    'label152': '0C9F',
    'label153': '0CA0',
    'label154': '0CEC',
    'label155': '0C94',
    'label156': '0CA2',
    'label157': '0D10',
    'label158': '0D07',
    'label159': '0C1A',
    'label160': '0C66',
    'label161': '0C2E',
    'label162': '0C96',
    'label163': '0C94',
    'label164': '0C5F',
    'label165': '0C5D',
    'label166': '0CE3',
    'label167': '0C9E',
    'label168': '0C40',
    'label169': '0C5B',
    'label170': '0C70',
    'label171': '0C45',
    'label172': '0C3A',
    'label173': '0C7E',
    'label174': '0C4C',
    'label175': '0C9E',
    'label176': '0C7A',
    'label177': '0D20',
    'label178': '0C2D',
    'label179': '0CD6',
    'label180': '0CBD',
    'label181': '0C83',
    'label182': '0C4B',
    'label183': '0D0C',
    'label184': '0C87',
    'label185': '0C6A',
    'label186': '0D03',
    'label187': '0D08',
    'label188': '0C39',
    'label189': '0C66',
    'label190': '0C48',
    'label191': '0CB0',
    'label192': '0CA3',
    'label193': '0CA3',
    'label194': '0C4B',
    'label195': '0CA7',
    'label196': '0C57',
    'label197': '0CDD',
    'label198': '0C83',
    'label199': '0C8B',
    }
    Line.labels = labels

    # code
    text = "#code"
    line_code = Line(text, "test", 2, [])
    #assert hex == f"{} 8C1C"
    assert line_code.error == False
    assert Line.seg == 1
    assert line_code.hex() == ''

    # data in code seg => error
    text = "#byte TestByte"
    line_datacseg = Line(text, "test", 2, [])
    #assert hex == f"{} 8C1C"
    assert line_datacseg.error == True
    assert line_datacseg.hex() == ''

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
    #assert hex == "0BFC 76FC"
    assert line_3.error == False
    assert len(Line.preOrg) == 3

    # stack init
    text = "#stack 100 0xF5"
    stack = Line(text, "test", 2, [])
    assert Line.stack == ('F5', 245, 144) # stack start -> stack end 
    assert stack.hex() == ''

    # test #org first
    text = "#org"
    org = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = org.hex()
    assert hex == "0000 89F5\n0001 0750" # need to load s with stack pointer
    assert org.error == False
    assert Line.org == True

##############################################################################

    Line.instructions = 3065


    # 00011011kkkkkkkk SBBI k
    text = "SBBI k"
    line0 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line0.hex()
    assert hex == "0BF9 1B2C"
    assert line0.error == False

    # 10001100rrrrrrrr JAE r
    text = "JAE label1"
    line1 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line1.hex()
    assert hex == "0BFA 8C1C"
    assert line1.error == False

    # 10111100rrrrrrrr JNU r
    text = "JNU label2"
    line2 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line2.hex()
    assert hex == "0BFB BCE6"
    assert line2.error == False

    # 01110110oooooooo OR S, o
    text = "OR S, 252"
    line3 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line3.hex()
    assert hex == "0BFC 76FC"
    assert line3.error == False

    # 00010001oooooooo SUB X, o
    text = "SUB X, 132"
    line4 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line4.hex()
    assert hex == "0BFD 1184"
    assert line4.error == False

    # 00110010oooooooo CMP S, o
    text = "CMP S, 106"
    line5 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line5.hex()
    assert hex == "0BFE 326A"
    assert line5.error == False

    # 10001100rrrrrrrr JAE r
    text = "JAE label6"
    line6 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line6.hex()
    assert hex == "0BFF 8CC9"
    assert line6.error == False

    # 0000011101010000 TAS 
    text = "TAS"
    line7 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line7.hex()
    assert hex == "0C00 0750"
    assert line7.error == False

    # 00011000mmmmmmmm SBB m
    text = "SBB m"
    line8 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line8.hex()
    assert hex == "0C01 189F"
    assert line8.error == False

    # 0110011100000000 TSA 
    text = "TSA"
    line9 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line9.hex()
    assert hex == "0C02 6700"
    assert line9.error == False

    # 0000000000000000 INC 
    text = "INC"
    line10 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line10.hex()
    assert hex == "0C03 0000"
    assert line10.error == False

    # 00110001oooooooo CMP X, o
    text = "CMP X, 82"
    line11 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line11.hex()
    assert hex == "0C04 3152"
    assert line11.error == False

    # 0001111100000000 RTS 
    text = "RTS"
    line12 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line12.hex()
    assert hex == "0C05 1F00"
    assert line12.error == False

    # 01000111kkkkkkkk ANDI k
    text = "ANDI k"
    line13 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line13.hex()
    assert hex == "0C06 47FF"
    assert line13.error == False

    # 00010011kkkkkkkk SUBI k
    text = "SUBI k"
    line14 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line14.hex()
    assert hex == "0C07 1327"
    assert line14.error == False

    # 10111011rrrrrrrr JGE r
    text = "JGE label15"
    line15 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line15.hex()
    assert hex == "0C08 BB66"
    assert line15.error == False

    # 10101000rrrrrrrr JNV r
    text = "JNV label16"
    line16 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line16.hex()
    assert hex == "0C09 A895"
    assert line16.error == False

    # 0111111100100010 STU 
    text = "STU"
    line17 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line17.hex()
    assert hex == "0C0A 7F22"
    assert line17.error == False

    # 0111111100100010 STU 
    text = "STU"
    line18 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line18.hex()
    assert hex == "0C0B 7F22"
    assert line18.error == False

    # 00010001oooooooo SUB X, o
    text = "SUB X, 250"
    line19 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line19.hex()
    assert hex == "0C0C 11FA"
    assert line19.error == False

    # 0110011100000000 TSA 
    text = "TSA"
    line20 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line20.hex()
    assert hex == "0C0D 6700"
    assert line20.error == False

    # 0010110100000000 NOT 
    text = "NOT"
    line21 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line21.hex()
    assert hex == "0C0E 2D00"
    assert line21.error == False

    # 00110110oooooooo XOR S, o
    text = "XOR S, 174"
    line22 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line22.hex()
    assert hex == "0C0F 36AE"
    assert line22.error == False

    # 00110000mmmmmmmm CMP m
    text = "CMP m"
    line23 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line23.hex()
    assert hex == "0C10 302D"
    assert line23.error == False

    # 0000110110000000 DEX 
    text = "DEX"
    line24 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line24.hex()
    assert hex == "0C11 0D80"
    assert line24.error == False

    # 10111011rrrrrrrr JGE r
    text = "JGE label25"
    line25 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line25.hex()
    assert hex == "0C12 BB7D"
    assert line25.error == False

    # 10101100rrrrrrrr JLE r
    text = "JLE label26"
    line26 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line26.hex()
    assert hex == "0C13 AC61"
    assert line26.error == False

    # 0111101100000000 DEC 
    text = "DEC"
    line27 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line27.hex()
    assert hex == "0C14 7B00"
    assert line27.error == False

    # 0001111110000000 NOP 
    text = "NOP"
    line28 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line28.hex()
    assert hex == "0C15 1F80"
    assert line28.error == False

    # 00011001oooooooo SBB X, o
    text = "SBB X, 106"
    line29 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line29.hex()
    assert hex == "0C16 196A"
    assert line29.error == False

    # 10111111rrrrrrrr JU r
    text = "JU label30"
    line30 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line30.hex()
    assert hex == "0C17 BF85"
    assert line30.error == False

    # 0111000100000011 RRC 
    text = "RRC"
    line31 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line31.hex()
    assert hex == "0C18 7103"
    assert line31.error == False

    # 01110110oooooooo OR S, o
    text = "OR S, 103"
    line32 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line32.hex()
    assert hex == "0C19 7667"
    assert line32.error == False

    # 10100000mmmmmmmm STD m
    text = "STD m"
    line33 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line33.hex()
    assert hex == "0C1A A00F"
    assert line33.error == False

    # 0000000000000000 INC 
    text = "INC"
    line34 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line34.hex()
    assert hex == "0C1B 0000"
    assert line34.error == False

    # 10101011rrrrrrrr JV r
    text = "JV label35"
    line35 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line35.hex()
    assert hex == "0C1C AB36"
    assert line35.error == False

    # 10101011rrrrrrrr JV r
    text = "JV label36"
    line36 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line36.hex()
    assert hex == "0C1D ABA2"
    assert line36.error == False

    # 0000110110000000 DEX 
    text = "DEX"
    line37 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line37.hex()
    assert hex == "0C1E 0D80"
    assert line37.error == False

    # 0001111110000000 NOP 
    text = "NOP"
    line38 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line38.hex()
    assert hex == "0C1F 1F80"
    assert line38.error == False

    # 10011000rrrrrrrr JNS r
    text = "JNS label39"
    line39 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line39.hex()
    assert hex == "0C20 9801"
    assert line39.error == False

    # 00110010oooooooo CMP S, o
    text = "CMP S, 222"
    line40 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line40.hex()
    assert hex == "0C21 32DE"
    assert line40.error == False

    # 0000011001000000 INS 
    text = "INS"
    line41 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line41.hex()
    assert hex == "0C22 0640"
    assert line41.error == False

    # 10101111rrrrrrrr JG r
    text = "JG label42"
    line42 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line42.hex()
    assert hex == "0C23 AF2E"
    assert line42.error == False

    # 0000001000000000 POPF 
    text = "POPF"
    line43 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line43.hex()
    assert hex == "0C24 0200"
    assert line43.error == False

    # 0010011100000000 NEG 
    text = "NEG"
    line44 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line44.hex()
    assert hex == "0C25 2700"
    assert line44.error == False

    # 10101011rrrrrrrr JV r
    text = "JV label45"
    line45 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line45.hex()
    assert hex == "0C26 ABA5"
    assert line45.error == False

    # 10111100rrrrrrrr JNU r
    text = "JNU label46"
    line46 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line46.hex()
    assert hex == "0C27 BC93"
    assert line46.error == False

    # 10001100rrrrrrrr JAE r
    text = "JAE label47"
    line47 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line47.hex()
    assert hex == "0C28 8C17"
    assert line47.error == False

    # 10100000mmmmmmmm STD m
    text = "STD m"
    line48 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line48.hex()
    assert hex == "0C29 A01B"
    assert line48.error == False

    # 10111111rrrrrrrr JU r
    text = "JU label49"
    line49 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line49.hex()
    assert hex == "0C2A BFE6"
    assert line49.error == False

    # 0010011100000000 NEG 
    text = "NEG"
    line50 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line50.hex()
    assert hex == "0C2B 2700"
    assert line50.error == False

    # 10010000pppppppp IN p
    text = "IN p"
    line51 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line51.hex()
    assert hex == "0C2C 9068"
    assert line51.error == False

    # 10001001kkkkkkkk LDI k
    text = "LDI k"
    line52 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line52.hex()
    assert hex == "0C2D 8903"
    assert line52.error == False

    # 00010001oooooooo SUB X, o
    text = "SUB X, 177"
    line53 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line53.hex()
    assert hex == "0C2E 11B1"
    assert line53.error == False

    # 0000011001000000 INS 
    text = "INS"
    line54 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line54.hex()
    assert hex == "0C2F 0640"
    assert line54.error == False

    # 0000011101010000 TAS 
    text = "TAS"
    line55 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line55.hex()
    assert hex == "0C30 0750"
    assert line55.error == False

    # 0101001000000000 ROL 
    text = "ROL"
    line56 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line56.hex()
    assert hex == "0C31 5200"
    assert line56.error == False

    # 10011011rrrrrrrr JS r
    text = "JS label57"
    line57 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line57.hex()
    assert hex == "0C32 9B0D"
    assert line57.error == False

    # 0000000000000000 INC 
    text = "INC"
    line58 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line58.hex()
    assert hex == "0C33 0000"
    assert line58.error == False

    # 10111111rrrrrrrr JU r
    text = "JU label59"
    line59 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line59.hex()
    assert hex == "0C34 BF76"
    assert line59.error == False

    # 0101001000000000 ROL 
    text = "ROL"
    line60 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line60.hex()
    assert hex == "0C35 5200"
    assert line60.error == False

    # 0000111000000000 PUSHF 
    text = "PUSHF"
    line61 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line61.hex()
    assert hex == "0C36 0E00"
    assert line61.error == False

    # 0010110100000000 NOT 
    text = "NOT"
    line62 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line62.hex()
    assert hex == "0C37 2D00"
    assert line62.error == False

    # 00110011kkkkkkkk CMPI k
    text = "CMPI k"
    line63 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line63.hex()
    assert hex == "0C38 33D0"
    assert line63.error == False

    # 10101000rrrrrrrr JNV r
    text = "JNV label64"
    line64 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line64.hex()
    assert hex == "0C39 A8F6"
    assert line64.error == False

    # 00110010oooooooo CMP S, o
    text = "CMP S, 203"
    line65 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line65.hex()
    assert hex == "0C3A 32CB"
    assert line65.error == False

    # 00110011kkkkkkkk CMPI k
    text = "CMPI k"
    line66 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line66.hex()
    assert hex == "0C3B 3339"
    assert line66.error == False

    # 00011011kkkkkkkk SBBI k
    text = "SBBI k"
    line67 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line67.hex()
    assert hex == "0C3C 1BCC"
    assert line67.error == False

    # 01000100mmmmmmmm AND m
    text = "AND m"
    line68 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line68.hex()
    assert hex == "0C3D 4448"
    assert line68.error == False

    # 0000011110000000 TAX 
    text = "TAX"
    line69 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line69.hex()
    assert hex == "0C3E 0780"
    assert line69.error == False

    # 01001111kkkkkkkk TSTI k
    text = "TSTI k"
    line70 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line70.hex()
    assert hex == "0C3F 4FD0"
    assert line70.error == False

    # 10111100rrrrrrrr JNU r
    text = "JNU label71"
    line71 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line71.hex()
    assert hex == "0C40 BC13"
    assert line71.error == False

    # 0111000100000011 RRC 
    text = "RRC"
    line72 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line72.hex()
    assert hex == "0C41 7103"
    assert line72.error == False

    # 10001111rrrrrrrr JB r
    text = "JB label73"
    line73 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line73.hex()
    assert hex == "0C42 8F5B"
    assert line73.error == False

    # 0010110100000000 NOT 
    text = "NOT"
    line74 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line74.hex()
    assert hex == "0C43 2D00"
    assert line74.error == False

    # 01000100mmmmmmmm AND m
    text = "AND m"
    line75 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line75.hex()
    assert hex == "0C44 44E2"
    assert line75.error == False

    # 00011011kkkkkkkk SBBI k
    text = "SBBI k"
    line76 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line76.hex()
    assert hex == "0C45 1B3B"
    assert line76.error == False

    # 0000010110000000 INX 
    text = "INX"
    line77 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line77.hex()
    assert hex == "0C46 0580"
    assert line77.error == False

    # 0111000100000010 ROR 
    text = "ROR"
    line78 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line78.hex()
    assert hex == "0C47 7102"
    assert line78.error == False

    # 10101011rrrrrrrr JV r
    text = "JV label79"
    line79 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line79.hex()
    assert hex == "0C48 AB9B"
    assert line79.error == False

    # 0000111001000000 DES 
    text = "DES"
    line80 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line80.hex()
    assert hex == "0C49 0E40"
    assert line80.error == False

    # 00110101oooooooo XOR X, o
    text = "XOR X, 171"
    line81 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line81.hex()
    assert hex == "0C4A 35AB"
    assert line81.error == False

    # 00011000mmmmmmmm SBB m
    text = "SBB m"
    line82 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line82.hex()
    assert hex == "0C4B 18B9"
    assert line82.error == False

    # 0000011110000000 TAX 
    text = "TAX"
    line83 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line83.hex()
    assert hex == "0C4C 0780"
    assert line83.error == False

    # 01110100mmmmmmmm OR m
    text = "OR m"
    line84 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line84.hex()
    assert hex == "0C4D 747B"
    assert line84.error == False

    # 0000000000000000 INC 
    text = "INC"
    line85 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line85.hex()
    assert hex == "0C4E 0000"
    assert line85.error == False

    # 10001111rrrrrrrr JB r
    text = "JB label86"
    line86 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line86.hex()
    assert hex == "0C4F 8F32"
    assert line86.error == False

    # 10111000rrrrrrrr JL r
    text = "JL label87"
    line87 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line87.hex()
    assert hex == "0C50 B8D8"
    assert line87.error == False

    # 01110100mmmmmmmm OR m
    text = "OR m"
    line88 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line88.hex()
    assert hex == "0C51 7473"
    assert line88.error == False

    # 00010011kkkkkkkk SUBI k
    text = "SUBI k"
    line89 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line89.hex()
    assert hex == "0C52 1375"
    assert line89.error == False

    # 10000000mmmmmmmm LDD m
    text = "LDD m"
    line90 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line90.hex()
    assert hex == "0C53 80100"
    assert line90.error == False

    # 0010110100000000 NOT 
    text = "NOT"
    line91 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line91.hex()
    assert hex == "0C54 2D00"
    assert line91.error == False

    # 01001110oooooooo TST S, o
    text = "TST S, 208"
    line92 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line92.hex()
    assert hex == "0C55 4ED0"
    assert line92.error == False

    # 00011000mmmmmmmm SBB m
    text = "SBB m"
    line93 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line93.hex()
    assert hex == "0C56 184A"
    assert line93.error == False

    # 10001011rrrrrrrr JBE r
    text = "JBE label94"
    line94 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line94.hex()
    assert hex == "0C57 8BB5"
    assert line94.error == False

    # 10000000mmmmmmmm LDD m
    text = "LDD m"
    line95 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line95.hex()
    assert hex == "0C58 808F"
    assert line95.error == False

    # 01001111kkkkkkkk TSTI k
    text = "TSTI k"
    line96 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line96.hex()
    assert hex == "0C59 4F73"
    assert line96.error == False

    # 0111000100000000 LSR 
    text = "LSR"
    line97 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line97.hex()
    assert hex == "0C5A 7100"
    assert line97.error == False

    # 00110100mmmmmmmm XOR m
    text = "XOR m"
    line98 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line98.hex()
    assert hex == "0C5B 3476"
    assert line98.error == False

    # 10011100rrrrrrrr JNE r
    text = "JNE label99"
    line99 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line99.hex()
    assert hex == "0C5C 9CB6"
    assert line99.error == False

    # 0110011100000000 TSA 
    text = "TSA"
    line100 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line100.hex()
    assert hex == "0C5D 6700"
    assert line100.error == False

    # 0111000100000011 RRC 
    text = "RRC"
    line101 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line101.hex()
    assert hex == "0C5E 7103"
    assert line101.error == False

    # 0111111100100010 STU 
    text = "STU"
    line102 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line102.hex()
    assert hex == "0C5F 7F22"
    assert line102.error == False

    # 0000011111100100 CLC 
    text = "CLC"
    line103 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line103.hex()
    assert hex == "0C60 07E4"
    assert line103.error == False

    # 01001100mmmmmmmm TST m
    text = "TST m"
    line104 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line104.hex()
    assert hex == "0C61 4C1C"
    assert line104.error == False

    # 00110110oooooooo XOR S, o
    text = "XOR S, 146"
    line105 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line105.hex()
    assert hex == "0C62 3692"
    assert line105.error == False

    # 10001111rrrrrrrr JB r
    text = "JB label106"
    line106 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line106.hex()
    assert hex == "0C63 8F2D"
    assert line106.error == False

    # 0000011110000000 TAX 
    text = "TAX"
    line107 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line107.hex()
    assert hex == "0C64 0780"
    assert line107.error == False

    # 0000011110000000 TAX 
    text = "TAX"
    line108 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line108.hex()
    assert hex == "0C65 0780"
    assert line108.error == False

    # 10011000rrrrrrrr JNS r
    text = "JNS label109"
    line109 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line109.hex()
    assert hex == "0C66 9875"
    assert line109.error == False

    # 00110100mmmmmmmm XOR m
    text = "XOR m"
    line110 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line110.hex()
    assert hex == "0C67 3492"
    assert line110.error == False

    # 0000011101101001 CLI 
    text = "CLI"
    line111 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line111.hex()
    assert hex == "0C68 0769"
    assert line111.error == False

    # 00110100mmmmmmmm XOR m
    text = "XOR m"
    line112 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line112.hex()
    assert hex == "0C69 34D2"
    assert line112.error == False

    # 0000011111100100 CLC 
    text = "CLC"
    line113 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line113.hex()
    assert hex == "0C6A 07E4"
    assert line113.error == False

    # 01001110oooooooo TST S, o
    text = "TST S, 229"
    line114 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line114.hex()
    assert hex == "0C6B 4EE5"
    assert line114.error == False

    # 0001111100000000 RTS 
    text = "RTS"
    line115 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line115.hex()
    assert hex == "0C6C 1F00"
    assert line115.error == False

    # 01001111kkkkkkkk TSTI k
    text = "TSTI k"
    line116 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line116.hex()
    assert hex == "0C6D 4FF0"
    assert line116.error == False

    # 10001111rrrrrrrr JB r
    text = "JB label117"
    line117 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line117.hex()
    assert hex == "0C6E 8F6A"
    assert line117.error == False

    # 01110101oooooooo OR X, o
    text = "OR X, 35"
    line118 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line118.hex()
    assert hex == "0C6F 7523"
    assert line118.error == False

    # 00010001oooooooo SUB X, o
    text = "SUB X, 83"
    line119 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line119.hex()
    assert hex == "0C70 1153"
    assert line119.error == False

    # 00010011kkkkkkkk SUBI k
    text = "SUBI k"
    line120 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line120.hex()
    assert hex == "0C71 1352"
    assert line120.error == False

    # 0000011111001010 CLU 
    text = "CLU"
    line121 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line121.hex()
    assert hex == "0C72 07CA"
    assert line121.error == False

    # 0000010110000000 INX 
    text = "INX"
    line122 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line122.hex()
    assert hex == "0C73 0580"
    assert line122.error == False

    # 0111000100000010 ROR 
    text = "ROR"
    line123 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line123.hex()
    assert hex == "0C74 7102"
    assert line123.error == False

    # 0000011111100100 CLC 
    text = "CLC"
    line124 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line124.hex()
    assert hex == "0C75 07E4"
    assert line124.error == False

    # 00110101oooooooo XOR X, o
    text = "XOR X, 28"
    line125 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line125.hex()
    assert hex == "0C76 351C"
    assert line125.error == False

    # 0001111110000000 NOP 
    text = "NOP"
    line126 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line126.hex()
    assert hex == "0C77 1F80"
    assert line126.error == False

    # 0010011100000000 NEG 
    text = "NEG"
    line127 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line127.hex()
    assert hex == "0C78 2700"
    assert line127.error == False

    # 0111000100000011 RRC 
    text = "RRC"
    line128 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line128.hex()
    assert hex == "0C79 7103"
    assert line128.error == False

    # 10111000rrrrrrrr JL r
    text = "JL label129"
    line129 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line129.hex()
    assert hex == "0C7A B8CE"
    assert line129.error == False

    # 0111111100100010 STU 
    text = "STU"
    line130 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line130.hex()
    assert hex == "0C7B 7F22"
    assert line130.error == False

    # 10001111rrrrrrrr JB r
    text = "JB label131"
    line131 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line131.hex()
    assert hex == "0C7C 8F46"
    assert line131.error == False

    # 01110111kkkkkkkk ORI k
    text = "ORI k"
    line132 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line132.hex()
    assert hex == "0C7D 778A"
    assert line132.error == False

    # 10001000rrrrrrrr JA r
    text = "JA label133"
    line133 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line133.hex()
    assert hex == "0C7E 889A"
    assert line133.error == False

    # 10001111rrrrrrrr JB r
    text = "JB label134"
    line134 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line134.hex()
    assert hex == "0C7F 8F85"
    assert line134.error == False

    # 0111000100000011 RRC 
    text = "RRC"
    line135 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line135.hex()
    assert hex == "0C80 7103"
    assert line135.error == False

    # 00011000mmmmmmmm SBB m
    text = "SBB m"
    line136 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line136.hex()
    assert hex == "0C81 18A4"
    assert line136.error == False

    # 01110100mmmmmmmm OR m
    text = "OR m"
    line137 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line137.hex()
    assert hex == "0C82 7438"
    assert line137.error == False

    # 00010010oooooooo SUB S, o
    text = "SUB S, 144"
    line138 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line138.hex()
    assert hex == "0C83 1290"
    assert line138.error == False

    # 00110011kkkkkkkk CMPI k
    text = "CMPI k"
    line139 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line139.hex()
    assert hex == "0C84 33B5"
    assert line139.error == False

    # 10010000pppppppp IN p
    text = "IN p"
    line140 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line140.hex()
    assert hex == "0C85 9018"
    assert line140.error == False

    # 01110100mmmmmmmm OR m
    text = "OR m"
    line141 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line141.hex()
    assert hex == "0C86 74F1"
    assert line141.error == False

    # 10101011rrrrrrrr JV r
    text = "JV label142"
    line142 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line142.hex()
    assert hex == "0C87 ABCF"
    assert line142.error == False

    # 00110110oooooooo XOR S, o
    text = "XOR S, 154"
    line143 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line143.hex()
    assert hex == "0C88 369A"
    assert line143.error == False

    # 0101100000000000 LSL 
    text = "LSL"
    line144 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line144.hex()
    assert hex == "0C89 5800"
    assert line144.error == False

    # 01000110oooooooo AND S, o
    text = "AND S, 200"
    line145 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line145.hex()
    assert hex == "0C8A 46C8"
    assert line145.error == False

    # 01110100mmmmmmmm OR m
    text = "OR m"
    line146 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line146.hex()
    assert hex == "0C8B 74BF"
    assert line146.error == False

    # 10001000rrrrrrrr JA r
    text = "JA label147"
    line147 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line147.hex()
    assert hex == "0C8C 8891"
    assert line147.error == False

    # 10110000pppppppp OUT p
    text = "OUT p"
    line148 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line148.hex()
    assert hex == "0C8D B040"
    assert line148.error == False

    # 0110011100000001 TXA 
    text = "TXA"
    line149 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line149.hex()
    assert hex == "0C8E 6701"
    assert line149.error == False

    # 0101000000000000 RLC 
    text = "RLC"
    line150 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line150.hex()
    assert hex == "0C8F 5000"
    assert line150.error == False

    # 00110000mmmmmmmm CMP m
    text = "CMP m"
    line151 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line151.hex()
    assert hex == "0C90 306D"
    assert line151.error == False

    # 0000110110000000 DEX 
    text = "DEX"
    line152 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line152.hex()
    assert hex == "0C91 0D80"
    assert line152.error == False

    # 01110101oooooooo OR X, o
    text = "OR X, 14"
    line153 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line153.hex()
    assert hex == "0C92 750E"
    assert line153.error == False

    # 00110111kkkkkkkk XORI k
    text = "XORI k"
    line154 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line154.hex()
    assert hex == "0C93 3759"
    assert line154.error == False

    # 10010000pppppppp IN p
    text = "IN p"
    line155 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line155.hex()
    assert hex == "0C94 90100"
    assert line155.error == False

    # 0000011111001010 CLU 
    text = "CLU"
    line156 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line156.hex()
    assert hex == "0C95 07CA"
    assert line156.error == False

    # 0101100000000000 LSL 
    text = "LSL"
    line157 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line157.hex()
    assert hex == "0C96 5800"
    assert line157.error == False

    # 01110110oooooooo OR S, o
    text = "OR S, 112"
    line158 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line158.hex()
    assert hex == "0C97 7670"
    assert line158.error == False

    # 0000011111100100 CLC 
    text = "CLC"
    line159 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line159.hex()
    assert hex == "0C98 07E4"
    assert line159.error == False

    # 0001111100000000 RTS 
    text = "RTS"
    line160 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line160.hex()
    assert hex == "0C99 1F00"
    assert line160.error == False

    # 00110100mmmmmmmm XOR m
    text = "XOR m"
    line161 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line161.hex()
    assert hex == "0C9A 3494"
    assert line161.error == False

    # 0000011111100100 CLC 
    text = "CLC"
    line162 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line162.hex()
    assert hex == "0C9B 07E4"
    assert line162.error == False

    # 0101001000000000 ROL 
    text = "ROL"
    line163 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line163.hex()
    assert hex == "0C9C 5200"
    assert line163.error == False

    # 10011100rrrrrrrr JNE r
    text = "JNE label164"
    line164 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line164.hex()
    assert hex == "0C9D 9CC1"
    assert line164.error == False

    # 0101001000000000 ROL 
    text = "ROL"
    line165 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line165.hex()
    assert hex == "0C9E 5200"
    assert line165.error == False

    # 00010001oooooooo SUB X, o
    text = "SUB X, 68"
    line166 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line166.hex()
    assert hex == "0C9F 1144"
    assert line166.error == False

    # 0000111001000000 DES 
    text = "DES"
    line167 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line167.hex()
    assert hex == "0CA0 0E40"
    assert line167.error == False

    # 01001111kkkkkkkk TSTI k
    text = "TSTI k"
    line168 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line168.hex()
    assert hex == "0CA1 4F9F"
    assert line168.error == False

    # 0000011111001010 CLU 
    text = "CLU"
    line169 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line169.hex()
    assert hex == "0CA2 07CA"
    assert line169.error == False

    # 01001101oooooooo TST X, o
    text = "TST X, 205"
    line170 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line170.hex()
    assert hex == "0CA3 4DCD"
    assert line170.error == False

    # 0000111001000000 DES 
    text = "DES"
    line171 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line171.hex()
    assert hex == "0CA4 0E40"
    assert line171.error == False

    # 01001100mmmmmmmm TST m
    text = "TST m"
    line172 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line172.hex()
    assert hex == "0CA5 4C95"
    assert line172.error == False

    # 00110100mmmmmmmm XOR m
    text = "XOR m"
    line173 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line173.hex()
    assert hex == "0CA6 34D8"
    assert line173.error == False

    # 01000100mmmmmmmm AND m
    text = "AND m"
    line174 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line174.hex()
    assert hex == "0CA7 44A5"
    assert line174.error == False

    # 01000100mmmmmmmm AND m
    text = "AND m"
    line175 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line175.hex()
    assert hex == "0CA8 44F6"
    assert line175.error == False

    # 01001111kkkkkkkk TSTI k
    text = "TSTI k"
    line176 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line176.hex()
    assert hex == "0CA9 4FD1"
    assert line176.error == False

    # 10101011rrrrrrrr JV r
    text = "JV label177"
    line177 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line177.hex()
    assert hex == "0CAA AB75"
    assert line177.error == False

    # 0111000100000010 ROR 
    text = "ROR"
    line178 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line178.hex()
    assert hex == "0CAB 7102"
    assert line178.error == False

    # 0110011100000000 TSA 
    text = "TSA"
    line179 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line179.hex()
    assert hex == "0CAC 6700"
    assert line179.error == False

    # 0101100000000000 LSL 
    text = "LSL"
    line180 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line180.hex()
    assert hex == "0CAD 5800"
    assert line180.error == False

    # 00110000mmmmmmmm CMP m
    text = "CMP m"
    line181 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line181.hex()
    assert hex == "0CAE 30D5"
    assert line181.error == False

    # 10100000mmmmmmmm STD m
    text = "STD m"
    line182 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line182.hex()
    assert hex == "0CAF A09C"
    assert line182.error == False

    # 10110000pppppppp OUT p
    text = "OUT p"
    line183 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line183.hex()
    assert hex == "0CB0 B05C"
    assert line183.error == False

    # 0111000100000011 RRC 
    text = "RRC"
    line184 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line184.hex()
    assert hex == "0CB1 7103"
    assert line184.error == False

    # 10100000mmmmmmmm STD m
    text = "STD m"
    line185 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line185.hex()
    assert hex == "0CB2 A0B8"
    assert line185.error == False

    # 0111111100001100 STC 
    text = "STC"
    line186 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line186.hex()
    assert hex == "0CB3 7F0C"
    assert line186.error == False

    # 00010001oooooooo SUB X, o
    text = "SUB X, 84"
    line187 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line187.hex()
    assert hex == "0CB4 1154"
    assert line187.error == False

    # 10111111rrrrrrrr JU r
    text = "JU label188"
    line188 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line188.hex()
    assert hex == "0CB5 BF83"
    assert line188.error == False

    # 0000010110000000 INX 
    text = "INX"
    line189 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line189.hex()
    assert hex == "0CB6 0580"
    assert line189.error == False

    # 10001001kkkkkkkk LDI k
    text = "LDI k"
    line190 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line190.hex()
    assert hex == "0CB7 8991"
    assert line190.error == False

    # 0000000000000000 INC 
    text = "INC"
    line191 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line191.hex()
    assert hex == "0CB8 0000"
    assert line191.error == False

    # 0000010110000000 INX 
    text = "INX"
    line192 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line192.hex()
    assert hex == "0CB9 0580"
    assert line192.error == False

    # 00011001oooooooo SBB X, o
    text = "SBB X, 233"
    line193 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line193.hex()
    assert hex == "0CBA 19E9"
    assert line193.error == False

    # 01000110oooooooo AND S, o
    text = "AND S, 144"
    line194 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line194.hex()
    assert hex == "0CBB 4690"
    assert line194.error == False

    # 01110110oooooooo OR S, o
    text = "OR S, 235"
    line195 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line195.hex()
    assert hex == "0CBC 76EB"
    assert line195.error == False

    # 01110101oooooooo OR X, o
    text = "OR X, 154"
    line196 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line196.hex()
    assert hex == "0CBD 759A"
    assert line196.error == False

    # 0010011100000000 NEG 
    text = "NEG"
    line197 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line197.hex()
    assert hex == "0CBE 2700"
    assert line197.error == False

    # 00011000mmmmmmmm SBB m
    text = "SBB m"
    line198 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line198.hex()
    assert hex == "0CBF 18C4"
    assert line198.error == False

    # 00110101oooooooo XOR X, o
    text = "XOR X, 203"
    line199 = Line(text, "test", 2, [])
    instruction_num = 3065
    symbols = []
    (hex, num) = line199.hex()
    assert hex == "0CC0 35CB"
    assert line199.error == False

#########################################################################

    # test labels
    text = "Label: JBE Label"
    line200 = Line(text, "test", 2, [])
    instruction_num = 3066
    symbols = []
    (hex, num) = line200.hex()
    assert hex == "0CC1 8B00"
    assert line200.error == False

    # test pseudo-ops
    # #include
    text = "#include 'file.asm'"
    line201 = Line(text, "test", 2, [])
    instruction_num = 3066
    symbols = []
    (hex, num) = line201.hex()
    assert hex == ""
    assert line201.error == False
    assert Line.include_files == ['file.asm']

    # test dataseg
    text = "#data"
    line202 = Line(text, "test", 2, [])
    instruction_num = 3066
    symbols = []
    (hex, num) = line202.hex()
    assert hex == ""
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
    "JU label6"
    ]
    macro = Line(text, "test", 2), lines
    assert macro._ismacro == True
    assert macro.error == False
    instruction_num = 3266
    labels = {
    'label0': '1640',
    'label1': '1624',
    'label2': '1607',
    'label3': '1605',
    'label4': '1649',
    'label5': '1616',
    'label6': '160B',
    }
    arguments = "0x22,0x05,0x27,0xf3"
    assert len(Line.macros) == 1
    (hex, num) = macro.hex() # should not return num
    assert hex == ''
    assert num == instruction_num

    # cseg
    text = "#code"
    line_cseg2 = Line(text, "test", 2, [])
    (hex, num) = line_cseg2.hex()
    assert hex == ""
    assert line_cseg2.error == False
    assert Line.seg == 1

    # macro in code
    text = "macro(0x22,0x05,0x27,0xf3)"
    linecodemacro = Line(text, "test", 2, [])
    instruction_num = 3266
    symbols = []
    (hex, num) = linecodemacro.hex()
    assert hex == """0CC2 1822
0CC3 1A05
0CC4 0750
0CC5 6700
0CC6 3027
0CC7 30F3
0CC8 BFE6
"""
    assert linecodemacro.error == False
    assert num == instruction_num + 6

    #data
    text = "#data"
    line300 = Line(text, "test", 2, [])
    instruction_num = instruction_num + 7
    symbols = []
    (hex, num) = byte.hex()
    assert hex == ''
    assert line300.error == False
    assert num == instruction_num
    assert Line.seg == 0

    # #byte
    text = "#byte BYTE"
    byte = Line(text, "test", 2, [])
    symbols = []
    (hex, num) = byte.hex()
    assert hex == ''
    assert byte.error == False
    assert num == instruction_num
    assert len(Line.data) == 1

    # #word
    text = "#word WORD"
    word = Line(text, "test", 2, [])
    symbols = []
    (hex, num) = word.hex()
    assert hex == ''
    assert word.error == False
    assert num == instruction_num
    assert len(Line.data) == 2
    assert hex == ''

    # code
    text = "#code"
    line_code2 = Line(text, "test", 2, [])
    assert line_code2.error == False
    assert Line.seg == 1
    assert line_code2.hex() == ''

    # test second org => error
    text = "#org"
    org2 = Line(text, "test", 2, [])
    assert org2.error == True
    assert Line.seg == 1

    # test labels with no instructions
    text = "Labelnoinstruction: "
    labelnoinst = Line(text, "test", 2, [])
    assert labelnoinst.error == False
    assert Line.seg == 1
    assert labelnoinst.hex() == ''
    labelnoinstruction = '0' * (4 - len(hex(instruction_num + 1)[2:].upper())) + hex(instruction_num + 1)[2:].upper()
    assert Line.labels['Labelnoinstruction'] == labelnoinstruction.upper()

    # test invalid opcodes
    text = "Label15498: InvalidOpcode"
    invalidopcode = Line(text, "test", 2, [])
    assert invalidopcode.error == True
    

    # test tabs and spaces between things
    text = "JV\tLabelNoInstruction"
    tabopcodeoperands = Line(text, "test", 2, [])
    assert tabopcodeoperands.error == False
    (hex, num) = tabopcodeoperands.hex()
    assert hex == f'{labelnoinstruction.upper()} AB00'
    instruction_num += 1

    # handle code
    Line.handle_preOrg()
    line_1_addr = hex(instruction_num)[2:]
    line_1_addr = '0' * (4- len(line_1_addr)) + line_1_addr
    assert line_1.hex()[0] == f"{line_1_addr.upper()} 1F80"
    instruction_num += 1

    line_1_addr = hex(instruction_num)[2:]
    line_1_addr = '0' * (4- len(line_1_addr)) + line_1_addr
    assert line_2.hex()[0] == f"{line_1_addr.upper()} 1F80"
    instruction_num += 1

    line_1_addr = hex(instruction_num)[2:]
    line_1_addr = '0' * (4- len(line_1_addr)) + line_1_addr
    assert line_3.hex()[0] == f"{line_1_addr.upper()} 8C1C"
    instruction_num += 1


    # handle data
    Line.handle_data()
    assert Line.bytes == {'BYTE': '56','WORD[LOW]': '57', 'WORD[HIGH]': '58'}