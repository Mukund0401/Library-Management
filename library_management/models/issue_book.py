from odoo import models, fields, api
from datetime import date

class IssueBook(models.Model):
	_name = 'issue.book'

	user_id = fields.Many2one("res.partner",string="User Name")
	books_line_ids = fields.One2many('register.books','empty_id',string="Books")
	address = fields.Char(string="Address")
	email = fields.Char(string="Email")
	phone = fields.Char(string="Phone Number")
	issue_date = fields.Date(string="Issue Date", readonly=True)
	return_date = fields.Date(string=" Return Date", readonly=True)
	state = fields.Selection(selection=[('draft', 'Not_IssueBook'),('done', 'IssueBook'),('return','Thank u')], string='Status', required=True, readonly=True, copy=False, tracking=True, default='draft')


	# @api.model
	# def create(self,vals):
	# 	print("::::::::::::::::::::::::::::::::::::::::::::::::",vals)

	# 	if not vals.get('user_id'):
	# 		seq = self.env["register.date"].search([('id', '=', vals.books_line_ids)])
	# 		print("::::::::::::::::::::::::::::::::::::::::::::::::",seq)
	# 		vals['book_code'] = seq.book_name
	# 	return super(IssueBook,self).create(vals)

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
