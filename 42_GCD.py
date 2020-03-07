import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print (f"GCD for {a} and {b} is: ", end ="")
print (math.gcd(a, b))


while b>0:
    if a < b:
        a, b = b, a
    if b == 0:
            break
    else:
        a = a % b
print(a)