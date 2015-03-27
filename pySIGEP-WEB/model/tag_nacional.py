# -*- coding: utf-8 -*-
from tag_base import TagBase


class TagNacional(TagBase):

    def __init__(self, endereco, numero_nfe, serie_nfe, valor_a_cobrar,
                 codigo_usuario_postal='', centro_custo_cliente='',
                 valor_nfe=False, natureza_nfe='', descricao_objeto=''):
        self.endereco = endereco
        self.codigo_usuario_postal = codigo_usuario_postal
        self.centro_custo_cliente = centro_custo_cliente
        self.num_nfe = numero_nfe
        self.serie_nfe = serie_nfe
        self.valor_nfe = valor_nfe
        self.natureza_nfe = natureza_nfe
        self.descricao_objeto = descricao_objeto
        self.valor_a_cobrar = valor_a_cobrar

    def get_xml(self):

        xml = u'<nacional>'
        xml += u'<bairro_destinatario><![CDATA[%s]]></bairro_destinatario>' % \
               self.endereco.bairro
        xml += u'<cidade_destinatario><![CDATA[%s]]></cidade_destinatario>' % \
               self.endereco.cidade
        xml += u'<uf_destinatario>%s</uf_destinatario>' % self.endereco.uf
        xml += u'<cep_destinatario><![CDATA[%d]]></cep_destinatario>' % \
               self.endereco.cep
        xml += u'<codigo_usuario_postal>%s</codigo_usuario_postal>' % \
               self.codigo_usuario_postal
        xml += u'<centro_custo_cliente>%s</centro_custo_cliente>' % \
               self.centro_custo_cliente
        xml += u'<numero_nota_fiscal>%d</numero_nota_fiscal>' % self.num_nfe
        xml += u'<serie_nota_fiscal>%s</serie_nota_fiscal>' % self.serie_nfe
        xml += u'<valor_nota_fiscal>%s</valor_nota_fiscal>' % str(
            self.valor_nfe) if self.valor_nfe else ''
        xml += u'<natureza_nota_fiscal>%s</natureza_nota_fiscal>' % \
               self.natureza_nfe
        xml += u'<descricao_objeto><![CDATA[%s]]></descricao_objeto>' % \
               self.descricao_objeto
        xml += u'<valor a cobrar>%s</valor a cobrar>' % str(
            self.valor_a_cobrar) if self.valor_a_cobrar else ''
        xml += u'</nacional>'

        return xml