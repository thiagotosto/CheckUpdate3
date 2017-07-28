def dbAsDict(object_list):
    result = []
    for obj in object_list:
        result.append({
                        'nome': str(obj.nome).decode('cp1252'),
                        'baia': str(obj.baia),
                        'categoria': str(obj.categoria).decode('cp1252'),
                        'resp': str(obj.resp).decode('cp1252'),
                        'serial': str(obj.serial).decode('cp1252'),
                        'fabricante': str(obj.fabricante).decode('cp1252'),
                        'modelo': str(obj.modelo).decode('cp1252'),
                        'localizacao': str(obj.localizacao).decode('cp1252'),
                        'rack': str(obj.rack),
                        'patrimonio': str(obj.patrimonio),
                        'hostname': str(obj.hostname).decode('cp1252'),
                        'ip': str(obj.ip).decode('cp1252'),
                        'em_uso': str(obj.em_uso).decode('cp1252'),
                        'said': str(obj.said),
                        'contrato': str(obj.contrato).decode('cp1252'),
                        'start_date': str(obj.start_date),
                        'end_date': str(obj.end_date),
                        'leg_prod': str(obj.leg_prod).decode('cp1252'),
                        'posicao': str(obj.posicao)
                        })
    return result
