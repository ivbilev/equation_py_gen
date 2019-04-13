import random
import math
import itertools
import pandas

base = 13
start = 0
base_set = list(range(start,base))
final_set = []
columns = ['1', '2', '3','4','5']
final_dict = dict()
dict1 = []


def division():
    for i in base_set:
        for y in range(len(base_set)):
            if y != 0 and y < i and (i % (base_set[y])) == 0: #excluding divisin by zero and reminder
                final_set.append(str(i)+'/'+str(base_set[y])+'=')


def multiplication():
    for i in base_set:
        for y in range(len(base_set)):
            final_set.append(str(i) + '*' + str(base_set[y]) + '=')


division()
multiplication()

random.shuffle(final_set)

# split list
def split_seq(iterable):
    rows = math.ceil(len(iterable) / len(columns))  # round up to get the number of rows
    it = iter(iterable)
    item = list(itertools.islice(it, rows))
    while item:
        #print(item)
        yield item
        item = list(itertools.islice(it, rows))


#random.shuffle(final_set)
#print(final_set)
#pprint.pprint(list(split_seq(b)))
list_of_lists = (list(split_seq(final_set))) #creates list of lists from final set
#print(list_of_lists)

#makes the last list length even with the others
def even_lists():
    last_len = len(list_of_lists[len(list_of_lists) - 1])
    #print(last_len)
    before_lats_len = len(list_of_lists[len(list_of_lists) - 2])
    # print(before_lats_len)
    # extenidng the las list ot match the previous because pandas fails if the lists have different length
    if before_lats_len > last_len:
        dif = before_lats_len - last_len
        for i in range(dif):
            list_of_lists[(len(list_of_lists) - 1)].extend([""]) # adding empty strings because pandas fails if the length is not even


even_lists()

#extend the columns so i can add space in between
columns.extend(['6','7','8','9'])

def empty_columns():
    # adding empty column
    first_elem_len = len(list_of_lists[0])
    list_len = len(list_of_lists)
    #print(list_len)
    new_list = []
    ll2 = [] #temp list
    for ll in range(first_elem_len):
        ll2.extend([""])
    for l in range(list_len):
        new_list.append(list_of_lists[l])
        #print(l)
        if l != list_len - 1:
            new_list.append(ll2)
            #print(new_list)
    global dict1
    dict1 = dict(zip(columns, new_list))
    print(dict1)


empty_columns()
# CSV creation
df = pandas.DataFrame(dict1)
print(df)
df.to_csv('example.csv', index= False, header=0)
