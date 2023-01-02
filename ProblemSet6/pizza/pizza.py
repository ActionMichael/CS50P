from email import header
import sys
import csv
from tabulate import tabulate

def main():
    check_commend_line_arg()
    #
    table = []
    #
    try:
        with open(sys.argv[1] , 'r') as cavfile:
            reader = csv.reader(cavfile)
            for row in reader:
                table.append(row)
    #
    except FileNotFoundError:
        sys.exit("File does not exist")
    #
    print(tabulate(table[1:] , headers=table[0] , tablefmt="grid"))

def check_commend_line_arg():
    #check command line argument right 
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    #check is csv files or not
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
