from odoo.tests.common import TransactionCase

class TestResCompany(TransactionCase):
    def setUp(self):
        super().setUp()
        self.company = self.env.ref('base.main_company')

    def test_account_tr_default_value(self):
        self.assertEqual(self.company.account_tr, 'none', "Default value for account_tr should be 'none'")

    def test_write_method(self):
        # Positive test case
        self.company.write({'account_tr': 'all'})
        self.assertEqual(self.company.account_tr, 'all', "account_tr field should be updated to 'all'")

        # Negative test case
        with self.assertRaises(AssertionError):
            self.company.write({'account_tr': 'invalid_value'})