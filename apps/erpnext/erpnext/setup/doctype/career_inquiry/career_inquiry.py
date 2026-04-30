import frappe
from frappe.model.document import Document


class CareerInquiry(Document):
	pass


@frappe.whitelist(allow_guest=True)
def submit_career_inquiry(
	first_name,
	last_name,
	email,
	phone_number,
	role_applying_for,
	years_of_experience,
	linkedin_profile_url,
	tell_us_about_yourself,
	resume_link=None,
	portfolio_site=None,
	how_did_you_hear=None,
	other_source=None,
):
	hear_value = how_did_you_hear
	other_value = other_source

	if how_did_you_hear and how_did_you_hear.startswith("Other:"):
		hear_value = "Other"
		other_value = how_did_you_hear[len("Other:"):].strip()

	doc = frappe.get_doc({
		"doctype": "Career Inquiry",
		"first_name": first_name,
		"last_name": last_name,
		"email": email,
		"phone_number": phone_number,
		"role_applying_for": role_applying_for,
		"years_of_experience": years_of_experience,
		"linkedin_profile_url": linkedin_profile_url,
		"tell_us_about_yourself": tell_us_about_yourself,
		"resume_link": resume_link,
		"portfolio_site": portfolio_site,
		"how_did_you_hear": hear_value,
		"other_source": other_value,
	})
	doc.insert(ignore_permissions=True)
	frappe.db.commit()

	return {"status": "success", "name": doc.name}
