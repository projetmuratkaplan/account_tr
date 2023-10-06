from odoo.tests import common

class TestAccountJournal(common.TransactionCase):

    def test_get_payment_subtype(self):
        journal = self.env['account.journal']
        payment_subtype = journal._get_payment_subtype()
        self.assertEqual(payment_subtype, [])

    def test_get_payment_subtype_with_values(self):
        journal = self.env['account.journal']
        # Add test cases with different values for payment subtype
        pass

    def test_payment_subtype(self):
        journal = self.env['account.journal']
        journal.payment_subtype = 'subtype1'
        self.assertEqual(journal.payment_subtype, 'subtype1')

    def test_payment_subtype_invalid_value(self):
        journal = self.env['account.journal']
        with self.assertRaises(ValueError):
            journal.payment_subtype = 'invalid_subtype'