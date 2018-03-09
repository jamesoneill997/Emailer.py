import smtplib
import sys
subject = sys.argv[1] #here, enter the subject of your email in terminal/command prompt

message = file.read(file(sys.argv[2]))
if input('Please Enter Pin/Pass: ') == 1999: #set your pin/password,this is to be entered during execution.!!!!	NOTE: IF PASS = INT, REMOVE COMMAS	!!!!



	def sender(subject, message):
		#TRY STATEMENT CATCHES LOGIN ERRORS
		try:
			server = smtplib.SMTP('smtp.Provider__example:"gmail.com": 587')
			server.ehlo()
			server.starttls()
			server.login('Enter_Your_E-mail', 'Enter_Password')

			Subject_to_send = 'Subject: {} \n\n {}'.format(subject, message)
			server.sendmail('Enter_Your_E-mail', 'Enter_RECIPIENTS_E-mail', Subject_to_send)
			server.quit()
			print('Successfully sent.')


		except:
			print('Error occurred while sending E-Mail, try checking your login details.')
	

	sender(subject,message) #EXECUTION


else:
	print('Incorrect pin number entered, please retry.')

