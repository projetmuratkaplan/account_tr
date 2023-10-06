**Functional Scenario Steps:**
1. Open the Odoo application and navigate to the desired module.
2. Locate the "Res Partner" model and understand that it has been extended to include additional functionality.
3. Note that a constraint method named "_check_ref" has been added to ensure the uniqueness of partner references within a defined scope.
4. Understand that the constraint method checks the uniqueness of the "ref" field within the selected scope, based on the "account_tr" field in the company settings.
5. Make changes to the "ref" field in a partner record.
6. Save the changes.

**Expected Results:**
- The "_check_ref" method will be triggered when the "ref" field is updated.
- The method will check the uniqueness of the partner reference within the selected scope.
- If a duplicate partner reference is found within the scope, a validation error will be raised.
- The error message will indicate that the reference is equal to another partner's reference.
- The changes will not be saved until a unique partner reference is entered.
