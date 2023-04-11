from odoo import models, fields, api
from datetime import date, timedelta, datetime


class IssueBook(models.Model):
	_name = 'issue.book'

	user_id = fields.Many2one("res.partner",string="User Name")
	books_line_ids = fields.One2many('register.books','empty_id',string="Books")
	address = fields.Char(string="Address")
	email = fields.Char(string="Email")
	phone = fields.Char(string="Phone Number")
	book_name_id = fields.Many2one('book.details',string="Book Name")
	book_quantity = fields.Integer(string="Book Quantity")
	issue_date = fields.Date(string="Issue Date", readonly=True)
	return_date = fields.Date(string=" Return Date", readonly=True)
	state = fields.Selection(selection=[('draft', 'Not_IssueBook'),('done', 'IssueBook'),('return','Thank u')], string='Status', required=True, readonly=True, copy=False, tracking=True, default='draft')
	deadline_date = fields.Date(string="Deadline", compute='compute_deadline')
	total_charge = fields.Integer(string="Total Charge", compute="compute_total_charge")



	def compute_deadline(self):
		for rec in self:
			rec.deadline_date = 0
			if rec.issue_date:
				rec.deadline_date = rec.issue_date + timedelta(days=15)
		# print("::::::::::::::::::",current_date)
		# print("::::::::::::::::::::",type(current_date))
		# # self.issue_date = self.issue_date.strftime('%Y-%m-%d')
		# print(":::::::::::::::::\n\n\n",self.issue_date)
		# print(":::<<><<<<<<<<<<<<",type(self.issue_date))
		# # self.deadline_date = 



	@api.depends("return_date")
	def compute_total_charge(self):
		for rec in self:
			rec.total_charge = 0
			for record in rec.books_line_ids:
				for_charge = self.env['book.details'].search([('id','=',record.book_detail_id.id)]).book_charge
				# print('\n\n\n\n\n\n\n\n\n\n\n\n',for_charge)
					
					# print(":::::::::::::::::::::::::::::::::",rec.total_charge)
				# if rec.return_date and rec.deadline_date<rec.return_date:
					days_calculation = str(rec.return_date - rec.deadline_date)
					days_calculation = days_calculation[0:2]
					caluculation_days = int(days_calculation)//5
					print('::::::::::::::',caluculation_days)
					print('::::::::::::::',days_calculation)

					# rec.total_charge = rec.total_charge * caluculation_days + for_charge


					# print('\n\n\n\n\n\n\n\n\n\n\n\n',days_calculation)
					# print(":::::::::::::::::::<<<<>>>>>>",type(caluculation_days))
					# rec.total_charge = (caluculation_days) * for_charge
					for data in range(caluculation_days):
						for_charge += for_charge
						rec.total_charge = rec.total_charge * caluculation_days
						rec.total_charge = rec.total_charge + for_charge

					# print("::::::::::\n\n\n",type(days_calculation),days_calculation)
					# print(":::::::\n\n\n\n",days_calculation)
					# if int(days_calculation) > 5 and int(days_calculation) <10:
					# 	print(":::::::::::::::<<<<>>>>>>>\n\n\n",'abcbdh')
					# 	rec.total_charge = for_charge
					# else:
					# 	print(":::::::::::::::<<<<>>>>>>>\n\n\n",'12345')
					# 	rec.total_charge = for_charge * 2 








	def ref_button(self):
		vals={
			'issue_quantity' : self.book_quantity,
			'book_detail_id' : self.book_name_id.book_name,
		}
		self.write({
			'books_line_ids' :[(0,0,vals)]
			})


	@api.onchange("user_id")
	def _onchange_name_detail(self):
		for rec in self:
			rec.email = ""
			if rec.user_id:
				res_data = self.env["res.partner"].search([("id", "=", rec.user_id.id)])
				rec.email = res_data.email
				rec.phone = res_data.phone
				if not res_data.street2:
					rec.address = str(res_data.street)+"\n"+str(res_data.zip)+"\n"+str(res_data.city)
				else:
					rec.address = str(res_data.street)+"\n"+str(res_data.street2)+"\n"+str(res_data.zip)+"\n"+str(res_data.city)


	def issue_book_view(self):
		# change_outcoming_date = self.env["register.books"].search([()]
		register = self.env['register.date']
		for rec in self:
			rec.write({'state':'done'})
			rec.issue_date = date.today()
			for line in rec.books_line_ids:
				bookid_get = self.env['book.details'].search([('id', '=', line.book_detail_id.id)])
				globle_book_id = bookid_get.id
				for _ in range(line.issue_quantity or 1):
					print("\n\n\n", rec.books_line_ids)
					register.create({
						'book_id': globle_book_id,
						'book_name':line.book_detail_id.book_name,
						'issuing_date':rec.issue_date
						})
		

	





	def return_view(self):
		for rec in self:
			rec.write({'state': "return"})
			rec.return_date = date.today()
			for data in rec.books_line_ids:
				register = self.env["register.date"].search([("book_id", "=", data.book_detail_id.id)])
				register.return_date = date.today()
		# fields = ['name','city']
		# partner_id = self.env['res.partner'].read_group([('city','=','Fremont')], 
		# 	fields=['name'],groupby=['city','name'])
		# print("\n\n\n\n",partner_id)


	# def read_partner(self):
	
	# def unlink(self):
	# 	model_rec = self.env['register.books'].search([('id','=',self.books_line_ids.ids)])
	# 	for rec in model_rec:
	# 		rec.unlink()
	# 		print("abcdfddsgs",rec)
	# 	return super(IssueBook,self).unlink()

	# @api.model
	# def create(self,vals):
	# 	print("::::::::::::::::::::::::::::::::::::::::::::::::",vals)

	# 	if not vals.get('user_id'):
	# 		seq = self.env["register.date"].search([('id', '=', vals.books_line_ids)])
	# 		print("::::::::::::::::::::::::::::::::::::::::::::::::",seq)
	# 		vals['book_code'] = seq.book_name