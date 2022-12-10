age=int(22)
height=float(1.75)
cn=complex(-3+1j)
#triangle area

b=float(input('What is the base?'))
h=float(input('What is the height?'))
print('The area of the triangle is:', 0.5*b*h)

#triangle perimeter
side_a=float(input('What is the length of side a?'))
side_b=float(input('What is the length of side b?'))
side_c=float(input('What is the length of side c?'))
print('its perimeter is:', side_a+side_b+side_c)

#rectangle
l=float(input('length'))
w=float(input('width'))
print('area:',l*w,'perimeter:',2*(l+w))

#circle
r=float(input('radius'))
print('area:',3.14*r**2,'circumference:',2*3.14*r)

#slope and interceptions
y0=-2
x0=0
y1=0
x1=1
frist_slope=(y1-y0)/(x1-x0)
print('slope:',frist_slope)
print('x-intercept:',0/2+1)
print('y-intercept:',2*0-2)

import math
print('the first slope was:',frist_slope,'the other slope is:',(10-2)/(6-2))
print('Euclidean distance:',math.sqrt((6-2)**2+(10-2)**2))

x=-3
print('y is:',x**2+6*x+9, 'while x is:',x)

print(len('python')<len('dragon'))

print('on'is'python'and'dragon')

print('jargon'in'I hope this course is not full of jargon.')

print('on'not in'python'and'dragon')

length=len('python')
length_float=float(length)
length_string=str(length_float)
print(type(length_string))

number=int(input('type a number to check if it is even'))
reminder=number%2
print(reminder is 0)

floor=(7//3)
print(floor is int(2.7))

print(type('10') is type(10))

print(int(9.8)is 10)

hour=float(input('How many hours?'))
rph=float(input('How many per hour?'))
print('weekly earning',hour*rph)

years=int(input('How many years?'))
print('You have lived for',years/(3.171*10**(-8)),'seconds')

import tabulate
table=tabulate.tabulate([1,1,1,1,1],[2,1,2,4,8],[3,1,3,9,27],[4,1,4,16,64],[5,1,5,25,125])
print(table)