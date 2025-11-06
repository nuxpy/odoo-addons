# -*- coding: utf-8 -*-
{
    'name': "Git Odoo Addons",
    'summary': "Get Odoo Addons from Git Repositories",
    'description': """
This module allows you to import modules from free repositories like OCA or others via Git.
    """,
    'version': '0.1.2',
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
        'security/ir.model.access.csv',
        'views/git_repository_views.xml',
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
