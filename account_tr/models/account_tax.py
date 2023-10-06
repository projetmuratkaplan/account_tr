from odoo import models, fields, api

# Extending the Account Tax model
class AccountTax(models.Model):
    _inherit = 'account.tax'

    # Adding a custom field for Tax Code
    code = fields.Char('Tax Code', size=64)

# Extending the Account Tax Template model
class AccountTaxTemplate(models.Model):
    _inherit = 'account.tax.template'

    # Adding a custom field for Tax Code
    code = fields.Char('Tax Code', size=64)

    # Customizing the _generate_tax method to set tax codes
    @api.model
    def _generate_tax(self, company, accounts_exist=False):
        result = super(AccountTaxTemplate, self)._generate_tax(company, accounts_exist)
        for template_id, tax_id in result['tax_template_to_tax'].items():
            tax_id.code = template_id.code
        return result

# Defining a model for Tax Office
class AccountTaxOffice(models.Model):
    _description = "Tax Office"
    _name = 'account.tax.office'

    # Fields for the Tax Office model
    active = fields.Boolean('Active', default=True)
    name = fields.Char('Tax Office Name', required=True)
    code = fields.Char('Tax Office Code', size=6, required=True)
    state_id = fields.Many2one('res.country.state', 'State', required=True)
    _order = "state_id"

# Extending the Partner model
class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Adding a Many2one field to link to Tax Office
    tax_office_id = fields.Many2one('account.tax.office', 'Tax Office', ondelete='restrict')

# Extending the Company model
class ResCompany(models.Model):
    _inherit = "res.company"

    # Adding a related field for Tax Office
    tax_office_id = fields.Many2one("account.tax.office", related='partner_id.tax_office_id', string="Tax Office", readonly=False)

    # Customizing create and write methods to update related partner's Tax Office
    @api.model
    def create(self, vals):
        new_company = super(ResCompany, self).create(vals)

        if vals.get('tax_office_id'):
            new_company.partner_id.write({'tax_office_id': vals.get('tax_office_id')})
        return new_company

    def write(self, values):
        if values.get('tax_office_id'):
            self.partner_id.write({'tax_office_id': values.get('tax_office_id')})
        return super(ResCompany, self).write(values)
