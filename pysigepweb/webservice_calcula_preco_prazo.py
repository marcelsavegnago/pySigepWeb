# -*- coding: utf-8 -*-
# #############################################################################
#
#    Brazillian Carrier Correios Sigep WEB
#    Copyright (C) 2015 KMEE (http://www.kmee.com.br)
#    @author: Michell Stuttgart <michell.stuttgart@kmee.com.br>
#
#    Sponsored by Europestar www.europestar.com.br
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from .webservice_interface import *
from .resposta_calcula_preco_prazo import RespostaCalculaPrecoPrazo


class WebserviceCalculaPrecoPrazo(WebserviceInterface):

    _OPCAO = {
        True: 'S',
        False: 'N',
    }

    _FORMATO_CAIXA_PACOTE = 1
    _FORMATO_ROLO_PRISMA = 2
    _FORMATO_ENVELOPE = 3

    _nCdFormato = {
        '001': _FORMATO_ENVELOPE,
        '002': _FORMATO_CAIXA_PACOTE,
        '003': _FORMATO_ROLO_PRISMA,
    }

    _URL = 'http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx?WSDL'

    def __init__(self):
        super(WebserviceCalculaPrecoPrazo, self).__init__(
            WebserviceCalculaPrecoPrazo._URL)

    @property
    def url(self):
        return WebserviceCalculaPrecoPrazo._URL

    def calcula_preco_prazo(self, lista_obj_servico_postagem, codigo_admin,
                            cep_origem, cep_destino, peso, obj_dimensao,
                            usar_mao_propria, valor_declarado,
                            aviso_recebimento, cliente):

        cep_origem = cep_origem.replace('-', '')
        cep_destino = cep_destino.replace('-', '')

        # Para ncdservico = 3 (Envelope), o peso maximo permitido e 1 kg
        ncdservico = WebserviceCalculaPrecoPrazo._nCdFormato[
            obj_dimensao.codigo]

        scdmaopropria = WebserviceCalculaPrecoPrazo._OPCAO[usar_mao_propria]
        scdavisorecebimento = \
            WebserviceCalculaPrecoPrazo._OPCAO[aviso_recebimento]

        cod_servicos = ''
        for obj_servico in lista_obj_servico_postagem.values():
            cod_servicos += str(obj_servico.codigo) + ','

        try:
            servicos = self._service.CalcPrecoPrazo(
                codigo_admin, cliente.senha, cod_servicos, cep_origem,
                cep_destino, peso, ncdservico, obj_dimensao.comprimento,
                obj_dimensao.altura, obj_dimensao.largura,
                obj_dimensao.diametro, scdmaopropria,
                valor_declarado, scdavisorecebimento)

            result = []

            for servico in servicos.Servicos.cServico:
                result.append(RespostaCalculaPrecoPrazo(servico))

            return result

        except WebFault as exc:
            raise ErroConexaoComServidor(exc)
