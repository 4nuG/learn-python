'''
Convert a numerical score into a letter grade.
'''
score = float(input('Numerical score? '))
if score >=94:
	print ('A')
elif score >=90:
	print ('A-')
elif score >=87:
	print ('B+')
elif score >=84:
	print ('B')
elif score >=80:
	print ('B-')
elif score >=77:
	print ('C+')
elif score >=74:
	print ('C')
elif score >=70:
	print ('C-')
elif score >=67:
	print ('D+')
elif score >=64:
	print ('D')
elif score >=60:
	print ('D-')
elif score <60:
	print ('F')
