#!/usr/bin/python3

for i in range(1,51):		#	iterates int 1 through 50
	if (i % 3 == 0):		#	test if divisible by 3

		if (i % 7 == 0):		#	test if divisible by 7 
			print('#{}\t'.format(i) + 'CloudComputing')		#	if divisible by 3 & 7, prints iteration, arg response, and 'Computing'
			
		else:
			print('#{}\t'.format(i) + 'Computing')		#	prints iteration, arg response, and 'Computing'

	elif (i % 7 == 0):		#	test if divisible by 7
		print('#{}\t'.format(i) + 'Cloud')

	else:
		print('#{}'.format(i))
else:
	exit
