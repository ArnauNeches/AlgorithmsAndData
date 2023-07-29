#Create a data class for a Fraction with all of its features

def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n
    return n

class Fraction:

    def __init__(self,top,bottom):
        #Constructor
        self.num = top
        self.den = bottom

    def __str__ (self):
        #ToString
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        #Add function
        new_num = self.num*other.den + self.den*other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)
    
    def __sub__(self, other):
        #Substract function
        new_num = self.num*other.den - self.den*other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)       
    
    def __mul__(self, other):
        #Multiply function
        new_num = self.num * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __truediv__(self, other):
        #Division function
        new_num = self.num * other.den
        new_den = self.den * other.num
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)        

    def __eq__(self, other):
        #Equality
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num
    
    def __lt__(self, other):
        #Less (<) operator
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num < second_num  

    def __gt__(self, other):
        #Greater (>) operator
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num > second_num   

f1 = Fraction(3,5)
f2 = Fraction(1,2)
print(f1)
print(f2)
print(f1+f2)
print(f1-f2)
print(f1*f2)
print(f1/f2)
print(f1==f2)
print(f1<f2)
print(f1>f2)     