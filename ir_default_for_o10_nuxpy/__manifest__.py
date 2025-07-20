# -*- coding: utf-8 -*-
{
    'name': "ir_default for Ov10",
    'summary': "ir_default for Odoo v10",
    'description': """
This module creates an ir_default table/model like ir_default Odoo v18 into Odoo v10.

This module is part of the tools for migrating from Odoo version 10 to Odoo version 18.
    """,
    'author': "nuxpy",
    'website': "https://www.nuxpy.com",
    'contributors': [
        'Félix Urbina <furbina@nuxpy.com>'
    ],
    'category': 'Uncategorized',
    'version': '20250712.1926',
    'depends': ['base'],
    'data': [
        'security/base_groups.xml',
        'security/ir.model.access.csv',
        'views/ir_default_views.xml',
    ],
    'license': 'LGPL-3',
}

