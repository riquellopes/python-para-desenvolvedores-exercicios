import unittest
from converter import converter

class TesteConverteBase(unittest.TestCase):

	
	def testCoverteFarenheitParaCelcius(self):
		self.assertEquals(converter(932, 'farenheit'), 500)	

	def testConverteCelciusParaFarenheit(self):
		self.assertEquals(converter(500, 'celcius'), 932)

	
        		
if __name__ == '__main__':
	unittest.main()
