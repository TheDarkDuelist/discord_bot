import configparser

config = configparser.ConfigParser()
config.read('config.ini')
key = config["DISCORD"]
token = key["BOT_TOKEN"]
print(token)