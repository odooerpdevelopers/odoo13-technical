# -*- coding: utf-8 -*-
{
    'name': "Purchase Order Line Origin",

    'summary': """
       Add origin field in purchase order line
       """,

    'author': "Praxya Formaplus",
    'website': "https://www.praxyaformaplus.com",
    'category': 'Gestion Vehiculo',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ["purchase"],

    # always loaded
    'data': [
        "views/purchase_order_view.xml",
    ],
}
