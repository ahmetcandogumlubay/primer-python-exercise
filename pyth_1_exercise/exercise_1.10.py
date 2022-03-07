from math import pi, sqrt, exp

s = float(input("Enter the s: "))
x = float(input("Enter the x: "))
m = float(input("Enter the m: "))

funct = 1/((sqrt(2*pi))*s)*exp(-0.5*((x-m)/s)**2)
print(funct)


# from math import pi, exp, sqrt

# m = 0
# s = 2.0
# x = 1.0

# f = 1 / (sqrt(2 * pi) * s) * exp(-0.5 * ((x - m) / s) ** 2)
# print (f)

