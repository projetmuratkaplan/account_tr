from odoo import _, api, models
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = "res.partner"
    
    @api.constrains("ref", "is_company", "company_id")
    def _check_ref(self):
        """
        Constraint method to ensure unique partner reference within defined scope.

        This method checks the uniqueness of partner reference within the selected scope
        (defined by 'account_tr' field in the company settings).

        :raises: ValidationError if duplicate partner reference is found.
        """
        for partner in self.filtered("ref"):
            # If the company is not defined in the partner, use the current user's company
            company = partner.company_id or self.env.company
            mode = company.account_tr
            
            # Check if reference uniqueness should be enforced based on the mode
            if mode == "all" or (mode == "companies" and partner.is_company):
                domain = [
                    ("id", "!=", partner.id),
                    ("ref", "=", partner.ref),
                ]
                if mode == "companies":
                    domain.append(("is_company", "=", True))
                other = self.search(domain)
                
                # Don't raise when coming from contact merge wizard or no duplicates
                if other and not self.env.context.get("partner_ref_unique_merging"):
                    raise ValidationError(
                        _("This reference is equal to partner '%s'")
                        % other[0].display_name
                    )
