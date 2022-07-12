# -*- coding: utf-8 -*-
# Copyright 2020-22 Manish Kumar Bohra <manishkumarbohra@outlook.com>
# License LGPL-3 - See http://www.gnu.org/licenses/Lgpl-3.0.html

{
    'name': 'Sales Order Revision',
    'version': '1.0.0',
    'summary': 'This module mainly used for the create a revised (Copy) order for the selected order',
    'description': 'This module mainly used for the create a revised (Copy) order for the selected order',
    'category': 'Sales',
    'author': 'Manish Bohra',
    'website': 'www.linkedin.com/in/manishkumarbohra',
    'maintainer': 'Manish Bohra',
    'support': 'manishkumarbohra@outlook.com',
    'sequence': '10',
    'license': 'LGPL-3',
    'depends': ['sale', 'sale_management'],
    'data': [
        'views/sales_revision.xml'],
    'images': ['static/description/revision.gif'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
