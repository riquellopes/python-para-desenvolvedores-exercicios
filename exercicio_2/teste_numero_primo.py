import unittest
from numero_primo import primo

class TestNumeroPrimo(unittest.TestCase):


	def testVerificaSeNumeroDoisEPrimo(self):
		self.assertTrue(primo(2))

	
	def testVerificaSeNumeroCincoEPrimo(self):
		self.assertTrue(primo(5))

				
	
if __name__ == '__main__':
	unittest.main();	



