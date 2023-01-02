from um import count

def main():
    testupperlowercase()
    testwordum()
    testspace()

def testupperlowercase():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def testwordum():
    assert count("yummy") == 0

def testspace():
    assert count("hello world um") == 1
    assert count("um?") == 1

if __name__ == "__main__":
    main()