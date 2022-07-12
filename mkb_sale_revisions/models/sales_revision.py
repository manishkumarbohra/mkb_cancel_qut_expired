# -*- coding: utf-8 -*-
# Copyright 2020-22 Manish Kumar Bohra <manishkumarbohra@outlook.com>
# License LGPL-3 - See http://www.gnu.org/licenses/Lgpl-3.0.html
from odoo import api, fields, models


class SalesOrderRevision(models.Model):
    _inherit = 'sale.order'

    source_doc_id = fields.Many2one(comodel_name="sale.order", string="Source ID", readonly=True)

    child_order_ids = fields.Many2many(comodel_name="sale.order", relation="sale_child_order_ids", column1="id",
                                       column2="name", string="Child Order", )
    revision_count = fields.Integer(string='Revise Count', compute='_get_revised', readonly=True)
    is_revised_order = fields.Boolean(string="Is Revised Order", readonly=True)

    @api.depends('child_order_ids')
    def _get_revised(self):
        for order in self:
            order.revision_count = len(order.child_order_ids.ids)

    def sales_order_revision(self):
        for res in self:
            revision = res.copy()
            revision.update({'origin': res.name,
                             'source_doc_id': res.id,
                             'is_revised_order': True
                             })
            order_objects = res.search([('source_doc_id', '!=', False), ('source_doc_id', '=', res.id)])
            if not res.source_doc_id:
                res.update({'child_order_ids': [(6, 0, order_objects.ids)],
                            })
            revision.update({'name': res.name + '/' + str(len(res.child_order_ids))})

    def action_view_revise_order(self):
        revise = self.mapped('child_order_ids')
        action = self.env.ref('sale.action_quotations_with_onboarding').read()[0]
        if len(revise) > 1:
            action['domain'] = [('id', 'in', revise.ids)]
        elif len(revise) == 1:
            form_view = [(self.env.ref('sale.view_order_form').id, 'form')]
            if 'views' in action:
                action['views'] = form_view + [(state, view) for state, view in action['views'] if view != 'form']
            else:
                action['views'] = form_view
            action['res_id'] = revise.id
        else:
            action = {'type': 'ir.actions.act_window_close'}
        return action
