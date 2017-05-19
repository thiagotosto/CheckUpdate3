#!/usr/bin/env python
# -*- coding: utf-8 -*

import re
import string as str_class


class Inconsistence_check():
    def __init__(self):
        self.normas = {}

        self.normas['Nome'] = 'upper'
        self.normas['Baia'] = ''
        self.normas['Categoria'] = 'lower'
        self.normas['Resp'] = 'capt'
        self.normas['Serial'] = 'upper'
        self.normas['Fabricante'] = 'upper'
        self.normas['Modelo'] = 'capt'
        self.normas['Localizacao'] = ''
        self.normas['Rack'] = ''
        self.normas['Patrimonio'] = ''
        self.normas['Hostname'] = 'lower'
        self.normas['Ip'] = ''
        self.normas['Em uso?'] = 'upper'
        self.normas['SAID'] = ''
        self.normas['Contrato'] = 'upper'
        self.normas['Start_date'] = ''
        self.normas['End_date'] = ''
        self.normas['Legado'] = 'upper'

    #METODOS DE CONTROLE

    #metodo que osquestra a aplicação de regra
    def orquestrator(self, dados):
        retorno = []

        for elemento in dados:
            campo_atual = elemento['campo']
            valor_atual = elemento['valor']
            regras = self._parse(self.normas[campo_atual])
            for regra in regras:
                elemento['valor'] = self._aplica_regra(regra, valor_atual)
            retorno.append({'campo': elemento['campo'], 'valor': elemento['valor']})

        return retorno

    #método que parseia string de regras
    def _parse(self, regras):
        return regras.split('/')

    #método que faz o match da string regra com o método de aplicação e o chama
    def _aplica_regra(self, regra, arg):
        if regra == 'upper':
            return self._upper(arg)
        if regra == 'lower':
            return self._lower(arg)
        if regra == 'capt':
            return self._capitalize(arg)

        return arg


    #METODOS DE APLICAÇÃO DE REGRAS

    #transforma em maiúsculo
    def _upper(self, string):
        return string.upper();

    #transforma em minúsculo
    def _lower(self, string):
        return string.lower();

    def _capitalize(self, string):
        return str_class.capwords(string)
