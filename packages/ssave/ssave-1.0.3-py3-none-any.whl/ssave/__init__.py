import sys
import configparser
import easy

config = configparser.ConfigParser()
print("SCOS Save Utility is Included.")
config.read("data.ini")
print(config.read("Info", "Version"))

try:
    print(sys.argv[1])
except:
    print("File not found or not specified.")
else:
    try:
        config.read(sys.argv[1])
    except:
        print("File does not exist or something else happened.")
    else:
        config.read(sys.argv[1])