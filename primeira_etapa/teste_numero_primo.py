import unittest
from numero_primo import *


class TesteNumeroPrimo(unittest.TestCase):


	def testVerificaSeNumero2EPrimo(self):
		self.assertTrue(numero_primo(2))


	def testVerificaSeNumero3EPrimo(self):
		self.assertTrue(numero_primo(3))

	
	def testVerificaSeNumero100NaoEPrimo(self):
		self.assertFalse(numero_primo(100))

			
if __name__ == '__main__':
	unittest.main()
