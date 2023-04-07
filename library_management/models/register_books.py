from odoo import models, fields, api

class RegisterBooks(models.Model):
	_name = 'register.books'
	# _rec_name = "book_detail_id"

	book_detail_id = fields.Many2one('book.details',string='Book Name')
	empty_id = fields.Many2one("issue.book")
	issue_quantity = fields.Integer(string="Issue Quantity")
	book_type_ids = fields.Many2many("book.type",string="Book Type",readonly=True)



	@api.onchange('book_detail_id')
	def _onchange_book_type(self):
		for rec in self:
			book_type = self.env['book.details'].search([]).book_type_ids.ids
			# book_type_name=rec.books_line_ids.book_type_ids
			for record in book_type:
				print("::::::::::::::::::<<<<<<<<<<<?>???????>>>>>>",record)
				rec.update({
					'book_type_ids':[(4,record)]
					})



