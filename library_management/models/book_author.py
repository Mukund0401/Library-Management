from odoo import models, fields, api

class BookAuthor(models.Model):
	_name = "book.author"
	_rec_name ="author_name"

	author_name = fields.Char(string="Author Name")
	address	= fields.Char(string="Address")
	email = fields.Char(string="Email")
	contact_no = fields.Char(string="Contact Number")