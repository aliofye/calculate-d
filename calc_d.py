def calc_d():
	e = 100 						# Enter your own value for e here
	totient_n = 1729 					# Enter your own value for the totient of n (not the n value)
	d = 0
	m = 0			 				# Multiply m by totient_n and increment it one by one until the remainder is 0
	limit = 1 						# You can change this to output more values for d in case the first value of d doesn't satisfy your needs

	for i in range (0, limit):
		r = 1 						# Remainder must be initialized as 1 (or any number other than 0) for the while loop to work
		while r != 0:
			r = ((totient_n * m) + 1) % e 		# To identify which m, when multiplied by totient_n, divides e evenly
			if r == 0:
				d = ((totient_n * m) + 1) / e 	# To calculate d
			m += 1
		
		print("Modular Multiplicative Inverse: " + str(d))

calc_d()
