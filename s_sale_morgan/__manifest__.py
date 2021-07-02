# -*- coding: utf-8 -*-
{
    'name': "Unoobi | s_sale_morgan",
    'summary': """
        Sale order personalization""",
    'description': """
        Sale order personalization
    """,
    'author': "Unoobi",
    'category': 'Account',
    'version': '0.1',
    'depends': [
        's_invoice_morgan',
        'contacts',
        'sale_management',
        'stock'
    ],
    'data': [
        # Views
        'views/res_partner_view.xml'
    ],
    'qweb': [],
    'installable': True,
}
