#!/usr/bin/env python
# -*- coding: utf-8 -*

from flask import Flask, render_template, request, session, redirect, url_for
from form2db import *
from inconsistence_check import *
from db2flask import *

app = Flask(__name__)


app.secret_key = 'likujnyhtbgrvf67543'

globalSession = dict()
globalSession['consulta'] = []      #inicializando variavel global de Consulta
globalSession['update'] = []        #inicializando variavel global de Update
globalSession['insert'] = []        #inicializando variavel global de Insert
globalSession['insert'] = []        #inicializando variavel global de Insert
globalSession['bayface_rack'] = []  #inicializando variavel global de Bayface
globalValues = dict()
globalValues['Header'] = ['Nome','Baia','Categoria','Resp','Serial','Fabricante','Modelo','Localizacao','Rack', 'Posicao','Patrimonio','Hostname','IP','Em uso?','SAID','Contrato','Start Date','End Date','Legado']


@app.route('/')
def index():
    return render_template('index.html', globalSession=globalSession)

#CONSULTA ---------------------------------------------------------------------------------------------------

#renderizando clausulas da consulta
@app.route('/consulta/', methods=['POST'])
def consulta():

    print '\n\nPASSEI NA CONSULTA!!!\n\n'

    globalSession['consulta'].append({'campo': request.form['campo'], 'valor': request.form['valor']})
    print "globalSession['consulta']: ", globalSession['consulta']

    return render_template('index.html', globalSession=globalSession)

#renderiza o resultado da consulta
@app.route('/consulta_result/')
def consulta_result():

    print '\n\nPASSEI NA CONSULTA_RESULT!!!\n\n'

    bind = binder(globalSession['consulta'], 'c')
    globalSession['consulta_result'] = form2db_consulta(bind)

    #print "\n\nCONSULTA_RESULT",globalSession['consulta_result'], "\n\n"
    #print "\n\nDIDIONARIO: ", dbAsDict(globalSession['consulta_result']), "\n\n"
    #print dbAsDict(globalSession['consulta_result'])

    #teste de json dump
    #teste = json.dumps(globalSession['consulta_result'])
    asDict = dbAsDict(globalSession['consulta_result'])
    print "\n\n", asDict, "\n\n"

    return render_template('consulta_result.html', globalSession=globalSession, globalValues=globalValues, asDict=asDict)

#UPDATE -----------------------------------------------------------------------------------------------------

#renderizando clausulas do update
@app.route('/consulta_result/update', methods=['POST'])
def update():

    #print "\n\nPASSEI NO UPDATE!!!\n\n"

    #zerando lixo de update anterior
    globalSession['update'] = []

    #pegando serial do elemento atual
    elemento_atual = request.form['serial-id-update']

    #populando update
    for header in globalValues['Header']:
        if request.form[header] != '':
            globalSession['update'].append({'campo': header, 'valor': request.form[header]})

    #instanciando inconsistente check
    ict = Inconsistence_check()

    #checando inconsistencias de formatação
    globalSession['update'] = ict.orquestrator(globalSession['update'])

    index = binder(globalSession['update'], 'u')
    form2db_update(elemento_atual, globalSession['update'], index)

    #teste identificador unico
    #print elemento_atual

    '''
    #teste globalSession
    for teste_print in globalSession['update']:
        print teste_print
    '''

    return render_template('consulta_result.html', globalSession=globalSession, globalValues=globalValues)


#INSERT -----------------------------------------------------------------------------------------------------

@app.route('/insert/')
def insert():
    return render_template('insert.html', globalValues=globalValues)

@app.route('/insert_result/', methods=['POST'])
def insert_result():

    #print "Passei aqui!!!"

    #zerando lixo de insert anterior
    globalSession['insert'] = []

    #TESTE!!!
    #print "Headers", globalValues['Header']


    #populando insert
    for header in globalValues['Header']:
        if request.form[header] != '':
            #print "\ncampo: ", header, "\tvalor: ", request.form[header]
            globalSession['insert'].append({'campo': header, 'valor': request.form[header]})
            #print "passei dentro do for depois do append"


    #print "passei aqui depois do for"
    #print "insert: ", globalSession['insert']

    #instanciando inconsistente check
    ict = Inconsistence_check()

    #checando inconsistencias de formatação
    globalSession['insert'] = ict.orquestrator(globalSession['insert'])

    #fazendo bind
    bind = binder(globalSession['insert'], 'u')

    #fazendo insert
    form2db_insert(bind, globalSession['insert'])


    return render_template('insert.html', globalValues=globalValues)

#BAYFACE ----------------------------------------------------------------------------------------------------

@app.route('/bayface/', methods=['GET','POST'])
def bayface():

    #print "\n\n\n", globalSession['bayface_rack']
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
    globalSession['bayface_rack'] = form2db_consulta(bind)

    #print "\n\n\n", globalSession['bayface_rack'], "\n\n\n"

    #for server in globalSession['bayface_rack']:
    #    parse_posicao(server)

    #transformando lista de pbjetos em lista de dicionarios correspondentes
    asDict = dbAsDict(globalSession['bayface_rack'])

    #parseando o atributo posicao
    for server in asDict:
        parse_posicao(server)

    print "\n\n\nasDict: ", asDict, "\n\n\n"

    return render_template('bayface.html', globalSession=globalSession, rack=rack, asDict=asDict)

#REMOVE -----------------------------------------------------------------------------------------------------
@app.route('/remove/',  methods=['POST'])
def remove():

    #pegando serial do elemento atual
    elemento_atual = request.form['serial-id-remove']

    #index = binder(elemento_atual, 'd')
    form2db_remove(elemento_atual)

    asDict = dbAsDict(globalSession['consulta_result'])

    return render_template('consulta_result.html', globalSession=globalSession, globalValues=globalValues, asDict=asDict)

#RESET ------------------------------------------------------------------------------------------------------

@app.route('/reset')
def reset_session():

    for i in range(len(globalSession['consulta'])):
        globalSession['consulta'].pop(0)

    for i in range(len(globalSession['update'])):
        globalSession['update'].pop(0)

    if 'consulta_result' in globalSession.keys():
        for i in range(len(globalSession['consulta_result'])):
            globalSession['consulta_result'].pop(0)

    for i in range(len(globalSession['bayface_rack'])):
        globalSession['bayface_rack'].pop(0)

    return redirect(url_for('index'))
