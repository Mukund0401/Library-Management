from odoo import models, fields, api

class BookAuthor(models.Model):
	_name = "book.author"
	_rec_name ="author_name"

	author_name = fields.Char(string="Author Name")
	address	= fields.Char(string="Address")
	email = fields.Char(string="Email")
	contact_no = fields.Char(string="Contact Number")



class SaleOrder(models.Model):
	_inherit = 'sale.order'

	
	sale_order = fields.Char("Sale Order")

class ResPartner(models.Model):
	_inherit = 'res.partner'

	is_author = fields.Boolean(string="is author")
	# company_type = fields.Selection(string='Company Type',
	# 	selection=[('person', 'Individual'), ('company', 'Company'),('activ', 'Aktiv')],
	# 	compute='_compute_company_type', inverse='_write_company_type')


	def good(self):
		print("\n\n\nGood\n\n\n\n")
		return  {
				'type':"ir.actions.act_window",
				'res_model':"return.book.button",
				'name':("Book Line ID"),
				'view_mode':'form',
				'target':'new',
				}




	# def ref_button(self):
	# 	vals={
	# 	'author_name':"Mukund"
	# 	# 'address':"paldi",
	# 	# 'email':'Mukund@1404',
	# 	# 'contact_no':7227945509
	# 	}
	# 	self.create({
	# 		'author_name':[(0,0,vals)]
	# 		})