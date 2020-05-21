from operator import itemgetter
#============================================================
#adding value of same keys from different dictionary
#================================================================

# Initialising list of dictionary
# ini_dict = [{'a': 5, 'b': 10, 'c': 90},
#             {'a': 45, 'b': 78},
#             {'a': 90, 'c': 10}]
#
# # printing initial dictionary
# print("initial dictionary", str(ini_dict))
#
# # sum the values with same keys
# fresul = {}
# for i in ini_dict:
#     for d in i.keys():
#         fresul[d] = fresul.get(d, 0) + i[d]

#print("resultant dictionary : ", str(fresul))

ini_dict = [{'a': 5, 'b': 10, 'c': 90},
            {'a': 45, 'b': 78},
            {'a': 90, 'c': 10}]

# printing initial dictionary
print("initial dictionary", str(ini_dict))

# sum the values with same keys
fresul = {}
for i in ini_dict:
    for d in i.keys():
        try:

            fresul[d]=fresul[d]+i[d]

        except:
            fresul[d]=i[d]

# fresul[d] = fresul.get(d, 0) + i[d]
print("resultant dictionary : ", str(fresul))