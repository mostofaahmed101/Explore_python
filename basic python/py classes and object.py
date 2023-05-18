

class first_C:
    Depertment = "C.M.T"
    def __init__(self, nam, rol, blood):
        self.Name = nam
        self.Roll = rol
        self.Blood_Group = blood
    
    def __str__(self):
        return f"is {self.Name}. and his Roll is {self.Roll}, or Blood Group is {self.Blood_Group}\n"
    
    def F_detail(self):
        print("Hello " + self.Name)
    
class second_C(first_C):
    def __init__(self, nam, rol, blood):
        super().__init__(nam, rol, blood)
    pass


A = first_C("Mostofa Ahmed", 97, "B+")
B = second_C("MD. Fahim", 700, "AB+")
first_C.Depertment = "C.S.T"

A.F_detail()
B.F_detail()
print(A, B)
print(B.Depertment, B.Name, B.Roll, B.Blood_Group)


                   # __iter__ & __next__ with loop and class

class third_c:
    def __iter__(self):
        self.L_num = 1
        return self
    
    def __next__(self):
        if self.L_num <10:
            while self.L_num <10:
                self.L_num +=1
                return self.L_num
        else:
            raise StopIteration

it = third_c()

for ppp in it:
    print(ppp)
