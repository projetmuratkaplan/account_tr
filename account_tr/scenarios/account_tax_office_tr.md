**Functional Scenario Steps:**
1. Open the Odoo application and navigate to the "Accounting" module.
2. Locate the "Account Tax Office" model and understand that it has been extended to include additional functionality.
3. The added functionality prevents the deletion of tax offices during module uninstallation.
4. There is a custom method named "turkey_tax_office_ebyn_import" to import tax office data from an XML file.
5. Obtain an XML file containing tax office data in the required format.
6. Open the desired tax office record.
7. Scroll down to find the "Turkey Tax Office EBYN Import" button.
8. Click on the button to initiate the import process.
9. Select the XML file containing the tax office data.
10. Confirm the import.

**Expected Results:**
- The "Turkey Tax Office EBYN Import" button will be visible on the tax office form.
- Clicking on the button will prompt the user to select an XML file for import.
- The XML file should contain tax office data in the specified format.
- The import process will parse the XML file and extract tax office information.
- Each tax office will be processed individually.
- The tax office name will be modified for abbreviation purposes.
- The corresponding country state for the tax office will be determined.
- If an existing tax office with the same code exists, it will be updated with the new information.
- If no existing tax office is found, a new tax office will be created.
- Any errors encountered during the import process will be logged.
