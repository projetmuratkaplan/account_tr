from odoo import models, fields


class AccountChartTemplate(models.Model):
    _inherit = "account.chart.template"

    def _load(self, company):
        res = super(AccountChartTemplate, self)._load(company)
        if company.chart_template_id == self.env.ref("account_tr.l10ntr_tek_duzen_hesap"):
            journals = [
                {'code': 'DEVIR', 'name': 'Devir', 'type': 'general'},
                {'code': 'ACLS', 'name': 'Açılış Yevmiyesi', 'type': 'general'},
                {'code': 'KPNS', 'name': 'Kapanış Yevmiyesi', 'type': 'general'},
            ]
            for journal in journals:
                company_journal = self.env['account.journal'].search([
                    ('code', '=', journal.get('code')),
                    ('company_id', '=', company.id),
                ], limit=1)
                if not company_journal:
                    self.env['account.journal'].sudo().create({
                        'name': journal.get('name'),
                        'code': journal.get('code'),
                        'type': journal.get('type'),
                        'company_id': company.id,
                    })
        return res


class AccountAccountTemplate(models.Model):
    _inherit = "account.account.template"

    account_type = fields.Selection(selection_add=[
        ("asset_check", "Check"),
        ("liability_tax", "Tax"),
        ("equity_cpl", "Term Profit & Loss"),
        ("expense_other", "Other"),
    ], ondelete={
        'asset_check': 'cascade',
        'liability_tax': 'cascade',
        'equity_cpl': 'cascade',
        'expense_other': 'cascade',
    })
