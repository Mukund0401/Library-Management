from odoo import models, fields, api

class RegisterDate(models.Model):
	_name = "register.date"

	entry_id = fields.Integer(string="Entry Id")
	book_id = fields.Char(string="Book Id",readonly=True)
	book_name = fields.Char(string="Book",readonly=True)
	# test_ids = fields.One2many('issue.book','books_line_ids')
	issuing_date = fields.Char(string="Issue Date",readonly=True)
	return_date = fields.Char(string="Return Date",readonly=True)
	deadline_date = fields.Date(string='Deadline Date', readonly=True)
	# issue_quantity = fields.Integer(string='Issue Quantity')


	# _sql_constraints = [('xyz', 'unique(entry_id)', 'xyz')]
	
