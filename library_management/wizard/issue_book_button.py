from odoo import models, fields
from datetime import date, timedelta, datetime




class IssueBookButton(models.TransientModel):
	_name = "issue.book.button"

	# book_name = fields.Char(string="Book Name")
	issue_date = fields.Date(string="Issue Date")


	def action_confrom(self):
		if self._context.get('active_id', False):
			issue = self.env['issue.book'].browse(self._context.get('active_id'))
			print("\n\n\n uuyuyu",issue.state)
			if issue:
				issue.state = 'done'
			# if issue:
				issue.issue_date = self.issue_date
			# 	issue.state = issue.write({'state':'done'})



