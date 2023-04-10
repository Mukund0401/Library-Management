from odoo import models, fields, api

class BookAuthor(models.Model):
	_name = "book.author"
	_rec_name ="author_name"

	author_name = fields.Char(string="Author Name")
	address	= fields.Char(string="Address")
	email = fields.Char(string="Email")
	contact_no = fields.Char(string="Contact Number")


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