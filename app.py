from flask import Flask, render_template, request, session, redirect, url_for
from form2db import *

app = Flask(__name__)


app.secret_key = 'likujnyhtbgrvf67543'

globalSession = dict()
globalSession['consulta'] = []      #inicializando variavel global de Consulta
globalSession['update'] = []        #inicializando variavel global de Update
globalValues = dict()
globalValues['Header'] = ['Nome','Baia','Categoria','Resp','Serial','Fabricante','Modelo','Localizacao','Rack','Patrimonio','Hostname','IP','Em uso?','SAID','Contrato(FL)','Start Date','End Date','Legado']

@app.route('/')
def index():
    return render_template('index.html', globalSession=globalSession)

#renderizando clausulas da consulta
@app.route('/consulta/', methods=['POST'])
def consulta():
    globalSession['consulta'].append({'campo': request.form['campo'], 'valor': request.form['valor']})
    print "globalSession['consulta']: ", globalSession['consulta']

    return render_template('index.html', globalSession=globalSession)

#renderizando clausulas do update
@app.route('/consulta_result/update', methods=['POST'])
def update():
    globalSession['update'].append({'campo': request.form['campo'], 'valor': request.form['valor']})

    return render_template('consulta_result.html', globalSession=globalSession, globalValues=globalValues)


@app.route('/consulta_result/')
def consulta_result():

    bind = binder(globalSession['consulta'])
    globalSession['consulta_result'] = form2db_consulta(bind)

    return render_template('consulta_result.html', globalSession=globalSession, globalValues=globalValues)

@app.route('/reset')
def reset_session():

    for i in range(len(globalSession['consulta'])):
        globalSession['consulta'].pop(0)

    if 'consulta_result' in globalSession.keys():
        for i in range(len(globalSession['consulta_result'])):
            globalSession['consulta_result'].pop(0)


    return redirect(url_for('index'))
