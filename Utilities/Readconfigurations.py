from configparser import ConfigParser


def ReadConfigs(category,key) :
    config=ConfigParser()
    config.read("Configurations/config.ini")
    return config.get(category,key)
