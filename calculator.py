import art
from os import system, name

def clear():
	if name == 'nt':
		system('cls')
	else:
		system('clear')

print(art.logo)

def calc(n1, sign, n2) :
	if sign == '+' :
		return n1 + n2
	elif sign == '-' :
		return n1 - n2
	elif sign == '*' :
		return n1 * n2
	elif sign == '**' :
		p = n1
		if int(n2) == 0 :
			return 1
		for _ in range(1, int(n2)) :
			n1 *= p
		return n1
	elif sign == '/' :
		return n1 / n2
	elif sign == '%' :
		return n1 % n2
	else :
		return 0

def check_sign(str) :
	if str in ('+', '-', '*', '/', '**', '%') :
		return False
	else :
		return True

loop = True
result = 0
as_number = False

while loop :

	if as_number :
		n1 = result
	else :
		n1 = float(input("Enter first number : "))

	as_number = False
	wrong_sign = True

	while wrong_sign :
#	Used to check user input for the Sign
		sign = input("Which operation ?(+, -, %, *, **, /) : ")
		wrong_sign = check_sign(sign)
		if wrong_sign :
			print(".... try again")

	n2 = float(input("Enter second number : "))
	clear()
	result = calc(n1, sign, n2)

	print(f"{n1} {sign} {n2} = {result}")

	redo = input("enter = continue, n = new calculation, e = exit : ")
	if redo == 'n' :
		loop = True
	elif redo == 'e' :
		loop = False
	else :
		loop = True
		as_number = True

