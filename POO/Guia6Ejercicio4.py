import math

a = 0
b = 0
c = 0

while a <= 0:
    a = int(input("Ingrese un valor para a: "))
    if a <= 0:
        print("Error, valores deben ser mayor a 0")

while b <= 0:
    b = int(input("Ingrese un valor para b: "))
    if b <= 0:
        print("Error, valores deben ser mayor a 0")

while c <= 0:
    c = int(input("Ingrese un valor para c: "))
    if c <= 0:
        print("Error, valores deben ser mayor a 0")

#print(a,b,c)

s = (a+b+c)/2
x = s*(s-a)*(s-b)*(s-c)
area = math.sqrt(x)

print (area)
        
