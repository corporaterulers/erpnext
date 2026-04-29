import frappe


def execute():
	doctypes = ["Career Inquiry"]
	for doctype in doctypes:
		if frappe.db.exists("DocType", doctype):
			frappe.reload_doctype(doctype)
