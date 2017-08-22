#!/usr/bin/env python
# -*- coding: utf-8 -*

from random import *

def genSessionKey():

    #tamanho da session key
    length = 10

    return ''.join(random.choice(string.lowercase) for i in range(length))
    
