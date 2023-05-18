                                                                  # raise  for stop loop

loop1 = ("hello", "kello", "mello", "dello", "sello")
loop2 = [1,2,3]
for p in loop1:
    print(p)
             # Nested looop
for A in loop1:
    for B in loop2:
        print(A,B)


for Rloop in range(1, 20 ,2):
    print(Rloop)
else:
    print("Ohh.. finished :) ")

"""
ran_1 = int(input("type start range: "))
ran_2 = int(input("type end range: "))
total = 0

for R in range(ran_1 , ran_2+1):
    total += R
    print(R)

print(f"total sum is {total}")

num = 0

for x in range(0, 10):
    num +=1
    print("kya haal hay bro",num)



                             # while loop


N = 5

while(N<=100):
    print(N)
    N += 5
"""