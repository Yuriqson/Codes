#1
print('Thirty '+'Days '+'Of '+'Python')
#2
print('Coding '+'For '+'All')
#3
company="Coding For All"
#4
print(company)
#5
print(len(company))
#6
print(company.upper())
#7
print(company.lower())
#8
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9
print(company[1:])
#10
print(company.find('Coding'))
#11
print(company.replace('Coding','Python'))
#12
print(company.replace('Coding For All','Python for Everyone'))
#13
print(company.split(' '))
#14
s0="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(s0.split(','))
#15
print(company[0])
#16
print(company[-1])
#17
print(company[10])
#18
c0='Python For Everyone'
print(c0[0],c0[7],c0[11])
#19
print(company[0],company[7],company[11])
#20
print(company.index('C'))
#21
print(company.index('F'))
#22
print(company.rfind('l'))
#23
s1='You cannot end a sentence with because because because is a conjunction'
print(s1.find('because'))
#24
print(s1.rindex('because'))
#25
print(s1.replace('because',''))
#26
print(s1.find('because'))
#27
print(company.startswith('Coding'))
#28
print(company.startswith('coding'))
#29
print(company.endswith('coding'))
#30
s2='   Coding For All      '
print(s2[3:-6])
#31
s3='30DaysOfPython'
s4='thirty_days_of_python'
print(s3.isidentifier(),s4.isidentifier())
#32
list=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(list))
#33
print('I am enjoying this challenge.\nI just wonder what is next.')
#34
print('Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')
#35
radius=10
area=3.14*radius**2
print('The area of a circle with radius {} is {} meters square.'.format(radius,area))
#36
a=8
b=6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
