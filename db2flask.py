def dbAsDict(object_list):
    result = []
    for obj in object_list:
        print "PASSEEEEEEEEEEI AQUIIIIIIII!!!!!!!!!!!!!!!!!!"

        result.append({
                        'nome': str(obj.nome).decode('cp1252'),
                        'baia': str(obj.baia).decode('cp1252'),
                        'categoria': str(obj.categoria).decode('cp1252'),
                        'resp': str(obj.resp).decode('cp1252'),
                        'serial': str(obj.serial).decode('cp1252'),
                        'fabricante': str(obj.fabricante).decode('cp1252'),
                        'modelo': str(obj.modelo).decode('cp1252'),
                        'localizacao': str(obj.localizacao).decode('cp1252'),
                        'rack': str(obj.rack).decode('cp1252'),
                        'patrimonio': str(obj.patrimonio).decode('cp1252'),
                        'hostname': str(obj.hostname).decode('cp1252'),
                        'ip': str(obj.ip).decode('cp1252'),
                        'em_uso': str(obj.em_uso).decode('cp1252'),
                        'said': str(obj.said).decode('cp1252'),
                        'contrato': str(obj.contrato).decode('cp1252'),
                        'start_date': str(obj.start_date).decode('cp1252'),
                        'end_date': str(obj.end_date).decode('cp1252'),
                        'leg_prod': str(obj.leg_prod).decode('cp1252'),
                        'posicao': str(obj.posicao).decode('cp1252')
                        })
    return result
