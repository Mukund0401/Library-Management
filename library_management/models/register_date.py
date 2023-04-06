from odoo import models, fields, api

class RegisterDate(models.Model):
	_name = "register.date"

	book_id = fields.Integer(string="Book Id",readonly=True)
	book_name = fields.Char(string="Book",readonly=True)
	issuing_date = fields.Char(string="Issue Date",readonly=True)
	return_date = fields.Char(string="Return Date",readonly=True)

	
