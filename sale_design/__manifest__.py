# -*- coding: utf-8 -*-
{
    'name': "Sale Design",

    'summary': """
       It is define to design into sale order. """,

    'description': """
        This model defines the record to design in sales order.
    """,

    'author': "Julio Cesar Bravo",
    'website': "https://www.soloodoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/Sales',
    'version': '14.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/inherit_sale.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
    'auto_install': False
}
