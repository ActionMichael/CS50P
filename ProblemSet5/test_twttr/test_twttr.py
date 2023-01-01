from twttr import shorten

def main():
    test_twttr()


def test_twttr():
    #assert是取代if...沒有則print出結果...的所有程式碼，這是除錯的程式法
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("hello, WORLD") == "hll, WRLD"
    assert shorten("23") == "23"
    assert shorten("CS50") == "CS50"
    assert shorten(",.-_") == ",.-_"


if __name__ == "__main__":
    main()
