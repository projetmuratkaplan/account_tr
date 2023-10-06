import os
import urllib
from lxml import etree
from odoo.api import Environment, SUPERUSER_ID

from . import models
from . import wizard


def post_init_hook(cr, registry):
    env = Environment(cr, SUPERUSER_ID, {})

    file_path = os.path.dirname(os.path.realpath(__file__))
    file = urllib.parse.urljoin('file:', os.path.join(file_path, 'data', 'tax_offices_tr.xml'))
    root = etree.parse(file).getroot()
    xml_string = etree.tostring(root, pretty_print=True, encoding='unicode')

    env['account.tax.office'].turkey_tax_office_ebyn_import(xml_string)
