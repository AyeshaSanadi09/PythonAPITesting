# to read data from config file we are using config parser
from configparser import ConfigParser

# creating object of config parser
obj = ConfigParser()

# read file
obj.read("config.cfg")

# get sections
print(obj.get("Section1","password"))