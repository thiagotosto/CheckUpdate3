from dbconnect import *


def form2db_consulta(query):    # Recebe como parametro uma lista de dicionario com campo e valor das clausulas
                                #e retorna uma lista com objetos do modelo do banco.
    filters = []
    q = session.query(Inventario)

    for objeto in query:
        #filters.append(objeto['campo'] == objeto['valor'])
        filters.append(objeto)
    result = q.filter(*filters).all()

    return result

def form2db_update():
    pass

def binder(to_bind):    #recebe como parametro um tupla de dicionarios que representam as clausulas
    query = []

    print '\n\n\nBINDER: to_bind = %s\n\n\n' % to_bind

    for objeto in to_bind:
        if objeto['campo'] == 'Nome':
            query.append(Inventario.serial.op('regexp')('.*%s.*' % objeto['valor']))
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

        print "QUERY:", query," \n\n\n"

    return query
