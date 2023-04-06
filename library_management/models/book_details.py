from odoo import models, fields, api


class BookDetails(models.Model):
	_name = 'book.details'
	_rec_name = 'author_detail_id'

	author_detail_id = fields.Many2one('book.author',string='Author Name')
	book_name = fields.Char(string='Book Name')
	Price = fields.Integer(string="Book Price")
	Pages = fields.Integer(string="Book Pages")
	book_id = fields.Char(string="Book Id",readonly=True,copy=False)
	book_quantity = fields.Integer(string="Book Quantity")
	available_quentity = fields.Integer(string="Avelible Quantity",readonly=True)



	@api.model
	def create(self, vals):
		if not vals.get('book_id'):
			seq = self.env["ir.sequence"].next_by_code('book.details')
			vals['book_id'] = seq
			
		return super(BookDetails,self).create(vals)


	@api.model
	def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
		args = args or []
		if name:
			args = ['|','|',('book_id',operator,name),('book_name',operator,name),('author_detail_id',operator,name)]+args
		return self._search(args,limit=limit,access_rights_uid=name_get_uid)

	def name_get(self):
		result = []
		for rec in self:
		   name = rec.book_name+''+ str(rec.author_detail_id.author_name) +str(rec.book_id)
		   result.append((rec.id,name))
		return result


	def action_book_count(self):
		for rec in self:
			book_count = self.env['issue.book'].search([("book_name", "=",rec.book_name )])
			print("::::::::::::::::::",book_count)
				

		# 	print("::::::::::",book_count.issue_quantity)
		# 	print("::::::::::>>>><<<<<<<<",rec.book_quantity)
		# 	# rec.avelible_quentity=rec.book_quantity-book_count.issue_quantity
		
		# print(":::::::::::::::::::::::::::::::::::::::::",rec.avelible_quentity)
