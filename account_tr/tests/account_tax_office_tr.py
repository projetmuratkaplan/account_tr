from odoo.tests import common
from lxml import etree
import logging
from odoo.addons.base.models.ir_model import MODULE_UNINSTALL_FLAG

# Initialize logger for the module
logger = logging.getLogger(__name__)

class TestAccountTaxOffice(common.TransactionCase):
    def test_unlink(self):
        # Create test data
        tax_office = self.env['account.tax.office'].create({
            'name': 'Test Tax Office',
            'code': '123',
        })

        # Call the unlink method
        tax_office.unlink()

        # Assert that the tax office is not deleted
        self.assertTrue(tax_office.exists())

    def test_turkey_tax_office_ebyn_import(self):
        # Create test XML file string
        xml_file_string = """
            <root>
                <vergidairesi>
                    <vdad>Test Tax Office</vdad>
                    <vdkod>123</vdkod>
                </vergidairesi>
            </root>
        """

        # Call the turkey_tax_office_ebyn_import method
        self.env['account.tax.office'].turkey_tax_office_ebyn_import(xml_file_string)

        # Assert that the tax office is imported correctly
        tax_office = self.env['account.tax.office'].search([('code', '=', '123')])
        self.assertTrue(tax_office.exists())
        self.assertEqual(tax_office.name, 'Test Tax Office')