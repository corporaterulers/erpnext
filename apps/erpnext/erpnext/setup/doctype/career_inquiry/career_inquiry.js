frappe.ui.form.on("Career Inquiry", {
	years_of_experience(frm) {
		const val = frm.doc.years_of_experience;
		if (val && isNaN(parseFloat(val))) {
			frappe.msgprint("Years of Relevant Experience must be a number.");
			frm.set_value("years_of_experience", "");
		}
	}
});
