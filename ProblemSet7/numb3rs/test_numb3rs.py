from numb3rs import validate

def main():
    testformat()
    testrange()

def testformat():
    assert validate(r'1.2.3.4')==True
    assert validate(r'1.2.3')==False
    assert validate(r'1.2')==False
    assert validate(r'1')==False

def testrange():
    assert validate(r'255.255.255.255')==True
    assert validate(r'255.255.255.500')==False
    assert validate(r'255.255.500.255')==False
    assert validate(r'255.500.255.255')==False
    assert validate(r'500.255.255.255')==False

if __name__ == "__main__":
    main()