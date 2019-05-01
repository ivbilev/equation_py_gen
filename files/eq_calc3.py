from flask import Flask, render_template, request

strTable = \
"<html>"\
"<form action = \"/rs\" method = \"POST\">"\
"<table>"\
    "<tr>"\
    "</tr>"\


#print (strTable)
res = []
numbers = []
for num in range(5):
    symb = str(num)+"*"+str(num)+"="
    strRW = "<tr><td>" + str(symb) + "</td><td>" + "<input type='text'"+" name="+str(num)+" value="+str(num)+" />" + "</td></tr>"
    strTable = strTable + strRW
    res.append(num*num)
    numbers.append(num)

strTable = strTable + "<input type='submit' value='Submit' /></table></html>"
hs = open("templates/eq.html", 'w')
hs.write(strTable)
hs.close()


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('eq.html')


@app.route('/rs', methods=['POST'])
def hello():
    answer = [request.form['0'], request.form['1'], request.form['2'], request.form['3'], request.form['4']]
    strTable2 = "<html><form action = \"/eq\" method=\"post\"><table><tr></tr>"
    for i in range(len(answer)):
        if int(answer[i]) != int(res[i]):
            answer[i] = "wrong"
    for y in range(len(answer)):
        symb = "<tr><td>" + str(numbers[y]) + "*" + str(numbers[y]) + "=" + str(answer[y]) + "</td><td>"
        strTable2 = strTable2 + symb
    strTable2 = strTable2 + "</table><input type='submit' value='Back' /></html>"

    rs = open("templates/rs.html", 'w')
    rs.write(strTable2)
    rs.close()

    return render_template('rs.html')

@app.route('/eq')
def back():
    return render_template('eq.html')


if __name__ == '__main__':
    app.run(debug=True)
