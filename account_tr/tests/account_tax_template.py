from odoo.tests.common import TransactionCase

class TestAccountTaxTemplate(TransactionCase):

    def test_get_tax_vals(self):
        # Positive test case
        company = self.env['res.company'].create({'name': 'Test Company'})
        tax_template = self.env['account.tax.template'].create({'name': 'Test Tax Template', 'code': 'TAX1', 'tax_rate': '10%', 'witholding_rate': '5%'})
        
        tax_template._get_tax_vals(company, {})  # Call the function to get the tax values
        
        tax = self.env['account.tax'].search([('name', '=', 'Test Tax Template')])  # Check if the tax record is created
        
        self.assertEqual(tax.code, 'TAX1')  # Assert that the code is set correctly
        self.assertEqual(tax.tax_rate, '10%')  # Assert that the tax rate is set correctly
        self.assertEqual(tax.witholding_rate, '5%')  # Assert that the withholding rate is set correctly

        # Negative test case
        company = self.env['res.company'].create({'name': 'Test Company'})
        tax_template = self.env['account.tax.template'].create({'name': 'Test Tax Template', 'code': 'TAX2'})
        
        tax_template._get_tax_vals(company, {})  # Call the function to get the tax values
        
        tax = self.env['account.tax'].search([('name', '=', 'Test Tax Template')])  # Check if the tax record is created
        
        self.assertEqual(tax.code, 'TAX2')  # Assert that the code is set correctly
        self.assertFalse(tax.tax_rate)  # Assert that the tax rate is not set
        self.assertFalse(tax.witholding_rate)  # Assert that the withholding rate is not set