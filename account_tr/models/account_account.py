from odoo import models, fields, api

class AccountAccount(models.Model):
    _inherit = 'account.account'

    # Compute method to determine the specifier based on account_type
    @api.depends('account_type')
    def _compute_specifier(self):
        for account in self:
            if account.account_type.startswith('asset'):
                account.specifier = 'asset'
            elif account.account_type.startswith('income'):
                account.specifier = 'income'
            elif account.account_type.startswith('expense'):
                account.specifier = 'expense'
            else:
                account.specifier = False

    # Field to store the specifier
    specifier = fields.Selection([
        ('income', 'Income'),
        ('expense', 'Expense'),
        ('asset', 'Asset')
    ], "Type Specifier", compute="_compute_specifier", store=True, readonly=False)

# NOTE: This code defines a computed field "specifier" in the "account.account" model.
# The purpose of this field is to determine and store a specifier value ("asset", "income", or "expense")
# based on the account_type of the account. The specifier indicates the type of account for easy classification.
# The specifier is computed using the _compute_specifier method that uses the account_type field.
# The field is stored for performance and can be changed (readonly=False) by users if needed.

class AccountAccount(models.Model):
    _inherit = "account.account"

    account_type = fields.Selection(selection_add=[
        ("asset_check", "Check"),
        ("liability_tax", "Tax"),
        ("equity_cpl", "Current Profit & Loss"),
        ("expense_other", "Other"),
    ], ondelete={
        'asset_check': 'cascade',
        'liability_tax': 'cascade',
        'equity_cpl': 'cascade',
        'expense_other': 'cascade',
    })
