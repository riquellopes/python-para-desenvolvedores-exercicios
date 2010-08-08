def numero_primo(numero):

	primo = 1
	for n in range(numero):
		k = n+1

		if not k in (1, numero) and numero % k == 0:
			primo = 0
			break

		
	return primo		
