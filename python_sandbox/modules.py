# A module is basically a file containing a set of functions to include in your application. There are core python modules, 
# modules you can install using the pip package manager (including Django) as well as custom modules

#RUN `pip3 freeze` to see a list of packages installed in this file

# Core modules
import datetime
from datetime import date
# import time
from time import time

print(datetime.date.today())
print(date.today())
# print(time.time())
print(time())

today = date.today()
timestamp = time()

# Pip modules
import camelcase

camel = camelcase.CamelCase()
text = 'hello there world'

print(camel.hump(text))

# Custom modules
import validator
# to use `validator.validate_email(email)`
from validator import validate_email
# to use `validate_email(email)`

email = 'test@test.co'
if validate_email(email):
  print('Email is valid')
else:
  print('Not an email')