from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def ind():
    return render_template("base.html", title='Главная')


@app.route('/register')
def register():
    return render_template("register.html", title='Регистрация')


@app.route('/login')
def login():
    return render_template("login.html", title='Авторизация')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
