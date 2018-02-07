import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login("rajivahmed0001@gmail.com","password")


server.sendmail("rajivahmed0001@gmail.com","rajivuddinahmed001@gmail.com","I am Rajiv Uddin Ahmed")

server.close()



