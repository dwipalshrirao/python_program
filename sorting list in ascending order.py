fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
#sort list in ascending order according to its size
# print(sorted(fruits,key=len,reverse=True))
# if len(i)>len()
for i in range(0,len(fruits)):
    if len(fruits[i])<len(fruits[i-1]):
        c=fruits[i]
        fruits[i]=fruits[i-1]
        fruits[i-1]=c
print(fruits)