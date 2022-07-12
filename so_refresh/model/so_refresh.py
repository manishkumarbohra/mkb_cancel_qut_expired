# Copyright 2020-22 Manish Kumar Bohra <manishkumarbohra@outlook.com>
# License LGPL-3 - See http://www.gnu.org/licenses/Lgpl-3.0.html

from odoo import api, fields, models


class SoReload(models.Model):
    _inherit = 'sale.order'

    def so_reload(self):
        """this method used to reload the sales order without reload webpage."""
        return {
            'type': 'ir.actions.client',
            'tag': 'trigger_reload'
        }
