from odoo import models, fields, api
from datetime import date, timedelta, datetime


class ReturnBookButton(models.TransientModel):
	_name = "return.book.button"

	# reture_book = fields.Boolean(string="Return Individual Book")
	test_ids = fields.One2many('return.book.buttons','return_book_id',string='TEST')
	book_return = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="Book Return Yes Or No")
	returned_quantity = fields.Integer("Return Quantity ")
	temperory_date = fields.Date(string="Return Date")
	# book_name = fields.


	def action_done(self):
		for rec in self.test_ids:
			issue = self.env['register.date'].search([('return_date','=',False),('entry_id','=',self._context.get('active_id'))])
			for record in issue:
				record.state = 'return'
				for i in range(rec.returned_quantity):
					print("\n\n\n\n record",record)
					issue[i].return_date=date.today()

		# if self._context.get('active_id', False):
		# 	print("\n\n\n uuyuyu",self._context.get('active_id', False))
			# if issue:
			# 	issue.state = 'return'
				# print("::::::::>>>><<<<<<<<<",self.temperory_date)
				# issue.return_date = self.temperory_date

   # _sql_constraints = [('xyz', 'unique(phone)', 'xyz')]

	# @api.onchange('book_return')
	# def _onchange_return_date(self):
	# 	for rec in self:
	# 		for record in rec.test_ids:
	# 			if rec.book_return=='yes':
	# 				rec.temperory_date = date.today()
	# 				# print("\nself.temperory_date",rec.temperory_date)
	# 				vals={
	# 					"return_date":rec.temperory_date
	# 				}
	# 				rec.write({
	# 						"test_ids":[(1, record.id, vals)]
	# 						})
	# 			else:
	# 				vals={
	# 					"return_date":False
	# 				}
	# 				rec.write({
	# 					"test_ids":[(1, record.id, vals)]
	# 					})


	@api.onchange('returned_quantity')
	def _onchange_returned_quantity(self):
		# print("\n\n\n::::::::::::::::::::::>>><<<<<<<<",self)
		print("::::::::",self.returned_quantity)






	# 		print(self.return_date)
		# if self.book_return=="yes":
		# 	print("\n\n\n\n\n",self.book_return)
		# 	self.test_ids.return_date='Good'
		# 	print(self.test_ids.return_date)
		# else:
		# 	pass




	# books_line_ids = fields.One2many('register.books','empty_id',string="Return Book")


class ReturnBookButtons(models.TransientModel):
	_name = "return.book.buttons"

	return_book_id = fields.Many2one("return.book.button",string="Book Id", readonly=True)
	book_quantity = fields.Integer(string='Issued Quantity', readonly=True)
	return_date = fields.Date(string="Return Date", readonly=True)
	books_id = fields.Many2one("book.details",string='Book Name',  readonly=True)
	remaining_quantity = fields.Integer(string="Remaining Quantity", default=0)
	book_return = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="Book Return Yes Or No")
			 	
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



	



