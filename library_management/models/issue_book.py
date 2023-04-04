from odoo import models, fields, api

class IssueBook(models.Model):
	_name = 'issue.book'

	user_id = fields.Many2one("res.partner",string="User Name")
	books_line_ids = fields.One2many('register.books','empty_id',string="Books")
	address = fields.Char(string="Address")
	email = fields.Char(string="Email")
	phone = fields.Char(string="Phone Number")
	issue_date = fields.Date(string="Issue Date")
	state = fields.Selection(selection=[('draft', 'Not IssueBook'),('done', 'IssueBook'),], string='Status', required=True, readonly=True, copy=False, tracking=True, default='draft')


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