def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    cut_money_syntex = d.replace("$" , "")
    return float(cut_money_syntex)

def percent_to_float(p):
    # TODO
    cut_percent_syntex = p.replace("%" , "")
    convert = float(cut_percent_syntex)/100
    return convert

main()
