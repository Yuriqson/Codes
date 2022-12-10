ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print('min: ',ages[0],'max: ',ages[-1])
ages.insert(0,ages[0])
ages.insert(-1,ages[-1])
print(ages)
print(ages[6]/2)
average=sum(ages)/12
print(average)
print(ages[-1]-ages[0])

print(abs(ages[0]-average),abs(ages[-1]-average))
