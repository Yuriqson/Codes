import random,string
def rgb_generator(n):
    i=0
    l0=[]
    while i!=n:
        l0.append((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        print(l0)
        i+=1
rgb_generator(int(input('How many RGB colours?')))
def hexa_generator(m):
    j=0
    l1=[]
    while j!=m:
        r=lambda:random.randint(0,255)
        l1.append(('#%02X%02X%02X' % (r(), r(), r())))
        print(l1)
        j+=1
hexa_generator(int(input('How many Hexa RGB colours?')))


