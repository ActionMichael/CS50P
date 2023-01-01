from fuel import convert, gauge

def main():
    test_convert()
    test_gauge()

#assert 陳述在程式中安插除錯用的斷言（Assertion）檢查時很方便的一個方式
def test_convert():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("1/100") == 1
    assert convert("99/100") == 99
    with pytest.raises(ValueError):
        convert('cat/dog')
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_gauge():
    assert gauge(25) == '25%'
    assert gauge(50) == "50%"
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'

if __name__ == "__main__":
    main()
