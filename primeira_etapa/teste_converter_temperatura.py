import unittest
from converter_temperatura import converte

class TesteConverterTemperatura(unittest.TestCase):


	def testConverter30grausCelciusEmFahrenheit(self):
		self.assertEqual(converte(10, 'fahrenheit'), 50)
		
	
	def testConverter200grausFahrenheitEmCelcius(self):
		self.assertEqual(converte(50, 'celcius'), 10)

		
if __name__ == '__main__':
	unittest.main()

