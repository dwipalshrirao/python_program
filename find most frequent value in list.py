lst=[4,5,2,8,7,4,5,0,9,4,0,4]

set=set(lst)
list1=list(set)
dict={}
for i in list1:
    dict[i]=lst.count(i)
print(dict)
print(max(dict,key=dict.get))


