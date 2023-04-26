from odoo import models, fields, api



class SelectionWizard(models.TransientModel):
	_name = "selection.wizard"

	first_name = fields.Char("First Name")
	mid_name = fields.Char("Mid Name")
	last_name = fields.Char("Last Name")