# -*- coding: utf-8 -*-
from suds import client


class InterfaceServico(object):

    def __init__(self, url):
        self.url = url
        self.client = None

        print 'Conectando...'
        try:
            self.cliente = client.Client(url)
        except client.TransportError as exp:
            print exp.message
            exit(-1)
