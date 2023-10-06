from odoo.tests import common
from odoo.exceptions import ValidationError

class TestResPartner(common.TransactionCase):
    
    def test_check_ref_positive(self):
        # Positive test case with unique partner reference
        partner = self.env["res.partner"].create({"name": "Test Partner", "ref": "REF001"})
        partner._check_ref()  # No exception should be raised
    
    def test_check_ref_negative(self):
        # Negative test case with duplicate partner reference
        partner1 = self.env["res.partner"].create({"name": "Partner 1", "ref": "REF001"})
        partner2 = self.env["res.partner"].create({"name": "Partner 2", "ref": "REF001"})
        
        with self.assertRaises(ValidationError):
            partner2._check_ref()  # Should raise ValidationError
        
        # Negative test case with duplicate partner reference only within companies
        partner3 = self.env["res.partner"].create({"name": "Partner 3", "ref": "REF001", "is_company": True})
        partner4 = self.env["res.partner"].create({"name": "Partner 4", "ref": "REF001", "is_company": True})
        
        with self.assertRaises(ValidationError):
            partner4._check_ref()  # Should raise ValidationError