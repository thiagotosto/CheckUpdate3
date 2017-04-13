from dbconnect import *


def form2db_consulta(query):    # Recebe como parametro uma lista de dicionario com campo e valor das clausulas
                                #e retorna uma lista com objetos do modelo do banco.
    filters = []
    q = session.query(Inventario)

    for objeto in query:
        filters.append(objeto['campo'] == objeto['valor'])

    result = q.filter(*filters).all()

    return result

def binder(to_bind):    #recebe como parametro um tupla de dicionarios que representam as clausulas
    query = []

    for objeto in to_bind:
        if objeto['campo'] == 'Nome':
            query.append({'campo': Inventario.nome, 'valor': objeto['valor']})
        if objeto['campo'] == 'Baia':
            query.append({'campo': Inventario.baia, 'valor': objeto['valor']})
        if objeto['campo'] == 'Categoria':
            query.append({'campo': Inventario.categoria, 'valor': objeto['valor']})
        if objeto['campo'] == 'Resp':
            query.append({'campo': Inventario.resp, 'valor': objeto['valor']})
        if objeto['campo'] == 'Serial':
            query.append({'campo': Inventario.serial, 'valor': objeto['valor']})
        if objeto['campo'] == 'Fabricante':
            query.append({'campo': Inventario.fabricante, 'valor': objeto['valor']})
        if objeto['campo'] == 'Modelo':
            query.append({'campo': Inventario.modelo, 'valor': objeto['valor']})
        if objeto['campo'] == 'Localizacao':
            query.append({'campo': Inventario.localizacao, 'valor': objeto['valor']})
        if objeto['campo'] == 'Rack':
            query.append({'campo': Inventario.rack, 'valor': objeto['valor']})
        if objeto['campo'] == 'Patrimonio':
            query.append({'campo': Inventario.patrimonio, 'valor': objeto['valor']})
        if objeto['campo'] == 'Hostname':
            query.append({'campo': Inventario.hostname, 'valor': objeto['valor']})
        if objeto['campo'] == 'IP':
            query.append({'campo': Inventario.ip, 'valor': objeto['valor']})
        if objeto['campo'] == 'Em uso?':
            query.append({'campo': Inventario.em_uso, 'valor': objeto['valor']})
        if objeto['campo'] == 'Said':
            query.append({'campo': Inventario.said, 'valor': objeto['valor']})
        if objeto['campo'] == 'Contrato':
            query.append({'campo': Inventario.contrato, 'valor': objeto['valor']})
        if objeto['campo'] == 'Start Date':
            query.append({'campo': Inventario.start_date, 'valor': objeto['valor']})
        if objeto['campo'] == 'End Date':
            query.append({'campo': Inventario.end_date, 'valor': objeto['valor']})
        if objeto['campo'] == 'Legado':
            query.append({'campo': Inventario.leg_prod, 'valor': objeto['valor']})

    return query
