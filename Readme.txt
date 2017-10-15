 Program phone_check.py accepts a user input phone number string type and prints a normalized United States phone number string type in E.164 format. 
 
 A program prints phone number is invalid message if the user input is invalid phone number.

 Functionality of each function:

 1.) is_exit() : exit the program when user enters 'quit'

 2.) format() : 
     returns i) 'None' if user input starts with more than 				one '0' or contains alphabets
     		 ii) formatted user input without parantheses, 		hyphen, spaces or leading single '0'  

 3.) check() : checks formatted user input is valid phone 				  number and returns 'None' if not

 4.) create_e164() : creates E.164 format phone number

 5.) print_output() : prints output of program

 6.) APIChecker() : purpose of this function is to serve API 					calls and unittesting 

 Execution Instruction:

 To execute this program, you will need Python 2.7.11 installed on your system.

 To execute enter following command in cmd:
 	python phone_check.py


Program phone_check_unittest.py is python unittesting for the above program. It tests 4 positive cases where the phone number is formatted in E.164 format. It also tests 4 negative cases which returns 'None' as inputs are invalid.

Execution of UnitTests:
 	python phone_check_unittest.py -v

