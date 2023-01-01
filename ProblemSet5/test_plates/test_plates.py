from plates import is_valid

def main():
    letter_number()
    first_two_letter()
    middle_number()
    number_of_zero()
    not_character()

#assert 陳述在程式中安插除錯用的斷言（Assertion）檢查時很方便的一個方式
def letter_number():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def first_two_letter():
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("1A") == False
    assert is_valid("11") == False

def middle_number():
    assert is_valid("AAA123") == True
    assert is_valid("AA123A") == False

def number_of_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def not_character():
    assert is_valid("PI3.14") == False
    assert is_valid("PI3!14") == False
    assert is_valid("PI3 14") == False

if __name__ == "__main__":
    main()




"""
:) plates.py exists
:) input of CS50 yields output of Valid
:) input of ECTO88 yields output of Valid
:) input of NRVOUS yields output of Valid
:) input of CS05 yields output of Invalid
:) input of CS50P2 yields output of Invalid
:) input of PI3.14 yields output of Invalid
:) input of H yields output of Invalid
:) input of OUTATIME yields output of Invalid
"""
