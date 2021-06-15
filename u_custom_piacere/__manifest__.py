# -*- coding: utf-8 -*-
{
    'name': "Unoobi | Piacere personalization",
    'summary': """
        Piacere Personalization.
    """,
    'description': """
        Piacere Personalization
    """,
    'sequence': 50,
    'author': "UNOOBI",
    'category': 'Contact',
    'version': '1.0',
    'depends': ['sale_management', 'sale'],
    'data': [
        # ==== SECURITY
        'security/ir.model.access.csv',
        # === VIEWS
        'views/sale_order_amount_views.xml',
    ],
    'demo': [],
}
