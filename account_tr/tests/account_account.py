from odoo.tests import common
from odoo.exceptions import ValidationError

class TestAccountAccount(common.TransactionCase):

    def setUp(self):
        super(TestAccountAccount, self).setUp()
        self.AccountAccount = self.env['account.account']
        self.account1 = self.AccountAccount.create({
            'name': 'Test Account 1',
            'account_type': 'asset',
        })
        self.account2 = self.AccountAccount.create({
            'name': 'Test Account 2',
            'account_type': 'income',
        })
        self.account3 = self.AccountAccount.create({
            'name': 'Test Account 3',
            'account_type': 'expense',
        })

    def test_compute_specifier(self):
        """
        Test the _compute_specifier method
        """
        self.assertEqual(self.account1.specifier, 'asset', "Account 1 specifier should be 'asset'")
        self.assertEqual(self.account2.specifier, 'income', "Account 2 specifier should be 'income'")
        self.assertEqual(self.account3.specifier, 'expense', "Account 3 specifier should be 'expense'")

    def test_account_type(self):
        """
        Test the account_type field
        """
        # Positive test case
        self.account1.account_type = 'asset_check'
        self.assertEqual(self.account1.account_type, 'asset_check', "Account 1 type should be 'asset_check'")
        
        # Negative test case
        with self.assertRaises(ValidationError):
            self.account1.account_type = 'invalid_type'