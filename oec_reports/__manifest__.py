# -*- coding: utf-8 -*-
{
    'name': "OEC Reports",

    'summary': """
       Reports personalizados
       * Ventas
       """,

    'description': """
        -- Reports personalizados ---
       * Ventas
    """,

    'author': "OdooERPCloud",
    'website': "https://www.odooerpcloud.com",
    'category': 'Reporting',
    'version': '13.0.0.7',

    # any module necessary for this one to work correctly
    'depends': ['web', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/report_templates.xml',
        'views/res_company_view.xml',
        'report/report_sale_order.xml',
        'data/report_layout.xml',
    ],

}
