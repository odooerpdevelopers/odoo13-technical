# -*- coding: utf-8 -*-
{
    'name': "Report Ejemplo Webinar Odoo 13.0",

    'summary': """
       Report Ejemplo Webinar Odoo 13.0
       """,

    'author': "Praxya Formaplus",
    'website': "https://www.praxyaformaplus.com",
    'category': 'MRP',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ["account"],

    # always loaded
    'data': [
        "report/reports.xml",
        "report/report_invoice.xml",
    ],
}

