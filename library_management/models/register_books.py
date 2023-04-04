from odoo import models, fields, api

class RegisterBooks(models.Model):
	_name = 'register.books'
	# _rec_name = "book_detail_id"

	book_detail_id = fields.Many2one('book.details',string='Book Name')
	empty_id = fields.Many2one("issue.book")
	issue_quantity = fields.Integer(string="Issue Quantity")