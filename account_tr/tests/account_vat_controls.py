from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestAccountTaxTemplate(TransactionCase):
    def test_get_tax_vals(self):
        # Positive test case
        company = self.env['res.company'].create({'name': 'Test Company'})
        tax_template = self.env['account.tax.template'].create({
            'name': 'Test Tax Template',
            'code': 'TAX1',
            'tax_rate': '10%',
            'withholding_rate': '5%'
        })
        tax_template._get_tax_vals(company, {})  # Call the function to get the tax values
        tax = self.env['account.tax'].search([('name', '=', 'Test Tax Template')])  # Check if the tax record is created
        self.assertEqual(tax.code, 'TAX1')  # Assert that the code is set correctly
        self.assertEqual(tax.tax_rate, '10%')  # Assert that the tax rate is set correctly
        self.assertEqual(tax.withholding_rate, '5%')  # Assert that the withholding rate is set correctly

        # Negative test case
        company = self.env['res.company'].create({'name': 'Test Company'})
        tax_template = self.env['account.tax.template'].create({
            'name': 'Test Tax Template',
            'code': 'TAX2'
        })
        tax_template._get_tax_vals(company, {})  # Call the function to get the tax values
        tax = self.env['account.tax'].search([('name', '=', 'Test Tax Template')])  # Check if the tax record is created
        self.assertEqual(tax.code, 'TAX2')  # Assert that the code is set correctly
        self.assertFalse(tax.tax_rate)  # Assert that the tax rate is not set
        self.assertFalse(tax.withholding_rate)  # Assert that the withholding rate is not set

    def test_check_vat_unique(self):
        # Test case for _check_vat_unique method
        partner1 = self.env['res.partner'].create({'name': 'Partner 1', 'vat': 'TR1234567890'})
        partner2 = self.env['res.partner'].create({'name': 'Partner 2', 'vat': 'TR1234567890'})
        with self.assertRaises(ValidationError):
            partner2.write({'vat': 'TR1234567890'})

    def test_check_vat_tr(self):
        # Test case for check_vat_tr method
        valid_vat_number = 'TR1234567890'
        invalid_vat_number = 'TR123456789'
        result_valid = self.env['res.partner'].check_vat_tr(valid_vat_number)
        result_invalid = self.env['res.partner'].check_vat_tr(invalid_vat_number)
        self.assertTrue(result_valid)
        self.assertFalse(result_invalid)