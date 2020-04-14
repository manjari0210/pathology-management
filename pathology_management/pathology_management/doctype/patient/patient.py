# -*- coding: utf-8 -*-
# Copyright (c) 2020, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import re
from frappe import _
from frappe.utils import validate_email_address
from frappe.model.document import Document

class Patient(Document):
	def validate(self):
		validate_email_address(self.email_id, True)
		self.validate_mobile_no()

	def validate_mobile_no(self):
		if not re.match("(^[+0-9]{1,3})*([0-9]{10,11}$)", self.mobile):
			frappe.throw(_("{0} is not a valid mobile no").format(self.mobile))

	def on_update(self):
		pass
