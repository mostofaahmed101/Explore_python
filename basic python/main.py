import explore_py_2 as Imp

name = "kuddus ali"
print(name)
print(name[0:2])
print(5//2)
print(5**3)
print(len(name))
print(name.title()) # upper / lower /strip for remove first last space
print(name.replace("ali", "islam"))   
print(name.split())


number = 83
number +=2           
print(number)

print(f"the person name is {name}. and his number is {number}")
format_test = "Also: the person name is {}. and his number is {}"
print(format_test.format(name, number))
format_test2 = "val {amar} what the {matha}"
print(format_test2.format(amar = "1111111", matha = "0000000"))



namee = "aluuu baba"
print("hello"+" "+ namee)


"""
NUM = int(input("type number"))
if NUM %2 ==0:
    print("even")
else:
    print("odd")
"""
Num1 = 20
Num2 = 20
            # if in short hand
print(1) if Num1 > Num2 else print("=") if Num1 == Num2 else print(2)



def first_function(f_name="None", l_name=""):
    print("MD.", f_name, l_name)

first_function("abul", "islam")
first_function("alhaj", "ali")
first_function()
# first_function(input("type your name: "), input("Your last name: "))


                # Return function
def S_function(NAMM):
    return "Good" +" "+ NAMM
    
print("code is:", S_function("Morning"))
print("code is:", S_function("Evening"))
print("code is:", S_function("Night"))



                # Lambda function
lambda_1 = lambda x,y,z : x + y + z
print(lambda_1(1,2,3))

def lambda_2(nnn):
    return lambda x: nnn / x
print(lambda_2(10)(2))



                    # import   

Imp.import_test()
print(Imp.list_i[1])

from explore_py_2 import new_list

print(new_list, "from import")

print(dir(Imp)) 



                    # try / except / else / finally

txt_tryy = "hello world ;)"

try:
    print(txt_tryy)
except:
    print("Not found")
else:
    print("Ohhh... the try Work!!!!!")
finally:
    print("try concept End finally")




