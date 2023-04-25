from odoo import models, fields, api
from datetime import date, timedelta, datetime
from odoo.exceptions import ValidationError


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
	deadline_date = fields.Date(string="Deadline", readonly=True)
	# test_id = fields.Many2one('return.book.button',string='test')
	total_charge = fields.Integer(string="Total Charge", compute="compute_total_charge")

	@api.onchange('book_quantity')
	def _onchange_book_quantity(self):
		for element in self:
			# book_get = element['book_name_id']
			# register_book_data.issue_bookline_ids = element.id
			vals = {
			'book_detail_id': element.book_name_id.id,
			'issue_quantity': element.book_quantity,
			'book_types_ids': element.books_line_ids.book_types_ids
			}
			if element.book_name_id:
				self.write({
					'books_line_ids': [(0,0,vals)]
					})

	


		

	# _sql_constraints = [('xyz', 'unique(phone)', 'xyz')]

	def book_return_reminder(self):
		print(":::::::<<<<>>>>>\n\n\n\n\n>>>>>>><<<<<<<")
		reminder = self.env['register.date'].search([])
		for rec in reminder:
			print(rec.book_name)
			if not rec.return_date:
				self.issue_book_mail()

	def issue_book_mail(self):
		for rec in self:
			template = self.env.ref('library_management.user_mail_id').id
			template_id = self.env['mail.template'].browse(template)
			template_id.send_mail(rec.id , force_send = True)

	# def unlink(self):
	# 	model_rec = self.env['register.books'].search([('id','=',self.books_line_ids.id)])
	# 	for rec in model_rec:
	# 		rec.unlink()
	# 		# print("ncfbbcfedfbcvd",rec)
	# 	return super(IssueBook,self).unlink()



	@api.depends("return_date")
	def compute_total_charge(self):
		for rec in self:
			rec.total_charge = 0
			if rec.return_date:
				for record in rec.books_line_ids:
					for_charge = self.env['book.details'].search([('id','=',record.book_detail_id.id)]).book_charge
					if str(rec.return_date) > str(rec.deadline_date):
						rec.total_charge += for_charge
				if rec.total_charge:
					days_calculation = (rec.return_date - rec.deadline_date).days
					if (days_calculation//5) == 0:
						rec.total_charge = rec.total_charge
					else:
						for i in range((days_calculation // 5) - 1):
							rec.total_charge += rec.total_charge



	def ref_button(self):
		vals={
			'issue_quantity' : self.book_quantity,
			'book_detail_id' : self.book_name_id.book_name,
		}
		self.write({
			'books_line_ids' :[(1,ID,vals)]
			})


	@api.onchange("user_id")
	def _onchange_name_detail(self):
		for rec in self:
			read_data = self.env["res.partner"].search_read([("id", "=", rec.user_id.id)],['user_id',"email",'phone'])
			print("\n\n\n\n\n",read_data)
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
		for rec in self:
			rec.deadline_date = date.today() + timedelta(days=15)
			# rec.write({'state':'done'})
			register = self.env['register.date']
			for line in rec.books_line_ids:
				bookid_get = self.env['book.details'].search([('id', '=', line.book_detail_id.id)])
				globle_book_id = bookid_get.id
				for _ in range(line.issue_quantity or 1):
					register.create({
						'book_id': globle_book_id,
						'book_name':line.book_detail_id.book_name,
						'issuing_date':date.today(),
						'deadline_date':rec.deadline_date,
						'issue_quantity':rec.book_quantity
						})
					append = self.env["register.books"].search([('id','=',line.id)])
					append.issue_bookline_ids=self.id

		action = {
			'type':"ir.actions.act_window",
			'res_model':"issue.book.button",
			'name':("ISSUE DATE"),
			'view_mode':'form',
			'target':'new',
			'context':{
				"default_issue_date":date.today(),
			}
		}
		return action
		
		# change_outcoming_date = self.env["register.books"].search([()]
		

		

	





	def return_view(self):
		print("jwbhdryuwgbdvretyuwdrgfy3uergyu8gu67hjh6gh5drf774")
		for rec in self:
			rec.write({'state': "return"})
			rec.return_date = date.today()
			for data in rec.books_line_ids:
				register = self.env["register.date"].search([("book_id", "=", data.book_detail_id.id)])
				register.return_date = date.today()
				return  {
						'type':"ir.actions.act_window",
						'res_model':"return.book.button",
						'name':("Book Line ID"),
						'view_mode':'form',
						'target':'new',
						'context':{
							"default_book_quantity":rec.book_quantity
						}
					}
		# return action
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