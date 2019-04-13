import pprint
import itertools
import math
import pandas

dict1 = {}
a = ['1', '2','3',]
b = ['a','b','c','d','e','f',"g","h","i","j"]

rows = math.ceil(len(b) / len(a)) # round up to get the number of rows
#print(rows)

# split b list
def split_seq(iterable):
    it = iter(iterable)

    item = list(itertools.islice(it, rows))

    while item:
        #print(item)
        yield item
        item = list(itertools.islice(it, rows))


#pprint.pprint(list(split_seq(b)))
c = (list(split_seq(b))) #creates list of lists

last_len = len(c[len(c) - 1])
#print(last_len)
before_lats_len = len(c[len(c) - 2])
#print(before_lats_len)

# extenidng the las list ot match the previous because pandas fails if the lists have different length
if before_lats_len > last_len:
    dif = before_lats_len - last_len

    for i in range(dif):
        c[(len(c) - 1)].extend([""])

#print(c)

a.extend(['4','5'])
print(a)
#adding empty column

first_elem_len = len(c[0])
list_len = len(c)
print(list_len)
new_list = []
ll2 = []
for ll in range(first_elem_len):
    ll2.extend([""])

for l in range(list_len):
        new_list.append(c[l])
        print(l)
        if l != list_len -1:
            new_list.append(ll2)

print(new_list)

dict1 = dict(zip(a,new_list))

print(dict1)

# CSV creation
df = pandas.DataFrame(dict1)
print(df)
df.to_csv('example.csv', index= False, header=0)