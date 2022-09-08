from model import Model
from view import View


class Controller(object):	
	"""Manage the View part and the Model part of the app."""
	def __init__(self):
		self.model = Model()
		self.view = View(self)

	def main(self):
		self.view.main()

	def on_button_click(self,  caption):
		#rint(f'button {caption} clicked')
		result = self.model.calculate(caption)

		self.view.value_var.set(result)
		




