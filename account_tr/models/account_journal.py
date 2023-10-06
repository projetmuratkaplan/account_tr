from odoo import models, fields, api

class AccountJournal(models.Model):
    _inherit = 'account.journal'

    @api.model
    def _get_payment_subtype(self):
        return []

    payment_subtype = fields.Selection('_get_payment_subtype', string='Payment Subtype')
