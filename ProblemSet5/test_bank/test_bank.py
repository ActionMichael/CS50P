from bank import value

def main():
    test_value1()
    test_value2()
    test_value3()

#assert 陳述在程式中安插除錯用的斷言（Assertion）檢查時很方便的一個方式
#0
def test_value1():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("    hello     ") == 0
    #assert value["hello" , "Hello" , "    hello     "] == 0
    """
__________________________________________________________________________________________________ test_value1 ___________________________________________________________________________________________________ 

    def test_value1():
>       assert value["hello" , "Hello" , "    hello     "] == 0
E       TypeError: 'function' object is not subscriptable
test_bank.py:10: TypeError
"""

#20
def test_value2():
    assert value("hi") == 20
    assert value("hotel") == 20
    #assert value["hi" , "hotel"] == 20
"""
__________________________________________________________________________________________________ test_value2 ___________________________________________________________________________________________________ 

    def test_value2():
>       assert value["hi" , "hotel"] == 20
E       TypeError: 'function' object is not subscriptable
test_bank.py:13: TypeError
"""
#100
def test_value3():
    assert value("CS50") == 100
    assert value("50") == 100
    assert value("what's happen") == 100
    #assert value["CS50" , "50" , "what's happen"] == 100
    """
__________________________________________________________________________________________________ test_value3 ___________________________________________________________________________________________________ 

    def test_value3():
>       assert value["CS50" , "50" , "what's happen"] == 100
E       TypeError: 'function' object is not subscriptable
test_bank.py:16: TypeError
"""

if __name__ == "__main__":
    main()
