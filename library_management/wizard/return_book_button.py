from odoo import models, fields, api
from datetime import date, timedelta, datetime


class ReturnBookButton(models.TransientModel):
	_name = "return.book.button"

	# reture_book = fields.Boolean(string="Return Individual Book")
	test_ids = fields.One2many('return.book.buttons','return_book_id',string='TEST')
	# book_name = fields.


	def action_done(self):
		if self._context.get('active_id', False):
			issue = self.env['issue.book'].browse(self._context.get('active_id'))
			if issue:
				issue.state = 'return'
		for rec in self.test_ids:
			return_book_date = self.env["register.date"].search([
								("entry_id","=", self._context.get("active_id")),
								("return_date", "=", False),
								("book_id", "=", rec.books_id.id)
								])
			for book_line in return_book_date:
				for book in range(rec.returned_quantity):
					return_book_date[book].return_date = date.today()
		
	








class ReturnBookButtons(models.TransientModel):
	_name = "return.book.buttons"

	return_book_id = fields.Many2one("return.book.button",string="Book Id", readonly=True)
	book_quantity = fields.Integer(string='Issued Quantity', readonly=True)
	return_date = fields.Date(string="Return Date", readonly=True)
	books_id = fields.Many2one("book.details",string='Book Name',  readonly=True)
	remaining_quantity = fields.Integer(string="Remaining Quantity", default=0, readonly=True)
	returned_quantity = fields.Integer("Return Quantity ")
			 	
	# @api.onchange("reture_book")
	# def add_data(self):
	# 	print("in***********", self)
	# 	for rc in  self:
	# 		print("check *******")
	# 		data = self.env["register.books"].search([('id','=',self._context.get('active_id'))])
	# 		print(":::::::::::::::::::::::::::::::::::::::",data)

	# 		# print("\n\n data",data)
	# 		for dat in data:
	# 			print(":::::::<<<<<<<<",dat.book_detail_id)
	# 			vals={
	# 				'books_id':dat.book_detail_id.book_name,
	# 				'book_quantity':dat.issue_quantity
	# 			}
	# 			print(":::::::::::",vals)
	# 	rc.write({
	# 		"test_ids":[(0,0,vals)]
	# 		})

	# @api.model
	# def default_get(self,fields):
	# 	res = super(ReturnBookButton,self).default_get(fields)
	# 	issue = self.env["issue.book"].search([("books_line_ids", "=", self._context.get("active_id"))])
	# 	print("\n\n\n guhuthg",issue)
	# 	lst1 = []
	# 	for rec in issue.books_line_ids:
	# 		lst1.append((0,0,{'books_id' : rec.book_detail_id.book_name,'book_quantity':rec.issue_quantity}))
	# 	print("\n\n\n tftvgrtgtr",lst1)
	# 	if issue:
	# 		res['test_ids'] = lst1
	# 	# model_rec = self.env['issue.book.info'].search([]).books_line_ids
	# 	# for record in model_rec:
	# 		# res['books_ids'] = ([0,0,])
	# 	return res



	



