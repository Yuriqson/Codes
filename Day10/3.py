l=['#']
for i in l:
    print(''.join(l))
    l.append('#')
    if len(l)==8:
        break