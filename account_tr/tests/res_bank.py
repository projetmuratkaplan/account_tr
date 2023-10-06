from odoo.tests.common import TransactionCase

class TestResBank(TransactionCase):
    def setUp(self):
        super().setUp()
        self.bank = self.env['res.bank'].create({
            'name': 'Test Bank',
            'eft_code': '1234',
        })

    def test_create_res_bank(self):
        self.assertEqual(self.bank.name, 'Test Bank')
        self.assertEqual(self.bank.eft_code, '1234')

    def test_update_res_bank(self):
        self.bank.name = 'Updated Bank'
        self.bank.eft_code = '5678'
        self.assertEqual(self.bank.name, 'Updated Bank')
        self.assertEqual(self.bank.eft_code, '5678')

    def test_invalid_eft_code(self):
        with self.assertRaises(ValueError):
            self.bank.eft_code = '12345'

    def test_blank_eft_code(self):
        self.bank.eft_code = ''
        self.assertEqual(self.bank.eft_code, '')

    def test_long_eft_code(self):
        with self.assertRaises(ValueError):
            self.bank.eft_code = '123456'