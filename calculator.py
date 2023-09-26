def add(num1, num2):
	return num1+num2
    
def subtract(num1, num2):
	return num1-num2

def multiply(num1, num2):
	return num1*num2

def divide(num1, num2):
	return num1/num2

def calculator():
	print('Please select from below - \n' \
        '1.Add\n'\
        '2.Subtract\n'\
        '3.Multiply\n'\
        '4.Divide\n')
	op=input('Select operations from 1, 2, 3, 4: ')
	num1=int(input('Enter first number- '))
	num2=int(input('Enter second number- '))
	if op=='1':
		print(num1,'+',num2,'=',add(num1, num2))
	elif op=='2':
		print(num1,'-',num2,'=',subttract(num1, num2))
	elif op=='3':
		print(num1,'*',num2,'=',multiply(num1, num2))
	elif op=='4':
		print(num1,'/',num2,'=',divide(num1, num2))
	else:
		print('Please select a valid operation')

calculator()
