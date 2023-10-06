from odoo import fields, models

class ResCompany(models.Model):
    _inherit = "res.company"
    
    # Define a selection field for managing unique partner references
    account_tr = fields.Selection(
        selection=[
            ("none", "None"),
            ("companies", "Only companies"),
            ("all", "All partners"),
        ],
        string="Unique partner reference for",
        default="none",
    )
    
    def write(self, vals):
        """
        Override the write method to enforce constraint check in related partners.

        This method launches the constraint check manually on partners since the
        current ORM doesn't trigger the constraint on related fields.

        :param vals: Dictionary of field values to update.
        :return: Result of the original write method.
        """
        res = super().write(vals)
        
        # Check if 'account_tr' field is being updated
        if "account_tr" in vals:
            # Search for related partners using company_id
            partners = (
                self.env["res.partner"]
                .with_context(active_test=False)
                .search([("company_id", "in", [False] + self.ids)])
            )
            
            # Manually trigger the constraint check on related partners
            partners._check_ref()
        
        return res
