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
	total_charge = fields.Integer(string="Total Charge", compute="compute_total_charge")

	@api.onchange('book_quantity')
	def _onchange_book_quantity(self):
		print("\n\n\n::::::::<<>>>",self._origin)
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

			# if element.books_line_ids:
			# 	print("yes")
			# 	print('element.books_line_ids',element.books_line_ids)
			# 	register_book_data = self.env["register.books"].search([
			# 		('book_detail_id','=',element.book_name_id.id)])
			# 	print('\n\n\n\n')
			# 	print("-----------------------")
			# 	print(register_book_data.ids)
			# 	# print(register_book_data.issue_bookline_ids)
			# 	print('-------------------------')
			# 	print('\n\n\n\n')


				# print(":::::::::::::::::::::<<<>>>\n\n\n",register_book_data)

		# record_book = self.env["book.details"].search([('id','=',self.book_name_id.id)])

		# vals= {
		# 	"book_detail_id": self.book_name_id.id,
		# 	"issue_quantity":self.book_quantity,
		# 	"book_types_ids":[(6,0, record_book.book_type_ids.ids)]
		# }		

		# vals = {
		# 	"book_name_id" : "33",
		# 	"issue_quantity" : 2,
		# }
		# self.write({'books_line_ids' : [(0,0,vals)]})
		# for line in self.books_line_ids:
		# 	line.write({
		# 		'book_detail_id':self.book_name_id.book_name,
		# 		})
			# print("::::\n\n\n",line.book_detail_id.book_name)
			# bookid_get = self.env['book.details'].search([('id', '=', line.book_detail_id.id)])
			# globle_book_id = bookid_get.id
			# for _ in range(line.issue_quantity or 1):
			# 	book_line.write({
			# 		'book_name':line.book_detail_id.book_name
			# 		})


		

	# _sql_constraints = [('xyz', 'unique(phone)', 'xyz')]




	def issue_book_mail(self):
		template = self.env.ref('library_management.user_mail_id').id
		template_id = self.env['mail.template'].browse(template)
		template_id.send_mail(self.id , force_send = True)

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
						'deadline_date':rec.deadline_date
						})
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


	def unlink(self):
		for line in self.book_lines_ids:
			self.env["register.books"].search([("id", "=", line.id)]).unlink()
		return super(IssueBook, self).unlink()

	# To send email from odoo
	# def action_send_email(self):
	#    self.ensure_one()
	#    ir_model_data = self.env['ir.model.data']
	#    try:
	#        template_id =    ir_model_data._xmlid_lookup('module_name.template_name')[2]
	#   	except ValueError:
	#      template_id = False
	#    try:
	# 	   compose_form_id = ir_model_data._xmlid_lookup('mail.email_compose_message_wizard_form')[2]
	#    except ValueError:
	# 	   compose_form_id = False
	# 	   template_id = self.env.ref('event.event_registration_mail_template_badge')
	# 	   compose_form = self.env.ref('mail.email_compose_message_wizard_form')
	# 	   ctx = {
	# 	       default_model='example.email',
	# 	       default_res_id=self.ids[0],
	# 	       default_use_template=bool(template_id),
	# 	       default_template_id=template_id,
	# 	       default_composition_mode='comment',
	# 	       mark_so_as_sent: True,
	# 	       force_email: True,
	# 	  }
	# 	   return {
	# 	       'type': 'ir.actions.act_window',
	# 	      'view_type': 'form',
	# 	       'view_mode': 'form',
	# 	       'res_model': 'mail.compose.message',
	# 	       'views': [(compose_form.id, 'form')],
	# 	       'view_id': compose_form.id,
	# 	       'target': 'new',
	# 	       'context': ctx,
	# 	   }
		

		

	





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