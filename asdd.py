# try:
#     a=input('strig: ')
#     b=int(input('slice'))
#     c=int(input('slice2'))
#     d=int(input('gyp'))
# except:
#     d=1
#
# print(a[b:c:d])
from time import sleep

# pos=0
# position=[]
# a='i am in hyderabad am'
# n=len('am')
# while True:
#     pos=a.find('am',pos+1,n)
#     if pos==-1:
#         break
#
#     print(pos)
#     if pos==False:
#         print('not found')


# x=input('')
# if a.find(x)!=-1:
#     for i in range(0,len(a)):
#         if a[i]==x:
#             count+=1
#             position.append(i)
#     print(count, position)
#
# else:
#     print('file not find')

#
# def fuction(viewfun):
#     def inner(x,y):
#         if y==0:
#             print('cant divisible')
#             sleep(2)
#
#         else:
#             print('sewgr')
#             return viewfun(x,y), inner(x,y-1)
#     return inner
#
# @fuction
# def sum1(a,b):
#     return a+b
#
#
# print(sum1(10,6))

# list=['durga','narayan','nagoor','mahesh']
#
# x=lambda a:print('{} is available'.format(a))if a in list else print('no')
# x('narayan')

# t=[2,3,4,5,6]
# x=list(filter(lambda a: a in t,t))
# # b=list(map(t,filter(lambda n: n % 2, range(6))))
# print(x)
# symbols = '$¢£¥€¤'
# beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
# beyond_ascii


# list1=['a','b','c']

# for i in list:
#     if 'mahesh' in i:
#         print(i,'y')
#         break
#     else:
#         continue

# import re
# a=['<th><strong>S. No.</strong></th>',
#     '<th><strong>Name of State / UT</strong></th>', "<th><strong>Total Confirmed cases (Including 77 foreign Nationals) </strong></th>", '<th><strong>Cured/Discharged/<br/>Migrated</strong></th>', '<th><strong>Death</strong></th>']
# print(a[0])
# x=re.findall(r"\b<th>",a[0])
#
#
# print(x)



