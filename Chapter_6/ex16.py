import smtplib
 
Email_addr = "*********@gmail.com"
password = "***************"
server_addr = 'smtp.gmail.com'
port = 587

def send_email(recipient,subject,msg):
	server = smtplib.SMTP(server_addr, port)
	server.starttls()
	server.login(Email_addr, password)
	header = 'To:' + recipient + '\n' + 'From: ' + Email_addr
	header = header + '\n' + 'Subject:' + subject + '\n'
	msg = header + '\n' + msg + ' \n\n'
	server.sendmail(Email_addr,recipient, msg)
	server.quit()

send_email('*************@yahoo.com','Test','Hi, We test Pyhthon.')
