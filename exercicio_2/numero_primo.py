def primo(numero):

	primo = 1
	
	for k in range(numero):
	
		d = k + 1 
		
		if ( d not in (1, numero) ) and numero % d == 0 :
			primo = 0
			break
			
								
	return primo 
