import subprocess
import MySQLdb
db = MySQLdb.connect("localhost","root","p","numberplate")
cursor = db.cursor()

a = "alpr -c eu /home/parth/Documents/car3.jpg"
a = a.split(' ')
z = subprocess.check_output(a)
z=z.split('\n')
print z
#print z[1]
detectnumber_1 = z[1].split('- ')[1].split('\t')[0]
detectnumber = "'"+detectnumber_1+"'"
print detectnumber
#sql = " INSERT INTO licensenumber (number) VALUES" % (detectnumber)
#cursor.execute("""INSERT INTO licensenumber(number) VALUES (%s)""" % (detectnumber))
#db.commit()
#db.close()

import os
import json
import urllib2

url = "https://www.regcheck.org.uk/api/reg.asmx/Check?RegistrationNumber="+detectnumber_1+"&username=jayu4"
print url
req = urllib2.Request(url)
response = urllib2.urlopen(req)
x = response.read()
#print x
y = x.split('<vehicleJson>')[1].split('</vehicleJson>')[0]
#print y
z = json.loads(y)
#print z
#a = ""
#b = ""
#c = ""
#d = ""
#e = ""
#f = ""
#name = ""
#monumber = ""
#emailid = ""
if 'RegistrationYear' in z:
	a = z['RegistrationYear']
	#name = "Parthkumar Patel"
	#monumber = "8140212380"
	#emailid = "pandyakavi@gmail.com"
if 'CarModel' in z:
	b = z['CarModel']['CurrentTextValue']
if 'EngineSize' in z:
	c = z['EngineSize']['CurrentTextValue']
if 'FuelType' in z:
	d = z['FuelType']['CurrentTextValue']
if 'CarMake' in z:
	e = z['CarMake']['CurrentTextValue']
#print z['ModelDescription']
#print z['DriverSide']['CurrentTextValue']
#print z['Transmission']['CurrentTextValue']
#if 'VehicleInsuranceGroup' in z:
#	f = z['VehicleInsuranceGroup']
#name = "Parthkumar Patel"
#monumber = "8140212380"
#emailid = "parthkumarj.patel@gmail.com"
if a != "":
	#cursor.execute("""INSERT into vehicledetails(number,year,carmodel,enginesize,fueltype,carmake,name,monumber,emailid) values (%s,%s,%s,%s,%s,%s,%s,%s,%s) """ % (detectnumber,a_1,b_1,c_1,d_1,e_1,name,monumber,emailid))
	cursor.execute("""SELECT emailid from vehicledetails where number = %s""" % (detectnumber))
	row = cursor.fetchone()
	#print row
	emailid = row

	db.commit()
	db.close()
	#print emailid
	import smtplib

	fromaddr = '7pjpatel77@gmail.com'
	toaddrs  = emailid
	# Credentials (if needed)
	username = '7pjpatel77'
	password = 'pj11126892'

	SUBJECT = "Traffic e-Challan"
	msg = 'Dear Sir/Maam, \n\n Offence Description : Violation of Parking Law \n Applicable Section : 119 \n Fine Amount : Rs.100 \n Deadline : within 1 month of issuing date \n\n Sincerely, \n Ahmedabad Traffic Police'

	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login(username,password)
	BODY = '\r\n'.join(['To: %s' % toaddrs,
	        'From: %s' % fromaddr,
	        'Subject: %s' % SUBJECT,
	        '', msg])

	server.sendmail(fromaddr, [toaddrs], BODY)
	server.quit()

