**Functional Scenario Steps:**
1. Open the Odoo application and navigate to the "Accounting" module.
2. Locate the "Account Tax" model and understand that it has been extended to include additional functionality.
3. Note that a new field called "Tax Code" has been added to the "Account Tax" model.
4. This field allows users to enter a custom tax code for each tax.
5. Open the desired tax record.
6. Scroll down to find the "Tax Code" field.
7. Enter the desired tax code.
8. Save the changes.

**Expected Results:**
- The "Tax Code" field will be visible on the tax form.
- Users can enter a custom tax code for each tax.
- The entered tax code will be associated with the tax record.

9. Locate the "Account Tax Template" model and understand that it has been extended to include additional functionality.
10. Note that a new field called "Tax Code" has been added to the "Account Tax Template" model.
11. This field allows users to enter a custom tax code for each tax template.
12. Open the desired tax template record.
13. Scroll down to find the "Tax Code" field.
14. Enter the desired tax code.
15. Save the changes.

**Expected Results:**
- The "Tax Code" field will be visible on the tax template form.
- Users can enter a custom tax code for each tax template.
- The entered tax code will be associated with the tax template record.

16. Understand that a new model called "Tax Office" has been defined.
17. This model represents a tax office and contains fields such as "Active", "Tax Office Name", "Tax Office Code", and "State".
18. Open the desired tax office record.
19. Fill in the required information such as tax office name, tax office code, and state.
20. Save the changes.

**Expected Results:**
- The tax office record will be created with the provided information.
- The tax office will be marked as active.
- The tax office will be associated with the specified state.

21. Locate the "Partner" model and understand that it has been extended to include additional functionality.
22. Note that a new field called "Tax Office" has been added to the "Partner" model as a Many2one field.
23. This field allows users to link a partner to a specific tax office.
24. Open the desired partner record.
25. Scroll down to find the "Tax Office" field.
26. Select the appropriate tax office from the dropdown menu.
27. Save the changes.

**Expected Results:**
- The "Tax Office" field will be visible on the partner form.
- Users can select a tax office from the dropdown menu to link it to the partner.
- The selected tax office will be associated with the partner record.

28. Understand that the "Company" model has been extended to include additional functionality.
29. Note that a related field called "Tax Office" has been added to the "Company" model.
30. This field is linked to the "Tax Office" field of the related partner.
31. Open the desired company record.
32. Scroll down to find the "Tax Office" field.
33. Select the appropriate tax office from the dropdown menu.
34. Save the changes.

**Expected Results:**
- The "Tax Office" field will be visible on the company form.
- Users can select a tax office from the dropdown menu to link it to the company.
- The selected tax office will be associated with the company record.
- If the tax office is changed, the related partner's tax office will also be updated.
