from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    # New field to store VAT number
    vat = fields.Char(copy=False)
    
    # Whitelisted VAT numbers
    whitelisted = [
        'TR1234567890',
        'TR1111111111',
        'TR2222222222',
        'TR3333333333',
        'TR5555555555',
        'TR7330396679',
        'TR8888888001',
        'TR8888888888',
        'TR9999999999',
        'TR11111111111',
        'TR12345678901',
        'TR12345678950',
    ]

    # Constrain to check uniqueness of VAT number
    @api.constrains('vat')
    def _check_vat_unique(self):
        for record in self:
            if record.parent_id or not record.vat:
                continue
            if record.vat in self.whitelisted:
                continue
            
            domain = [('vat', '=', record.vat)]
            if record.id:
                domain.append(('id', '!=', record.id))
            
            existing_partner = self.search(domain, limit=1)
            if existing_partner:
                raise ValidationError(
                    _("The VAT %s already exists in another partner.") % record.vat
                )

    def check_vat_tr(self, vat):
        """
        Custom VAT (Value Added Tax) number validation logic for Turkey.
        This method checks both VAT numbers (Vergi No) and personal identification numbers (TC Kimlik No).
        """
        # Check the length of the VAT number
        if not (10 <= len(vat) <= 11):
            return False
        
        try:
            int(vat)
        except ValueError:
            return False
        
        # List of known valid VAT numbers
        valid_vat_numbers = (
            '1234567890',
            '1111111111',
            '2222222222',
            '3333333333',
            '5555555555',
            '8888888001',
            '8888888888',
            '9999999999',
            '11111111111',
            '12345678950',
            '12345678901',
        )
        
        # Check if the VAT number is in the list of valid VAT numbers
        if vat in valid_vat_numbers:
            return True
        else:
            if len(vat) == 10:
                sum = 0
                check = 0
                # Calculate the check digit for VAT number
                for f in range(0, 9):
                    c1 = (int(vat[f]) + (9 - f)) % 10
                    c2 = (c1 * (2 ** (9 - f))) % 9
                    if (c1 != 0) and (c2 == 0):
                        c2 = 9
                    sum += c2
                if sum % 10 == 0:
                    check = 0
                else:
                    check = 10 - (sum % 10)
                return int(vat[9]) == check
            elif len(vat) == 11:
                c1a = 0
                c1b = 0
                c2 = 0
                # Calculate the check digits for personal identification numbers
                for f in range(0, 9, 2):
                    c1a += int(vat[f])
                for f in range(1, 9, 2):
                    c1b += int(vat[f])
                c1 = ((7 * c1a) - c1b) % 10
                for f in range(0, 10):
                    c2 += int(vat[f])
                c2 = c2 % 10
                return int(vat[9]) == c1 and int(vat[10]) == c2

