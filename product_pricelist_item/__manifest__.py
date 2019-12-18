# -*- coding: utf-8 -*-
{
    'name': "Product Pricelist Item Show price",

    'summary': """
       Product Pricelist Item Show price
       """,

    'author': "Praxya Formaplus",
    'website': "https://www.praxyaformaplus.com",
    'category': 'Gestion Vehiculo',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ["product"],

    # always loaded
    'data': [
        "views/product_pricelist_view.xml",
    ],
}
