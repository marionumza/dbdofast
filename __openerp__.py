# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Softecnico SA
#    Licence: 
#
##############################################################################

{
    "name": "Pequeño Comercio",
    "version": "0.2",
    "category": "Generic Modules/Others",
    'summary': 'Gestión de un comercio pequeño',
    "description": """
Este modulo sirve para poder administrar un pequeño comercio
=================================================================

Lo que intentamos hacer con este modulo es una pantalla de gestión
para poder administrar rapidamente los datos básicos de un comercio pequeño

""",
    "author": "Softecnico S.A.",
    "website": "https://www.sudano.net",
    "summary": "Ayuda a la pequeña empresa",
    "depends": ["base","hr","crm","account_voucher"],
    "data": [
        "views/menu_principal.xml",
        "views/repartidores_views.xml",
        "views/repartos_views.xml",
        "security/ir.model.access.csv"
        ],
    "init_xml" : [],
    "demo_xml" : [],
    "active": False,
    "installable": True,
    "application": True,
    "auto_install": False
}