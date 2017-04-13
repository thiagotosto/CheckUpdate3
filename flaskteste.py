from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', teste='Bem vindo!!!')

@app.route('/<teste>')
def show_template(teste=None):
    return render_template('index.html', teste=teste)

#@app.route('/user/', methods=['POST'])
#def user_section():
#    if request.form['Email']:
#        return render_template('index.html', teste=request.form['Email'])
#    else:
#        return redirect(url_for('/'))
