from odoo import models, fields, api


class BookType(models.Model):
	_name = 'book.type'

	name = fields.Char(String='Book Type')





	def copy(self, default=None):
		if default is None:
			default = {}
		default['name'] = self._get_copy_name()
		return super(BookType, self).copy(default)
	
	def _get_copy_name(self):
		parts = self.name.split(' - ')
		name = parts[0]
		if len(parts) > 1:
			number = int(parts[1]) + 1
		else:
			number = 1
		return '%s - %s' % (name, number)