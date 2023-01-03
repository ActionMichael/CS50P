from project import crawler, regular, drawing_and_save
import os

def main():
    test_crawler()
    test_regular()
    test_drawing_and_save()

def test_crawler():
    # Call crawler function
    crawler('0050.tw')
    # Check if txt file exists in directory
    assert os.path.exists('C:/Users/User/Desktop/CS50P/project/0050.tw-items.txt') == True

def test_regular():
    # Call regular function
    regular('0050.tw')
    # Check if txt file exists in directory
    assert os.path.exists('C:/Users/User/Desktop/CS50P/project/0050.tw.csv') == True

def test_drawing_and_save():
    # Call drawing_and_save function
    drawing_and_save('0050.tw')
    # Check if png file exists in directory
    assert os.path.exists('C:/Users/User/Desktop/CS50P/project/Stock Index of 0050.tw.png') == True

if __name__ == "__main__":
    main()
