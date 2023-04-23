import smtplib as s


ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
ob.login('ziamalhi1234@gmail.com', '-------------')
subject = "test python"
body = "I love Muhammad"
massage = "subject:{}\n\n{}".format(subject, body)
list_add = ['ziamalhi15@gmail.com']
ob.sendmail('ziamalhi1234@gmail.com', list_add, massage)
print("send mail")
ob.quit()
