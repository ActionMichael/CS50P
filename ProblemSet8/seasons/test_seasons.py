from seasons import checkbirthday

def main():
    testcheckbirthday()

def testcheckbirthday():
    assert checkbirthday("2010-09-24") == ("2010" , "09" , "24")
    assert checkbirthday("2010-9-24") == None
    assert checkbirthday("Sep 24, 2010") == None

if __name__ == "__main__":
    main()