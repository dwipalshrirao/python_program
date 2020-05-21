n=int(input('give a no.'))
sum_of_squares=(n*(n+1)*(2*n+1))/6
print(int(sum_of_squares))

#======================================
n=int(input('give a no.'))
x=0
for i in range(n+1):
    x=x+ i**2
print(x)
#================================================
n=int(input('give a no.'))
x=0
y=0
while x<=n:
    y=y+x**2
    x += 1
print(y)

