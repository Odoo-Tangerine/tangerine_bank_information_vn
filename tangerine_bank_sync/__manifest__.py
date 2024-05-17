# -*- coding: utf-8 -*-
{
    'name': 'Bank Vietnam Information',
    'summary': """Providing the latest API to synchronize banking information in Vietnam.""",
    'author': 'Long Duong Nhat',
    'category': 'Extra Tools',
    'support': 'odoo.tangerine@gmail.com',
    'version': '15.0.1.0',
    'post_init_hook': 'bank_information_sync',
    'depends': ['base',],
    'data': ['views/res_bank_views.xml'],
    'images': ['static/description/thumbnail.png'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}