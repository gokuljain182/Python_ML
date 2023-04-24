a = int(input('Enter the coefficient of x^2:'))
b = int(input('Enter the coefficient of x^1'))
c = int(input('Enter the coefficient of x^0'))
d = (b**2)-(4*a*c)
k = d**0.5
x1 = (-b+d)/(2*a)
x2 = (-b-d)/(2*a)
print('The roots are',x1,x2)