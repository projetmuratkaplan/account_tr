**Functional Scenario Steps:**
1. Open the Odoo application and navigate to the "Contacts" module.
2. Locate the desired partner record.
3. Scroll down to find the "VAT Number" field.
4. Enter the VAT number for the partner.
5. Save the changes.

**Expected Results:**
- The "VAT Number" field will be visible on the partner form.
- Users can enter the VAT number for the partner.
- The entered VAT number will be associated with the partner record.

6. Understand that there is a constraint to check the uniqueness of the VAT number.
7. If the entered VAT number already exists in another partner record, an error message will be displayed.
8. Try entering a VAT number that already exists in another partner record.
9. Save the changes.

**Expected Results:**
- An error message will be displayed stating that the entered VAT number already exists in another partner record.
- The changes will not be saved until a unique VAT number is entered.

10. Note that there is a custom VAT number validation logic specific to Turkey.
11. This logic checks both VAT numbers (Vergi No) and personal identification numbers (TC Kimlik No).
12. Understand that the validation logic includes length checks, digit checks, and check digit calculations.
13. Use the provided "check_vat_tr" method to validate a VAT number.
14. Pass a VAT number as a parameter to the "check_vat_tr" method.
15. Observe the return value of the method to determine if the VAT number is valid.

**Expected Results:**
- The "check_vat_tr" method will return True if the VAT number is valid according to the Turkish VAT number validation logic.
- The method will return False if the VAT number is not valid.

Please note that the default language for the conversation is English unless a specific language is mentioned.