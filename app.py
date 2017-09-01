#!/usr/bin/env python
# -*- coding: utf-8 -*

from flask import Flask, render_template, request, session, redirect, url_for
from form2db import *
from inconsistence_check import *
from db2flask import *
from random import *
from session import *
import thread


#instanciando a aplicação
app = Flask(__name__)


app.secret_key = 'likujnyhtbgrvf67543'

#session = dict()
globalValues = dict()
globalValues['Header'] = ['Nome','Baia','Categoria','Resp','Serial','Fabricante','Modelo','Localizacao','Rack', 'Posicao','Patrimonio','Hostname','IP','Em uso?','SAID','Contrato','Start Date','End Date','Legado']


@app.route('/')
def index():


    session['consulta'] = []      #inicializando variavel global de Consulta
    session['update'] = []        #inicializando variavel global de Update
    session['insert'] = []        #inicializando variavel global de Insert
    session['bayface_rack'] = []  #inicializando variavel global de Bayface


    return render_template('index.html', session=session)

#CONSULTA ---------------------------------------------------------------------------------------------------

#renderizando clausulas da consulta
@app.route('/consulta/', methods=['POST'])
def consulta():

    temp = session['consulta']

    temp.append({'campo': request.form['campo'], 'valor': request.form['valor']})

    session['consulta'] = temp

    return render_template('index.html', session=session)

#renderiza o resultado da consulta
@app.route('/consulta_result/')
def consulta_result():

    bind = binder(session['consulta'], 'c')

    session['consulta_result'] = dbAsDict(form2db_consulta(bind))

    asDict = session['consulta_result']
    print "\n\nAsDict: ", asDict, "\n\n"

    return render_template('consulta_result.html', session=session, globalValues=globalValues, asDict=asDict)

#UPDATE -----------------------------------------------------------------------------------------------------

#renderizando clausulas do update
@app.route('/consulta_result/update', methods=['POST'])
def update():

    #zerando lixo de update anterior
    session['update'] = []

    #pegando serial do elemento atual
    elemento_atual = request.form['serial-id-update']

    #populando update
    for header in globalValues['Header']:
        if request.form[header] != '':
            session['update'].append({'campo': header, 'valor': request.form[header]})

    #instanciando inconsistente check
    ict = Inconsistence_check()

    #checando inconsistencias de formatação
    session['update'] = ict.orquestrator(session['update'])

    index = binder(session['update'], 'u')
    form2db_update(elemento_atual, session['update'], index)

    return redirect(url_for('consulta_result'))

#INSERT -----------------------------------------------------------------------------------------------------

@app.route('/insert/')
def insert():
    return render_template('insert.html', globalValues=globalValues)

@app.route('/insert_result/', methods=['POST'])
def insert_result():

    #zerando lixo de insert anterior
    session['insert'] = []

    #populando insert
    for header in globalValues['Header']:
        if request.form[header] != '':
            session['insert'].append({'campo': header, 'valor': request.form[header]})

    #instanciando inconsistente check
    ict = Inconsistence_check()

    #checando inconsistencias de formatação
    session['insert'] = ict.orquestrator(session['insert'])

    #fazendo bind
    bind = binder(session['insert'], 'u')

    try:
        #fazendo insert
        form2db_insert(bind, session['insert'])
    except Exception as e:
        if e[0].find('Integrity'):
            error = 'Serial já existente!'
        return render_template('insert.html', globalValues=globalValues, error=error.decode('utf-8'))

    return render_template('insert.html', globalValues=globalValues)

#BAYFACE ----------------------------------------------------------------------------------------------------

@app.route('/bayface/', methods=['GET','POST'])
def bayface():

    #inicializando valor default de rack
    rack = 22

    #carregando numero do rack escolhido
    if (request.method == 'POST'):
        rack = request.form['rack_input']

    bind = binder([{'campo': 'Rack', 'valor': rack}], 'c')
    session['bayface_rack'] = dbAsDict(form2db_consulta(bind))

    #transformando lista de pbjetos em lista de dicionarios correspondentes
    asDict = session['bayface_rack']

    #parseando o atributo posicao
    for server in asDict:
        parse_posicao(server)

    return render_template('bayface.html', session=session, rack=rack, asDict=asDict)

#REMOVE -----------------------------------------------------------------------------------------------------

@app.route('/remove/',  methods=['POST'])
def remove():

    #pegando serial do elemento atual
    elemento_atual = request.form['serial-id-remove']

    form2db_remove(elemento_atual)

    #asDict = session['consulta_result']

    return redirect(url_for('consulta_result'))

#RESET ------------------------------------------------------------------------------------------------------

@app.route('/reset')
def reset_session():

    session.pop('consulta', None)

    session.pop('update', None)

    if 'consulta_result' in session.keys():
        session.pop('consulta_result', None)

    session.pop('bayface_rack', None)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(threaded=True, debug=True, processes=3)
