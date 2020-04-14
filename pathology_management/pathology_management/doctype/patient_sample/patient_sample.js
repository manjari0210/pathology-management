// Copyright (c) 2020, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Patient Sample', {
	setup: function(frm) {
		frappe.meta.get_docfield("Test","result", frm.doc.name).read_only = 1;
	}
});
