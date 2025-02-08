# Copyright (c) 2025, Hardik and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def before_save(self):
		self.total_amount = self.price_per_km * self.estimated_km + sum([i.amount for i in self.services] or [])
