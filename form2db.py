#!/usr/bin/env python
# -*- coding: utf-8 -*
from dbconnect import *

#CONSULTA
def form2db_consulta(query):    # Recebe como parametro uma lista de dicionario com campo e valor das clausulas
    #instanciando sessão        #e retorna uma lista com objetos do modelo do banco.

    #session = Session()

    filters = []
    q = session.query(Inventario)

    for objeto in query:
        #filters.append(objeto['campo'] == objeto['valor'])
        #print "\n\nTeste form2db_consulta ", objeto, "\n\n";
        filters.append(objeto)
    result = q.filter(*filters).all()

    session.commit()

    return result

#UPDATE
def form2db_update(target, value, indexes):
    #instanciando Sessão
    #session = Session()

    q = session.query(Inventario)
    print '\n\nForm2db update:\n\n'
    #for objeto in query:
        #filters.append(objeto['campo'] == objeto['valor'])
        #filters.append(objeto)

    print "target: ",target,",\tvalue: ",value,",\tindexes: ", indexes

    print "\n elemento:\t"
    #instancia elemento alvo
    elemento = q.filter(Inventario.serial == target).first()
    print "\n"

    #print "\n\nelemento: ", elemento, "elemento.serial: ", elemento.serial, "elemento.atributos[4]: ", elemento.atributos[4], "\n\n"
    #print "\n\nColunas\t", Inventario.__table__.columns, "\n\n"


    for i in range(len(indexes)):
        #print "\n\nValor:", value[i]['valor'], "\tIndexes: ", indexes[i]," \n\n"
        #elemento.em_uso = value[i]['valor']
        setattr(elemento, indexes[i], value[i]['valor'])

    print "\n\nq: ", q, "\n"

    session.commit()

    #return result

#INSERT
def form2db_insert(campos, atributos):
    #instanciando sessão

    #session.expire_all()
    #session = Session()

    #instanciando seção
    q = session.query(Inventario)

    #instanciando objeto do banco
    new = Inventario()

    print "\n\nAtributos: \n\n", atributos, "Campos: ", campos

    for i in range(len(atributos)):
        setattr(new, campos[i], atributos[i]['valor'])

    session.add(new)
    session.commit()


#UPDATE
def form2db_remove(target):
    #instanciando Sessão
    #session = Session()

    q = session.query(Inventario)

    #instancia elemento alvo
    elemento = q.filter(Inventario.serial == target).first()

    q.session.delete(elemento)

    session.commit()




def binder(to_bind, flag):    #recebe como parametro um tupla de dicionarios que representam as clausulas
    query = []

    print '\n\n\nBINDER: to_bind = %s\n\n\n' % to_bind

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
                #query.append(Inventario.nome == objeto['valor'])
                query.append('nome')
            if objeto['campo'] == 'Baia':
                #query.append(Inventario.baia == objeto['valor'])
                query.append('baia')
            if objeto['campo'] == 'Categoria':
                #query.append(Inventario.categoria == objeto['valor'])
                query.append('categoria')
            if objeto['campo'] == 'Resp':
                #query.append(Inventario.resp == objeto['valor'])
                query.append('resp')
            if objeto['campo'] == 'Serial':
                #query.append(Inventario.serial == objeto['valor'])
                query.append('serial')
            if objeto['campo'] == 'Fabricante':
                #query.append(Inventario.fabricante == objeto['valor'])
                query.append('fabricante')
            if objeto['campo'] == 'Modelo':
                #query.append(Inventario.modelo == objeto['valor'])
                query.append('modelo')
            if objeto['campo'] == 'Localizacao':
                #query.append(Inventario.localizacao == objeto['valor'])
                query.append('localizacao')
            if objeto['campo'] == 'Rack':
                #query.append(Inventario.rack == objeto['valor'])
                query.append('rack')
            if objeto['campo'] == 'Patrimonio':
                #query.append(Inventario.patrimonio == objeto['valor'])
                query.append('patrimonio')
            if objeto['campo'] == 'Hostname':
                #query.append(Inventario.hostname == objeto['valor'])
                query.append('hostname')
            if objeto['campo'] == 'IP':
                #query.append(Inventario.ip == objeto['valor'])
                query.append('ip')
            if objeto['campo'] == 'Em uso?':
                #query.append(Inventario.em_uso == objeto['valor'])
                query.append('em_uso')
            if objeto['campo'] == 'SAID':
                #query.append(Inventario.said == objeto['valor'])
                query.append('said')
            if objeto['campo'] == 'Contrato':
                #query.append(Inventario.contrato == objeto['valor'])
                query.append('contrato')
            if objeto['campo'] == 'Start Date':
                #query.append(Inventario.start_date == objeto['valor'])
                query.append('start_date')
            if objeto['campo'] == 'End Date':
                #query.append(Inventario.end_date == objeto['valor'])
                query.append('end_date')
            if objeto['campo'] == 'Legado':
                #query.append(Inventario.legado == objeto['valor'])
                query.append('legado')
            if objeto['campo'] == 'Posicao':
                #query.append(Inventario.legado == objeto['valor'])
                query.append('posicao')

        print "QUERY:", query," \n\n\n"

    return query

def parse_posicao(objeto):
    objeto['posicao'] = objeto['posicao'].split('-')

    if (len(objeto['posicao']) == 2):
        objeto['posicao'][0] = int(objeto['posicao'][0])
        objeto['posicao'][1] = int(objeto['posicao'][1])





'''    if (type(objeto.posicao) == str):
        print "\n\n\nSerial: ", objeto.serial
        print "\nRack: ", objeto.rack
        print "\nPosição", objeto.posicao,"\n\n\n"
        #separando limites
        objeto.posicao = objeto.posicao.split('-')

        #fazendo typecast para inteiro
        objeto.posicao[0] = int(objeto.posicao[0])
        objeto.posicao[1] = int(objeto.posicao[1])
'''
