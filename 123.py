from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def ind():
    return render_template("base.html")


#@app.route('/training/<prof>')
#def prof(prof):
#    if prof.find("инженер") != -1 or prof.find("строитель") != -1:
#        it = "Инженерные тренажеры"
#    elif prof.find("ученый") != -1:
#        it = "Научные симуляторы"
#    else:
#        it = "Неправильный ввод специальности!"
#    return render_template("base.html", x=prof, y=it)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
