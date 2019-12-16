# -*- coding: utf-8 -*-
{
    'name': "Gestion Taller",

    'summary': """
       Gestion Vehiculos y Reparaciones
       """,

    'description': """
        Gestion Vehiculos y Reparaciones
    """,

    'author': "Praxya Formaplus",
    'website': "https://www.praxyaformaplus.com",
    'category': 'Gestion Vehiculo',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ["base"],

    # always loaded
    'data': [
        "security/ir.model.access.csv",
        "views/vehiculo_view.xml",
    ],
}
