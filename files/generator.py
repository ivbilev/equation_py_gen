import random
import math
import itertools
import pandas
from flask import Flask, render_template, request


#final_set = []
columns = ['1', '2', '3', '4', '5']
columns_ext = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
final_dict = dict()
dict1 = []
results = []
answer = []
random_results = []
compare_set = []

app = Flask(__name__)


def zero():
    global input_id
    global final_set
    global list_of_lists
    global final_set
    list_of_lists = []
    final_set = []
    final_set = []
    input_id = []


def zero2():
    global answer
    global result_dict
    answer = []
    result_dict = dict()


def division(baseset):
    for i in baseset:
        for y in range(len(baseset)):
            if y != 0 and y < i and (i % (baseset[y])) == 0:  # excluding division by zero and reminder
                final_set.append(str(i) + ':' + str(baseset[y]) + '=')
                compare_set.append(str(i) + ':' + str(baseset[y]) + '=')
                results.append(int(i / baseset[y]))


def multiplication(baseset):
    for i in baseset:
        for y in range(len(baseset)):
            final_set.append(str(i) + 'x' + str(baseset[y]) + '=')
            compare_set.append(str(i) + 'x' + str(baseset[y]) + '=')
            results.append(int(i * baseset[y]))



# split list
def split_seq(iterable):
    rows = math.ceil(len(iterable) / len(columns))  # round up to get the number of rows
    it = iter(iterable)
    item = list(itertools.islice(it, rows))
    while item:
        yield item
        item = list(itertools.islice(it, rows))


 # makes the last list length even with the others
def even_lists(lists):
    last_len = len(lists[len(lists) - 1])
    before_lats_len = len(lists[len(lists) - 2])
    # extending the las list ot match the previous because pandas fails if the lists have different length
    if before_lats_len > last_len:
        dif = before_lats_len - last_len
        for i in range(dif):
            lists[(len(lists) - 1)].extend(
                [""])  # adding empty strings because pandas fails if the length is not even


def empty_columns(lists2):
    # adding empty column
    global dict1
    dict1 = {}
    first_elem_len = len(lists2[0])
    list_len = len(lists2)
    new_list = []
    ll2 = []  # temp list
    for ll in range(first_elem_len):
        ll2.extend([""])
    for l in range(list_len):
        new_list.append(lists2[l])
        if l != list_len - 1:
            new_list.append(ll2)
    dict1 = dict(zip(columns_ext, new_list))


@app.route('/', methods=['GET', 'POST'])
def start():

    return render_template('input.html')


@app.route('/eq',  methods=['GET', 'POST'])
def equations():

    if request.method == 'POST':
        zero()
        b = request.form['base']
        s = request.form['start']
        base = int(b)+1
        start = int(s)
        base_set = list(range(start, base))
        division(base_set)
        multiplication(base_set)
        #print(final_set)
        random.shuffle(final_set)

        # add input after each equation and create unique input name
        final_set2 = []
        for in_id in range(len(final_set)):
            input_id.append(in_id)
            final_set2.append(str(final_set[in_id]) + "<input type='text'" + " name=" + str(in_id) + ">")
        list_of_lists = (list(split_seq(final_set2)))  # creates list of lists from final set
        even_lists(list_of_lists)

        # extend the columns so i can add space in between
        empty_columns(list_of_lists)
        df = pandas.DataFrame(dict1)
        tables = ((df.to_html()).replace('&lt;', '<')).replace('&gt;',
                                                               ' autocomplete="off">')  # use pandas method to auto generate html and replace html simbols for tags

        tables = '<style>table {  border-collapse: collapse;  width: 100%;}th {  text-align: center;  padding: 8px;}td {  text-align: left;  padding: 8px;}tr:nth-child(even){background-color: #FFD5D5}th {  background-color: #0000FF;  color: white;}</style>' + tables
        zero2()
        return render_template('simple.html', tables=[tables])


@app.route('/result', methods=['GET', 'POST'])
def html_table():
    if request.method == 'POST':
        result_dict = dict(zip(compare_set, results))  # has the equation with the answers to compare with final_set
        for a in input_id:
            answer.append(request.form[str(a)])
        temp_list = []
        for eq in final_set:
            for key in result_dict.keys():
                if eq == key:
                    temp_list.append(result_dict[key])
        counter = len(temp_list)
        x = 0
        while x < counter:
            if str(temp_list[x]) != str(answer[x]):
                answer[x] = 'wrong'
            x += 1
        final_set3 = []
        for in_id2 in range(len(final_set)):
            final_set3.append(str(final_set[in_id2]) + answer[in_id2])
        list_of_lists2 = (list(split_seq(final_set3)))  # creates list of lists from final set
        even_lists(list_of_lists2)
        empty_columns(list_of_lists2)
        df2 = pandas.DataFrame(dict1)
        tables2 = ((df2.to_html()).replace('&lt;', '<')).replace('&gt;', '>')

        # use pandas method to auto generate html and replace html symbols for tags
        return render_template('simple2.html', tables=[tables2])


if __name__ == '__main__':
    app.run(debug=True, port=4000)
