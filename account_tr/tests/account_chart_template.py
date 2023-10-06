from odoo.tests import common

class TestAccountChartTemplate(common.TransactionCase):

    def setUp(self):
        super(TestAccountChartTemplate, self).setUp()
        self.account_chart_template = self.env['account.chart.template']

    def test__add_custom_journals(self):
        # Positive test case
        company = self.env['res.company'].create({'name': 'Test Company'})
        self.account_chart_template._add_custom_journals(company)
        journals = self.env['account.journal'].search([('company_id', '=', company.id)])
        self.assertEqual(len(journals), 3)

        # Negative test case
        self.account_chart_template._add_custom_journals(False)
        journals = self.env['account.journal'].search([('company_id', '=', False)])
        self.assertEqual(len(journals), 0)

    def test__create_journal_if_not_exists(self):
        # Positive test case
        company = self.env['res.company'].create({'name': 'Test Company'})
        journal_data = {'code': 'TEST', 'name': 'Test Journal', 'type': 'general'}
        self.account_chart_template._create_journal_if_not_exists(company, journal_data)
        journal = self.env['account.journal'].search([('code', '=', 'TEST'), ('company_id', '=', company.id)])
        self.assertTrue(journal)

        # Negative test case
        self.account_chart_template._create_journal_if_not_exists(False, journal_data)
        journal = self.env['account.journal'].search([('code', '=', 'TEST'), ('company_id', '=', False)])
        self.assertFalse(journal)

    def test__load(self):
        # Positive test case
        company = self.env['res.company'].create({'name': 'Test Company'})
        self.account_chart_template._load(company)
        journals = self.env['account.journal'].search([('company_id', '=', company.id)])
        self.assertEqual(len(journals), 3)

        # Negative test case
        self.account_chart_template._load(False)
        journals = self.env['account.journal'].search([('company_id', '=', False)])
        self.assertEqual(len(journals), 0)


class TestAccountAccountTemplate(common.TransactionCase):

    def setUp(self):
        super(TestAccountAccountTemplate, self).setUp()
        self.account_account_template = self.env['account.account.template']

    def test_account_type(self):
        # Positive test case
        account = self.account_account_template.create({
            'name': 'Test Account',
            'code': 'TEST',
            'user_type_id': self.ref('account.data_account_type_current_assets'),
            'account_type': 'asset_check'
        })
        self.assertEqual(account.account_type, 'asset_check')

        # Negative test case
        with self.assertRaises(ValidationError):
            self.account_account_template.create({
                'name': 'Test Account',
                'code': 'TEST',
                'user_type_id': self.ref('account.data_account_type_current_assets'),
                'account_type': 'invalid_type'
            })