from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', teste='Bem vindo!!!')

@app.route('/<teste>')
def show_template(teste=None):
    return render_template('index.html', teste=teste)

