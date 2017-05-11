from dbconnect import *


def form2db_consulta(query):    # Recebe como parametro uma lista de dicionario com campo e valor das clausulas
                                #e retorna uma lista com objetos do modelo do banco.
    filters = []
    q = session.query(Inventario)

    for objeto in query:
        #filters.append(objeto['campo'] == objeto['valor'])
        #print "\n\nTeste form2db_consulta ", objeto, "\n\n";
        filters.append(objeto)
    result = q.filter(*filters).all()

    return result

def form2db_update(target, value, indexes):
    q = session.query(Inventario)
    print '\n\nForm2db update:\n\n'
    #for objeto in query:
        #filters.append(objeto['campo'] == objeto['valor'])
        #filters.append(objeto)

    #print "target: ",target,",\tvalue: ",value,",\tindexes: ", indexes

    #instancia elemento alvo
    elemento = q.filter(Inventario.serial == target).first()

    #print "\n\nelemento: ", elemento, "elemento.serial: ", elemento.serial, "elemento.atributos[4]: ", elemento.atributos[4], "\n\n"
    #print "\n\nColunas\t", Inventario.__table__.columns, "\n\n"


    for i in range(len(indexes)):
        #print "\n\nValor:", value[i]['valor'], "\tIndexes: ", indexes[i]," \n\n"
        #elemento.em_uso = value[i]['valor']
        setattr(elemento, indexes[i], value[i]['valor'])

    q.session.commit()

    #return result


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
            if objeto['campo'] == 'Said':
                query.append(Inventario.said.op('regexp')('.*%s.*' % objeto['valor']))
            if objeto['campo'] == 'Contrato':
                query.append(Inventario.contrato.op('regexp')('.*%s.*' % objeto['valor']))
            if objeto['campo'] == 'Start Date':
                query.append(Inventario.start_date.op('regexp')('.*%s.*' % objeto['valor']))
            if objeto['campo'] == 'End Date':
                query.append(Inventario.end_date.op('regexp')('.*%s.*' % objeto['valor']))
            if objeto['campo'] == 'Legado':
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
            if objeto['campo'] == 'Said':
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

        print "QUERY:", query," \n\n\n"

    return query
