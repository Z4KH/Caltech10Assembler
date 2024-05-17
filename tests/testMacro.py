"""
This file is used by pytest to test the Macro class.
"""

from Macro import Macro

def test_macro():
    
    lines = [
        'LD X+4'
        'LD X++10'
        'LD X- + 21'
        'LD +   X + 21'
        'LD X + arg'
    ]
    
    arguments = 'arg, arg2'
    macro = Macro('macro', arguments, lines, 'test', 2)
    hex = macro.hex('4', 0, [], [], False, [])
    assert hex == '0000.....'##########