# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Licence Extension',
    'version' : '0.1',
    'summary': 'Licence Extension',
    'sequence': 10,
    'description': """
        Integration with NetSuite
    """,
    'category': 'Purchase/Billing',
    'website': '',
    'images' : [],
    'depends': [],
    'data': [
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/licence.xml",
        "menu.xml",
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
