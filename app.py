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

session = dict()
#session['consulta'] = []      #inicializando variavel global de Consulta
#session['update'] = []        #inicializando variavel global de Update
#session['insert'] = []        #inicializando variavel global de Insert
#session['insert'] = []        #inicializando variavel global de Insert
#session['bayface_rack'] = []  #inicializando variavel global de Bayface
globalValues = dict()
globalValues['Header'] = ['Nome','Baia','Categoria','Resp','Serial','Fabricante','Modelo','Localizacao','Rack', 'Posicao','Patrimonio','Hostname','IP','Em uso?','SAID','Contrato','Start Date','End Date','Legado']

'''
@app.route('/')
def openSession():
    #thread.start_new_thread( index, ())
    return redirect(url_for('index'))

'''

@app.route('/')
def index():

    session['consulta'] = []      #inicializando variavel global de Consulta
    session['update'] = []        #inicializando variavel global de Update
    session['insert'] = []        #inicializando variavel global de Insert
    #session['insert'] = []        #inicializando variavel global de Insert
    session['bayface_rack'] = []  #inicializando variavel global de Bayface


    return render_template('index.html', session=session)

#CONSULTA ---------------------------------------------------------------------------------------------------

#renderizando clausulas da consulta
@app.route('/consulta/', methods=['POST'])
def consulta():

    print '\n\nPASSEI NA CONSULTA!!!\n\n'
    print 'session keys: %s\n\n' % (session.keys())

    session['consulta'].append({'campo': request.form['campo'], 'valor': request.form['valor']})
    print "session['consulta']: ", session['consulta']

    return render_template('index.html', session=session)

#renderiza o resultado da consulta
@app.route('/consulta_result/')
def consulta_result():

    print '\n\nPASSEI NA CONSULTA_RESULT!!!\n\n'

    bind = binder(session['consulta'], 'c')
    session['consulta_result'] = form2db_consulta(bind)

    #print "\n\nCONSULTA_RESULT",session['consulta_result'], "\n\n"
    #print "\n\nDIDIONARIO: ", dbAsDict(session['consulta_result']), "\n\n"
    #print dbAsDict(session['consulta_result'])

    #teste de json dump
    #teste = json.dumps(session['consulta_result'])
    asDict = dbAsDict(session['consulta_result'])
    print "\n\n", asDict, "\n\n"

    return render_template('consulta_result.html', session=session, globalValues=globalValues, asDict=asDict)

#UPDATE -----------------------------------------------------------------------------------------------------

#renderizando clausulas do update
@app.route('/consulta_result/update', methods=['POST'])
def update():

    #print "\n\nPASSEI NO UPDATE!!!\n\n"

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

    #teste identificador unico
    #print elemento_atual

    '''
    #teste session
    for teste_print in session['update']:
        print teste_print
    '''

    return render_template('consulta_result.html', session=session, globalValues=globalValues)


#INSERT -----------------------------------------------------------------------------------------------------

@app.route('/insert/')
def insert():
    return render_template('insert.html', globalValues=globalValues)

@app.route('/insert_result/', methods=['POST'])
def insert_result():

    #print "Passei aqui!!!"

    #zerando lixo de insert anterior
    session['insert'] = []

    #TESTE!!!
    #print "Headers", globalValues['Header']


    #populando insert
    for header in globalValues['Header']:
        if request.form[header] != '':
            #print "\ncampo: ", header, "\tvalor: ", request.form[header]
            session['insert'].append({'campo': header, 'valor': request.form[header]})
            #print "passei dentro do for depois do append"


    #print "passei aqui depois do for"
    #print "insert: ", session['insert']

    #instanciando inconsistente check
    ict = Inconsistence_check()

    #checando inconsistencias de formatação
    session['insert'] = ict.orquestrator(session['insert'])

    #fazendo bind
    bind = binder(session['insert'], 'u')

    #fazendo insert
    form2db_insert(bind, session['insert'])


    return render_template('insert.html', globalValues=globalValues)

#BAYFACE ----------------------------------------------------------------------------------------------------

@app.route('/bayface/', methods=['GET','POST'])
def bayface():

    #print "\n\n\n", session['bayface_rack']
    #print "\n\n\nRACK: ", rack

    #inicializando valor default de rack
    rack = 22

    print "\n\n\nRequest method: ", request.method, "\n\n\n"

    #carregando numero do rack escolhido
    if (request.method == 'POST'):
        print "\n\n\nRequest form: ", request.form['rack_input'], "\n\n\n"
        rack = request.form['rack_input']

    bind = binder([{'campo': 'Rack', 'valor': rack}], 'c')
    #print '\n\n\nbind: ', bind
    session['bayface_rack'] = form2db_consulta(bind)

    #print "\n\n\n", session['bayface_rack'], "\n\n\n"

    #for server in session['bayface_rack']:
    #    parse_posicao(server)

    #transformando lista de pbjetos em lista de dicionarios correspondentes
    asDict = dbAsDict(session['bayface_rack'])

    #parseando o atributo posicao
    for server in asDict:
        parse_posicao(server)

    print "\n\n\nasDict: ", asDict, "\n\n\n"

    return render_template('bayface.html', session=session, rack=rack, asDict=asDict)

#REMOVE -----------------------------------------------------------------------------------------------------
@app.route('/remove/',  methods=['POST'])
def remove():

    #pegando serial do elemento atual
    elemento_atual = request.form['serial-id-remove']

    #index = binder(elemento_atual, 'd')
    form2db_remove(elemento_atual)

    asDict = dbAsDict(session['consulta_result'])

    return render_template('consulta_result.html', session=session, globalValues=globalValues, asDict=asDict)

#RESET ------------------------------------------------------------------------------------------------------

@app.route('/reset')
def reset_session():

    #for i in range(len(session['consulta'])):
    #    session['consulta'].pop(0)
    session.pop('consulta', None)

    #for i in range(len(session['update'])):
    #    session['update'].pop(0)
    session.pop('update', None)

    if 'consulta_result' in session.keys():
        #for i in range(len(session['consulta_result'])):
        #    session['consulta_result'].pop(0)
        session.pop('consulta_result', None)

    #for i in range(len(session['bayface_rack'])):
    #    session['bayface_rack'].pop(0)
    session.pop('bayface_rack', None)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(threaded=True, debug=True, processes=3)
