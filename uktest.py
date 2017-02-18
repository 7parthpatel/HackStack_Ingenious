import os
import json
import urllib2

url = 'https://www.regcheck.org.uk/api/reg.asmx/Check?RegistrationNumber=AR020NR&username=testertester194'    
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