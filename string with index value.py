a=input('enter string')
#printing string index in reverse order
for i in reversed(range(0,len(a))):
    print('string value {} is: '.format(a[i]),i-len(a))