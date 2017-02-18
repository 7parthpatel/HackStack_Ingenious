import subprocess
import MySQLdb
db = MySQLdb.connect("localhost","root","p","numberplate")
cursor = db.cursor()

a = "alpr -c eu /home/parth/Documents/car4.jpg"
a = a.split(' ')
z = subprocess.check_output(a)
z=z.split('\n')
print z
#print z[1]
detectnumber_1 = z[1].split('- ')[1].split('\t')[0]
detectnumber = "'"+detectnumber_1+"'"
print detectnumber
#sql = " INSERT INTO licensenumber (number) VALUES" % (detectnumber)
cursor.execute("""INSERT INTO licensenumber(number) VALUES (%s)""" % (detectnumber))
db.commit()
db.close()

import os
import json
import urllib2

url = "https://www.regcheck.org.uk/api/reg.asmx/Check?RegistrationNumber="+detectnumber_1+"&username=testertester194"
print url
req = urllib2.Request(url)
response = urllib2.urlopen(req)
x = response.read()
y = x.split('<vehicleJson>')[1].split('</vehicleJson>')[0]
z = json.loads(y)
print z
print z['RegistrationYear']
print z['CarModel']['CurrentTextValue']
print z['EngineSize']['CurrentTextValue']
print z['FuelType']['CurrentTextValue']
print z['CarMake']['CurrentTextValue']
print z['ModelDescription']
print z['DriverSide']['CurrentTextValue']
print z['Transmission']['CurrentTextValue']
print z['VehicleInsuranceGroup']