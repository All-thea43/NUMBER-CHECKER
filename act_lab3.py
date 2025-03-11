def check_number(num):
	if num == 0:
		print("0 is neither odd nor even. ")
	elif num % 2 == 0:
		print(f"{num} is an Even number. ")
	else:
		print(f"{num} is an Odd number. ")

while True:
	try:
		num = int(input("Enter a number: "))
		check_number(num)
	except:
		print("Invalid input! Please enter a valid integer. ")