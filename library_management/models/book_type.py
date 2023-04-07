from odoo import models, fields, api


class BookType(models.Model):
	_name = 'book.type'

	name = fields.Char(String='Book Type')