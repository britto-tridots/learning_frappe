# Copyright (c) 2025, Brit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Learning(Document):
	def before_save(self):
		self.name1 = "Brit"
		frappe.log_error("Error",{self.name1})

