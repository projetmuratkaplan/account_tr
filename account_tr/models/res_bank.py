from odoo import models, fields

class ResBank(models.Model):
    # Inheriting the 'res.bank' model
    _inherit = "res.bank"
    
    # Adding a new field for EFT code
    eft_code = fields.Char(string='EFT Code', size=4)
