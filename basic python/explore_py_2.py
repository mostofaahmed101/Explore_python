X = "what"
Y ="the"
Z = "Hello!"

def function1():
    global X
    X = "hey"
    print(X, Z)

function1()
print(X,Y,Z)

com = complex(2)
print(com)

multy_string = """hg  wrehfuiwerhfwe whgweui uewwhrfb y were
wehfruywef yewuif uyweuifr uiuyeiuf
ywerryf e
eiru8eu   i8uerue
e ewi90ri e0"""
print(multy_string)
print("hg" in multy_string)
print("hg" not in multy_string) # is / not is

N1 = 55
N2 = 44
N3 = 33
text = "you earned in bangla: {}, in english: {}, in math {}"
print(text.format(N1,N2,N3))

print("hello i am the \"boss\" ,\b \n \\this for new resurch") 
print(10//6)
print(not(3==5))



list_i=["hdfjahd", "mamaka", "rejoijer", "tejkge", "hnjhfdja", "aghgdh"]
new_list=[x for x in list_i if "a" in x] # loop and if in one line
print(new_list)


                    # import module
def import_test():
    print("Hello this is import :) ")


