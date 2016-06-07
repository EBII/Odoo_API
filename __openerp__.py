# -*- coding: utf-8 -*-
##############################################################################
#
#    MODULE_NAME module for Odoo
#    Copyright (C) 2016 Saaslys MonsieurB (http://www.saaslys.com)
#    @author Alexis de Lattre <acontact@saaslys.com>
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


{
    'name': 'Api-helper',
    'version': '9.0.0.1.0',
    'category': 'help & how-to',
    'license': 'AGPL-3',
    'summary': 'How good usage for asking value from all fields type',  # v7: size=64, v8: no size limit
    'description': """
        This module is an helper to try all king off request for evry kind of fields
        with the new API in Odoo 9.0c
        This module has been written by EBII MonsieurB <contact@ebii.fr>
        from snippets of
        Alexis de Lattre from Akretion <alexis.delattre@akretion.com>.
    """,
    'author': 'EBII MonsieurB',
    'contributors': 'Alexis de lattre',  # text
    'website': 'https://www.ebii.fr',

    #les screenshots en v8: mettre dans static/description/, sans déclaration
    # dans ce fichier
    # pour l'icone du module (PNG 64x64 ou 128x128): rien à mettre dans __openerp__.py
    # v7: ./static/src/img/icon.png
    # v8: ./static/description/icon.png
    # v9: ./static/description/icon.png
    'url': 'http://www.ebii.fr/odoo/Doc_Api_helper.html',  # ??
    'installable': True,
    'auto_install': False,
    'application': False,
}