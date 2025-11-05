# -*- coding: utf-8 -*-
{
    'name': "Hide Apps Menu",
    'summary': "Hide apps menu",
    'description': """
Hide apps menu for internal user no admin.
    """,
    'version': '0.1.1',
    'category': 'setting',
    'author': "nuxpy",
    'website': "https://www.nuxpy.com",
    'contributors': [
        'Félix Urbina <furbina@nuxpy.com>'
    ],
    'depends': [
        'base'
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'views/base_menus.xml',
    ],
    'license': 'LGPL-3',
    'support': 'soporte@nuxpy.com',
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
