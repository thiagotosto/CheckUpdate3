#!/usr/bin/env python
# -*- coding: utf-8 -*

from flask import Flask, render_template, request, session, redirect, url_for
from form2db import *
from inconsistence_check import *

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

#CONSULTA ---------------------------------------------------------------------------------------------------

#renderizando clausulas da consulta
@app.route('/consulta/', methods=['POST'])
def consulta():
    globalSession['consulta'].append({'campo': request.form['campo'], 'valor': request.form['valor']})
    print "globalSession['consulta']: ", globalSession['consulta']

    return render_template('index.html', globalSession=globalSession)

#renderiza o resultado da consulta
@app.route('/consulta_result/')
def consulta_result():

    bind = binder(globalSession['consulta'], 'c')
    globalSession['consulta_result'] = form2db_consulta(bind)

    #teste de json dump
    #teste = json.dumps(globalSession['consulta_result'])

    return render_template('consulta_result.html', globalSession=globalSession, globalValues=globalValues)

#UPDATE -----------------------------------------------------------------------------------------------------

#renderizando clausulas do update
@app.route('/consulta_result/update', methods=['POST'])
def update():

    #zerando lixo de update anterior
    globalSession['update'] = []

    #pegando serial do elemento atual
    elemento_atual = request.form['serial-id']

    #populando update
    for header in globalValues['Header']:
        if request.form[header] != '':
            globalSession['update'].append({'campo': header, 'valor': request.form[header]})

    #instanciando inconsistente check
    ict = Inconsistence_check()

    #checando inconsistencias d formatação
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


    return redirect(url_for('index'))
