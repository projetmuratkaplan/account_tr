import base64

from odoo import fields, models

class AccountTaxOfficeImport(models.TransientModel):
    _name = 'account.tax.office.import'
    _description = 'Account Tax Office Import'

    # Binary field to upload XML file
    xml_file = fields.Binary('Tax Office XML', required=True)

    # Method to perform XML import
    def import_xml(self):
        # Decode the binary XML file
        xml_file_string = base64.decodebytes(self.xml_file)

        # Access the Account Tax Office model
        account_tr = self.env['account.tax.office']

        # Call the custom method to import data from the XML file
        account_tr.turkey_tax_office_ebyn_import(xml_file_string)
