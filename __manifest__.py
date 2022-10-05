# -*- coding: utf-8 -*-
{
    'name': "Hello World",

    'summary': """
        Description of Hello World module
    """,

    'description': """
        Description of Hello World module
    """,

    'author': "Ernesto J. Suárez Pons",
    'website': "http://www.ejsp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'license': 'LGPL-3',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',
        'views/views.xml',
    ],
    'qweb': [
        'static/src/xml/hello_world.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    
    'auto_install': False,
    'application': True,
}
