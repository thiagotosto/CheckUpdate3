from flask import Flask, render_template, request, session, redirect, url_for
from form2db import *

app = Flask(__name__)


app.secret_key = 'likujnyhtbgrvf67543'

globalSession = dict()
globalSession['consulta'] = []
globalValues = dict()
globalValues['Header'] = ['Nome','Baia','Categoria','Resp','Serial','Fabricante','Modelo','Localizacao','Rack','Patrimonio','Hostname','IP','Em uso?','SAID','Contrato(FL)','Start Date','End Date','Legado']

@app.route('/')
def index():
    #print '------------------------'
    #print 'passei no index!!!!'
    #print '------------------------'
    print globalSession
    return render_template('index.html', globalSession=globalSession)

'''
@app.route('/campo/<campo>', methods=['GET', 'POST'])
def campo(campo):

    #print 'Entrei no campo --------'
    #print
    #print 'Campo: ', campo
    session['current'] = campo
    #print 'Current: ', session['current']
    #print "Consulta: ", session['consulta']
    #print

    session['consulta'] = session['consulta']

    return render_template('index.html', session=session)
'''

@app.route('/consulta/', methods=['POST'])
def consulta():
    #print 'Entrei no consulta -----'
    #print
    #print 'Consulta antes: ', session['consulta']
    #print 'Teste antes: ', globalSession['consulta']

    globalSession['consulta'].append({'campo': request.form['campo'], 'valor': request.form['valor']})
    #session['consulta'].append({'campo': request.form['campo'], 'valor': request.form['valor']})
    #print
    #print 'Consulta depois: ', session['consulta']
    print "globalSession['consulta']: ", globalSession['consulta']

    return render_template('index.html', globalSession=globalSession)

@app.route('/consulta_result/')
def consulta_result():

    bind = binder(globalSession['consulta'])
    globalSession['consulta_result'] = form2db_consulta(bind)

    #print '\n\n\nTeste consulta_result: ', globalSession['consulta_result'][0].serial, '\n\n\n'

    return render_template('consulta_result.html', globalSession=globalSession, globalValues=globalValues)

@app.route('/reset')
def reset_session():

    for i in range(len(globalSession['consulta'])):
        globalSession['consulta'].pop(0)

    if 'consulta_result' in globalSession.keys():
        for i in range(len(globalSession['consulta_result'])):
            globalSession['consulta_result'].pop(0)


    return redirect(url_for('index'))
