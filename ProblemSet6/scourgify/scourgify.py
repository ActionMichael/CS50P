import sys
import csv

def main():
    check_commend_line_arg()
    output = []
    #
    try:
        with open(sys.argv[1] , 'r') as cavfile:
            reader = csv.DictReader(cavfile)
            for row in reader:
                splitname = row["name"].split(",")
                output.append({'first':splitname[1].lstrip() , 'last':splitname[0].lstrip() , 'house':row["house"]})
    #
    except FileNotFoundError:
        sys.exit("File does not exist")
    #
    with open(sys.argv[2] , 'w') as file:
        writer = csv.DictWriter(file , fieldnames=["first" , "last" , "house"])
        writer.writerow({"first":"first" , "last":"last" , "house":"house"})
        for row in output:
            writer.writerow({"first":row["first"] , "last":row["last"] , "house":row["house"]})

def check_commend_line_arg():
    #check command line argument right 
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    #check is csv files or not
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
