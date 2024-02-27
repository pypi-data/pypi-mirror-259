import configparser

global config

config = configparser.ConfigParser()

def read(direct, variable):
    print(config[direct][variable])

def write(direct, variable, change):
    config[direct][variable] = change

def sopen(file):
    try:
        print(file)
    except:
        print("File not found or not specified.")
    else:
        try:
            config.read(file)
        except:
            print("File does not exist or something else happened.")
        else:
            config.read(file)
