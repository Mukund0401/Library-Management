from odoo import models, fields, api


class ReturnBookButton(models.TransientModel):
	_name = "return.book.button"

	reture_book = fields.Boolean(string="Return Individual Book")
	test_ids = fields.One2many('return.book.buttons','return_book_id',string='TEST')
	# book_name = fields.


	# books_line_ids = fields.One2many('register.books','empty_id',string="Return Book")


	@api.onchange("reture_book")
	def add_data(self):
		print("in***********")
		for rc in  self:
			print("check *******")
			data = self.env["register.books"].search([('issue_bookline_ids','=',self._context["active_id"])])
			print(":::::::::::::::::::::::::::::::::::::::",data)

			print("\n\n data",data)
			for dat in data:
				print(":::::::<<<<<<<<",dat.book_detail_id.id)
				vals={
					'book_name':dat.book_detail_id.book_name,
					'book_quantity':dat.issue_quantity
				}
				print(":::::::::::",vals)
				self.write({
					"test_ids":[(0,0,vals)]
					})
			 	

class ReturnBookButtons(models.TransientModel):
	_name = "return.book.buttons"

	return_book_id = fields.Many2one("register.date",string="Book Id")
	book_quantity = fields.Integer(string='Book Quantity')
	book_name = fields.Many2one("book_details",string='Book Name')

	



