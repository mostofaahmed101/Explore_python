num = float(input("type your avarage Number : "))

if num>100 :
    print("Wrong type")
elif num>=80:
    print("A+")
else:
    if num>=70:
        print("A")
    else:
        if num>=60:
            print("A-")
        else:
            if num>=50:
                print("B")
            else:
                if num>=40:
                    print("C")
                else:
                    if num>=33:
                        print("D")
                    else:
                        print("FAIL")