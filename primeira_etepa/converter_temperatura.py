def converte(valor, padrao):

	if padrao == 'fahrenheit' :
		temperatura = ( valor * 1.8 ) + 32
	else: 
		temperatura = ( valor - 32 ) / 1.8

	return 	temperatura	
