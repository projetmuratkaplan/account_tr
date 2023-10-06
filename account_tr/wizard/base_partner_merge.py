from odoo import models

class BasePartnerMergeAutomaticWizard(models.TransientModel):
    _inherit = "base.partner.merge.automatic.wizard"

    def action_merge(self):
        """
        Customized action to handle partner merging with context injection.

        This method overrides the default behavior of merging partners.
        It injects a context to avoid the duplicate reference constraint that
        may arise when merging one contact with a reference in another contact
        without a reference.

        :return: Result of the original action_merge method with injected context.
        """
        # Injecting the context 'partner_ref_unique_merging' to prevent duplicate reference constraint
        return super(
            BasePartnerMergeAutomaticWizard,
            self.with_context(partner_ref_unique_merging=True),
        ).action_merge()
