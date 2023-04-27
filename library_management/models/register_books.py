from odoo import models, fields, api
from odoo.exceptions import ValidationError

class RegisterBooks(models.Model):
	_name = 'register.books'
	# _rec_name = "book_detail_id"

	book_detail_id = fields.Many2one('book.details',string='Book Name')
	issue_bookline_ids = fields.Integer(string="Issue Book ID")
	empty_id = fields.Many2one("issue.book")
	issue_quantity = fields.Integer(string="Issue Quantity")
	# return_date = fields.Date(string="Return Date")
	book_types_ids = fields.Many2many("book.type",string="Book Type")
	reamaining_quantity = fields.Char("Ramaining Quantity", compute="_compute_remaining_quantity")

	@api.onchange('book_detail_id')
	def _onchange_book_type(self):
		if self.book_detail_id:
			book_type = self.env['book.details'].search([('id','=',self.book_detail_id.id)])
			self.update({
				'book_types_ids':[(6,0,book_type.book_type_ids.ids)]
				})
		else:
			pass


	def _compute_remaining_quantity(self):
		for rec in self:
			rec.reamaining_quantity = 0
			rec.reamaining_quantity = self.env["register.date"].search_count([("entry_id", "=", rec.empty_id.id), ("book_id", "=", rec.book_detail_id.id), ("return_date", "=", False)])








































	# @api.onchange('book_detail_id')
	# def _onchange_book_type(self):
	# 	for rec in self:
	# 		# rec.book_type_ids = False
	# 		book_type = self.env['book.details'].search([('book_name','=',self.book_detail_id.book_name)])
	# 		# book_type_name=rec.books_line_ids.book_type_ids
	# 		print("::::::::::::::>>>>>>>>>>>",book_type.book_name,self.book_detail_id.book_name)
	# 		for record in book_type:
	# 			if record.book_name == self.book_detail_id.book_name:
	# 				# print(":::::::::<<<>>>:::::::",'gtyufytfyfy',record.book_type_ids.id)
	# 				rec.update({
	# 					'book_type_ids':[(6,0,record.book_type_ids.ids)]
	# 					})



