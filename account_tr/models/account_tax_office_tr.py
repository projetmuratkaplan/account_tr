from lxml import etree
import logging

from odoo import models, api
from odoo.addons.base.models.ir_model import MODULE_UNINSTALL_FLAG

# Initialize logger for the module
logger = logging.getLogger(__name__)

class AccountTaxOffice(models.Model):
    _inherit = 'account.tax.office'

    # Overriding unlink method to prevent deletion during uninstallation
    def unlink(self):
        if not self.env.context.get(MODULE_UNINSTALL_FLAG, False):
            super(AccountTaxOffice, self).unlink()

    # Custom method to import tax office data from XML
    def turkey_tax_office_ebyn_import(self, xml_file_string):
        try:
            # Create an XML parser with recovery mode
            parser = etree.XMLParser(recover=True)
            xml_root = etree.fromstring(xml_file_string, parser)
            namespaces = xml_root.nsmap

            # Extract tax offices from XML and process each office
            tax_offices = xml_root.xpath("//vergidairesi", namespaces=namespaces)
            for tax_office in tax_offices:
                tax_name = tax_office.xpath("vdad", namespaces=namespaces)[0].text

                if tax_name:
                    # Modify tax office name for abbreviation
                    tax_name = tax_name.replace('MAL MÜDÜRLÜĞÜ', 'MAL.MD.')
                    tax_name = tax_name.replace('VERGİ DAİRESİ', 'V.D.')
                    tax_name = tax_name.replace('MÜDÜRLÜĞÜ', 'MD.')
                    tax_name = tax_name.replace('BAŞKANLIĞI', 'BŞK.')

                tax_code = tax_office.xpath("vdkod", namespaces=namespaces)[0].text
                country_code = tax_code[1:3] if tax_code else False

                # Find the corresponding country state for the tax office
                country_state = self.env['res.country.state'].search([
                    ('country_id.code', '=', 'TR'),
                    ('code', '=', country_code)
                ], limit=1)

                # Search for existing tax office or create a new one
                tax_office_model = self.search([
                    ('code', '=', tax_code),
                ])
                if tax_office_model.exists():
                    tax_office_model.write({
                        'name': tax_name,
                        'state_id': country_state.id if country_state else False
                    })
                else:
                    self.create({
                        'name': tax_name,
                        'code': tax_code,
                        'state_id': country_state.id if country_state else False
                    })

        except BaseException as e:
            logger.error('Account Tax Office Import XML Error: ' + str(e))
