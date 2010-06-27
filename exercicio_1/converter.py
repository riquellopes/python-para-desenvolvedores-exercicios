
def converter(valor, base):

	if base == 'farenheit' :
		r = ( valor - 32 ) / 1.8  
	elif base == 'celcius':
		r = ( valor * 1.8 ) + 32
	
	return r			
