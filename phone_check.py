import os
import re

def print_dashline():
	print "\n"+"-"*100+"\n"

def is_exit(user_input):
	if user_input.strip() == 'quit':
		print_dashline()
		print ("\t\t\t\t\t THANKS FOR USING OUR PROGRAM!")
		print_dashline()
		os._exit(1)
	
def format(user_input):
	if re.search('[a-zA-Z]', user_input):
		return None
	else:
		phone_number = re.sub('[^\+?\d]','', user_input).strip()
		if phone_number[0] == '0' and phone_number[1] == '0':
			return None
		else:
			return phone_number.lstrip('0')


def check(phone_number):
	pattern = re.compile("^\+?1?[2-9]\d{9,12}$")
	return pattern.match(phone_number)

def create_e164(phone_number):
	phone_number = '+1'+phone_number if phone_number[0] != '+' else phone_number
	return phone_number

def print_output(phone_number):
	if phone_number:
		print 'Your phone number in E.164 format : ',phone_number
	else:
		print 'Null : Entered Number is invalid.'

# Use only for unittesting and API Calls
def APIChecker(user_input):
	phone_number = format(user_input)
	# checking if valid	
	if phone_number:
		phone_number = create_e164(phone_number)  if (check(phone_number)) else None
	return phone_number

if __name__ == '__main__':
	print '\nType \'quit\' to exit any time!'

	while(1):
		user_input = raw_input('\nEnter phone number : ')
		# user wants to quit
		is_exit(user_input)
		# Formatting user_input
		phone_number = format(user_input)
		# checking if valid	
		if phone_number:
			phone_number = create_e164(phone_number)  if (check(phone_number)) else None
				
		# printing an output
		print_output(phone_number)
			