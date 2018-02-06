#!/usr/bin/env python
# -*- coding: utf-8 -*
from dbconnect import *

#CONSULTA
def form2db_consulta(query):    # Recebe como parametro uma lista de dicionario com campo e valor das clausulas

    filters = []
    q = dbsession.query(Inventario)

    for objeto in query:
        filters.append(objeto)
    result = q.filter(*filters).all()

    dbsession.commit()

    return result

# CONSULTA EXATA DE RACK
def form2db_consulta_rack(query):    # Recebe como um dicionario com campo e valor das clausulas

    filters = []
    q = dbsession.query(Inventario)

    result = q.filter_by(rack = query['valor']).all()

    dbsession.commit()

    return result

#UPDATE
def form2db_update(target, value, indexes):

    q = dbsession.query(Inventario)

    #instancia elemento alvo
    elemento = q.filter(Inventario.serial == target).first()

    for i in range(len(indexes)):
        setattr(elemento, indexes[i], value[i]['valor'])

    dbsession.commit()

#INSERT
def form2db_insert(campos, atributos):

    #instanciando seção
    q = dbsession.query(Inventario)

    #instanciando objeto do banco
    new = Inventario()

    for i in range(len(atributos)):
        setattr(new, campos[i], atributos[i]['valor'])

    try:
        dbsession.add(new)
        dbsession.commit()
    except:
        dbsession.rollback()
        raise


#UPDATE
def form2db_remove(target):

    q = dbsession.query(Inventario)

    #instancia elemento alvo
    elemento = q.filter(Inventario.serial == target).first()

    q.session.delete(elemento)

    dbsession.commit()


def binder(to_bind, flag):    #recebe como parametro um tupla de dicionarios que representam as clausulas
    query = []

    #CONSULTA
    if flag == 'c' or flag == 'consulta':
        for objeto in to_bind:
            if objeto['campo'] == 'Nome':
                query.append(Inventario.nome.op('regexp')('.*%s.*' % objeto['valor']))
            if objeto['campo'] == 'Baia':
                query.append(Inventario.baia == objeto['valor'])
            if objeto['campo'] == 'Categoria':
                query.append(Inventario.categoria.op('regexp')('.*%s.*' % objeto['valor']))
            if objeto['campo'] == 'Resp':
                query.append(Inventario.resp.op('regexp')('.*%s.*' % objeto['valor']))
            if objeto['campo'] == 'Serial':
                query.append(Inventario.serial.op('regexp')('.*%s.*' % objeto['valor']))
            if objeto['campo'] == 'Fabricante':
                query.append(Inventario.fabricante.op('regexp')('.*%s.*' % objeto['valor']))
            if objeto['campo'] == 'Modelo':
                query.append(Inventario.modelo.op('regexp')('.*%s.*' % objeto['valor']))
            if objeto['campo'] == 'Localizacao':
                query.append(Inventario.localizacao.op('regexp')('.*%s.*' % objeto['valor']))
            if objeto['campo'] == 'Rack':
                query.append(Inventario.rack.op('regexp')('.*%s.*' % objeto['valor']))
            if objeto['campo'] == 'Patrimonio':
                query.append(Inventario.patrimonio.op('regexp')('.*%s.*' % objeto['valor']))
            if objeto['campo'] == 'Hostname':
                query.append(Inventario.hostname.op('regexp')('.*%s.*' % objeto['valor']))
            if objeto['campo'] == 'IP':
                query.append(Inventario.ip.op('regexp')('.*%s.*' % objeto['valor']))
            if objeto['campo'] == 'Em uso?':
                query.append(Inventario.em_uso.op('regexp')('.*%s.*' % objeto['valor']))
            if objeto['campo'] == 'SAID':
                query.append(Inventario.said.op('regexp')('.*%s.*' % objeto['valor']))
            if objeto['campo'] == 'Contrato':
                query.append(Inventario.contrato.op('regexp')('.*%s.*' % objeto['valor']))
            if objeto['campo'] == 'Start Date':
                query.append(Inventario.start_date.op('regexp')('.*%s.*' % objeto['valor']))
            if objeto['campo'] == 'End Date':
                query.append(Inventario.end_date.op('regexp')('.*%s.*' % objeto['valor']))
            if objeto['campo'] == 'Legado':
                query.append(Inventario.legado.op('regexp')('.*%s.*' % objeto['valor']))
            if objeto['campo'] == 'Posicao':
                query.append(Inventario.legado.op('regexp')('.*%s.*' % objeto['valor']))

        #UPDATE
    elif flag == 'u' or flag == 'update':
        for objeto in to_bind:
            if objeto['campo'] == 'Nome':
                query.append('nome')
            if objeto['campo'] == 'Baia':
                query.append('baia')
            if objeto['campo'] == 'Categoria':
                query.append('categoria')
            if objeto['campo'] == 'Resp':
                query.append('resp')
            if objeto['campo'] == 'Serial':
                query.append('serial')
            if objeto['campo'] == 'Fabricante':
                query.append('fabricante')
            if objeto['campo'] == 'Modelo':
                query.append('modelo')
            if objeto['campo'] == 'Localizacao':
                query.append('localizacao')
            if objeto['campo'] == 'Rack':
                query.append('rack')
            if objeto['campo'] == 'Patrimonio':
                query.append('patrimonio')
            if objeto['campo'] == 'Hostname':
                query.append('hostname')
            if objeto['campo'] == 'IP':
                query.append('ip')
            if objeto['campo'] == 'Em uso?':
                query.append('em_uso')
            if objeto['campo'] == 'SAID':
                query.append('said')
            if objeto['campo'] == 'Contrato':
                query.append('contrato')
            if objeto['campo'] == 'Start Date':
                query.append('start_date')
            if objeto['campo'] == 'End Date':
                query.append('end_date')
            if objeto['campo'] == 'Legado':
                query.append('leg_prod')
            if objeto['campo'] == 'Posicao':
                query.append('posicao')

    return query

def parse_posicao(objeto):
    objeto['posicao'] = objeto['posicao'].split('-')

    if (len(objeto['posicao']) == 2):
        objeto['posicao'][0] = int(objeto['posicao'][0])
        objeto['posicao'][1] = int(objeto['posicao'][1])
