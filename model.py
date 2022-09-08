

class Model:
	""" Define the logic part """

	def __init__(self):
		self.previous_value = ''
		self.value = ''
		self.operator = ''
		
		

	def calculate(self, caption):
		#print(f' calculating for {caption}')

		if caption == 'C': #reset
			self.previous_value = ''
			self.value = ''
			self.operator = ''

		elif caption == '+/-':
			self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value

		elif caption == '%':
			value = float(self.value) if '.' in self.value else int(self.value)
			self.value = str(value / 100)

		elif caption == '=':
			value = self._evaluate()

			if '.0' in str(value):
				value = int(value)
		
			self.value = str(value)

		elif caption == '.':
			if not caption in self.value:
				self.value += caption

		elif isinstance(caption, int):		# → To check if an obj is a insante of a class or ints.
			self.value += str(caption)

		else:
			if self.value:
				self.operator = caption
				self.previous_value = self.value
				self.value = ''

		return self.value


	def _evaluate(self):
		return eval(self.previous_value + self.operator + self.value)

