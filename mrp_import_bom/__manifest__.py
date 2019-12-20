# -*- coding: utf-8 -*-
{
    'name': "MRP Import BOM",

    'summary': """
       MRP Import Bom
       """,

    'author': "Praxya Formaplus",
    'website': "https://www.praxyaformaplus.com",
    'category': 'MRP',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ["mrp"],

    # always loaded
    'data': [
        "wizard/mrp_bom_import_view.xml",
    ],
}
