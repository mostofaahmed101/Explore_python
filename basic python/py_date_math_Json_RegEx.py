import datetime
import math
import json
import re



                  # Date-Time

DT = datetime.datetime.now()
print("Present Time:", DT.strftime("%c"), DT.strftime("%f"), DT.strftime("%p"), DT.strftime("%j"), DT.strftime("%w"))

DT2 = datetime.datetime(2004, 8, 31)
print("Mostofa birth:", DT2.strftime("%c"))


                  # MATH

MTH_N1 = 50
MTH_N2 = 99
MTH_N3 = 43
MTH_N4 = -66.89
print("MIN is:", min(MTH_N1, MTH_N2, MTH_N3, MTH_N4))
print("MAX is:", max(MTH_N1, MTH_N2, MTH_N3, MTH_N4))
print("Get Negative to Positive:", abs(MTH_N4))
print("5 power 3 is:", pow(5, 3))   # ** also for power-math
print(math.ceil(3.02))
print(math.floor(3.97))
print(math.sqrt(25))    # sqrt =  square root
print("the Number of pi is:", math.pi)


                    # json to py & py to json

j_to_p = '{ "name":"John", "age":30, "city":"New York"}'
j_to_p = json.loads(j_to_p)
print(type(j_to_p))
print(j_to_p["name"], j_to_p["city"])

p_to_j = {"name":"John", "age":30, "city":"New York"}
p_to_j = json.dumps(p_to_j)
print(type(p_to_j))



                # Regular Expression

RegEx1 = "Hello, this is the first practice of regular expression, i just try to findout this module, also make a date: 31-Aug-2004 for this module test, thats not a easy module."
RegEx2 = re.search("module", RegEx1)
print(RegEx2.span())
print(RegEx2.group())
print(RegEx2.string)

print(re.findall("m.*le", RegEx1))
print(re.search("^Hello", RegEx1))
print(re.findall(r"\bpr", RegEx1))
print(re.findall(r"\d+-[a-zA-Z]+-\d{4}", RegEx1))

print(re.split(", ", RegEx1))
print(re.sub(r"module.\Z", "Leason.", RegEx1))

