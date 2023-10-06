**Functional Scenario Steps:**
1. Open the Odoo application and navigate to the "Settings" module.
2. Locate the "Companies" section and select the desired company record.
3. Scroll down to find the "Unique partner reference for" field.
4. Observe the available options in the dropdown menu.
5. Select one of the options: "None", "Only companies", or "All partners".
6. Save the changes.

**Expected Results:**
- The "Unique partner reference for" field will be visible on the company form.
- The dropdown menu will display the available options: "None", "Only companies", and "All partners".
- Users can select one of the options to manage the unique partner references for the company.
- The selected option will be associated with the company record.

7. Understand that the "write" method of the "ResCompany" model has been overridden.
8. Note that the overridden method enforces a constraint check on related partners when the "account_tr" field is updated.
9. Make changes to the "account_tr" field in the company record.
10. Save the changes.

**Expected Results:**
- The overridden "write" method will be triggered when the "account_tr" field is updated.
- The method will perform a constraint check on the related partners of the company.
- If any constraint violations are found, appropriate actions will be taken.
- The result of the original "write" method will be returned.
