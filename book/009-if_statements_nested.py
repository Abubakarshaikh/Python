# if statements nested
if 14 > 12:
    print("14 is greater than 12")
    if 8 > 6:
        print("8 is greater than 6")
        if 6 < 4:
            print("6 is less than 4")
        else:
            print("6 is not less than 4")
            if 4 > 2:
                print("4 is greater than 2")
else:
    print("14 is not greater than 12")
