# -*- coding: utf-8 -*-
# Copyright 2020-22 Manish Kumar Bohra <manishkumarbohra@outlook.com>
# License LGPL-3 - See http://www.gnu.org/licenses/Lgpl-3.0.html
{
    'name': 'Order Line Editable',
    'version': '1.0',
    'summary': 'This module allows order line editable top',
    'description': 'This module allows order line editable top',
    'category': 'Sales',
    'author': 'Manish Bohra',
    'website': 'www.linkedin.com/in/manishkumarbohra',
    'maintainer': 'Manish Bohra',
    'support': 'manishkumarbohra@outlook.com',
    'sequence': '10',
    'license': 'LGPL-3',
    "data": [
        'security/sales_security.xml',
        'views/res_configuration.xml',
        'views/sales_views.xml',
    ],
    'images': ['static/description/ole.gif'],
    'depends': ['base', 'sale', 'sales_team', 'sale_management'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
