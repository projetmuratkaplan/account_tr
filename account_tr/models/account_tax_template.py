from odoo import models, fields

class AccounTaxTemplate(models.Model):
    _inherit = 'account.tax.template'

    tax_rate = fields.Char("Tax Rate", help="Electronic Declaration Field")
    witholding_rate = fields.Char("Witholding Rate", help="Electronic Declaration Field")

    def _get_tax_vals(self, company, tax_template_to_tax):
        val = super(AccounTaxTemplate, self)._get_tax_vals(company, tax_template_to_tax)
        val.update({
            'code': self.code,
            'tax_rate': self.tax_rate,
            'witholding_rate': self.witholding_rate
        })
        return val


class AccounTax(models.Model):
    _inherit = 'account.tax'

    tax_rate = fields.Char("Tax Rate", help="Electronic Declaration Field")
    witholding_rate = fields.Char("Witholding Rate", help="Electronic Declaration Field")
