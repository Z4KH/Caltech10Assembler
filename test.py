from Macro import Macro

def test_():
    arguments = "o2"
    lines = [
    "NOT",
    "JL label1",
    "TXA",
    "CMP S, 138",
    "JNS label4",
    ]
    macro = Macro("macro", arguments, lines, "test", 2)
    print(macro.error)
    print(macro._lines)
    arguments = "0x8a"
    instruction_num = 4727
    symbols = []
    labels = {
    'label0': '1268',
    'label1': '123D',
    'label2': '12BF',
    'label3': '1204',
    'label4': '12BD',
    }
    (hex, num) = macro.hex(arguments, instruction_num, symbols, labels, False, [])
    print(hex)
# assert hex == """1277 2D00
# 1278 B8C4
# 1279 6701
# 127A 328A
# 127B 9841
# """
test_()
# assert macro.error == False