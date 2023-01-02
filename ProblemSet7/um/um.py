import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    unlist = re.findall(r"\b\W*um\W*", s, re.IGNORECASE)
    """
    "unlist = re.findall(r"\b\W*um\W", s, re.IGNORECASE)"
    :( um.py yields 1 for "um"
    Cause expected "1", not "0\n"
    Log running python3 testing.py...
        sending input um...
        checking for output "1"...
    """
    return len(unlist)


if __name__ == "__main__":
    main()
