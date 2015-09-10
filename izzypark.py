#!/usr/bin/python

## More Documentation
## https://github.com/joke2k/faker
## http://fake-factory.readthedocs.org/en/master/locales/en_US.html


from faker import Faker
import time
fake = Faker()

var = 1
while var == 1 :  # This constructs an infinite loop
	#print fake.iso8601() + " " + fake.timezone() + ", " + fake.ipv6() +  ", " + fake.name() + ", " + str(fake.longitude()) + ", " + str(fake.latitude())+ ", " + fake.bs() + ", " + fake.mac_address()
	print fake.iso8601() + " " + fake.timezone() + ", " + fake.ipv6() +  ", " + fake.bs() + ", " + str(fake.longitude()) + ", " + str(fake.latitude())
	time.sleep(.08) #control how fast it scrolls