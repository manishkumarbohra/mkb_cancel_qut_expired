# Copyright 2020-22 Manish Kumar Bohra <manishkumarbohra@outlook.com>
# License LGPL-3 - See http://www.gnu.org/licenses/Lgpl-3.0.html

{
    'name': 'User Signature in Sale/Quotation Reports',
    'version': '1.0.0',
    'summary': 'This app add User Signature in Sale/Quotation Reports',
    'description': 'This app add User Signature in Sale/Quotation Reports',
    'category': 'Sales',
    'author': 'Manish Bohra',
    'website': 'www.linkedin.com/in/manishkumarbohra',
    'maintainer': 'Manish Bohra',
    'support': 'manishkumarbohra@outlook.com',
    'sequence': '10',
    'license': 'LGPL-3',
    "data": [
        'views/res_users.xml',
        'report/sale_report_templates.xml',
    ],
    'images': ['static/description/bulk.gif'],
    'depends': ['base', 'sale', 'sale_management'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
