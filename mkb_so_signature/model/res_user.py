from odoo import api, fields, models


class ResPartnerSignature(models.Model):
    _inherit = 'res.users'

    user_signature = fields.Binary(string="User Signature")
