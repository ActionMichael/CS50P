import sys

if len(sys.argv) == 2:
    if ".py" in sys.argv[1]:
        try:
            with open(sys.argv[1]) as file:
                nlines = 0
                for line in file:
                    if not line.lstrip().startswith("#") and line.lstrip() != '':
                        nlines += 1
            print(nlines)
        except FileNotFoundError:
            print("File does not exist")
    elif ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
