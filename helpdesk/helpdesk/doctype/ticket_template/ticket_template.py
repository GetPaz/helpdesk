# Copyright (c) 2022, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TicketTemplate(Document):
	def validate(self):
		allowed_field_types = ['Data', 'Link']

		for custom_field in self.custom_fields:
			if custom_field.fieldtype not in allowed_field_types:
				frappe.throw(f'Type {custom_field.fieldtype} not allowed, should be in {allowed_field_types}')