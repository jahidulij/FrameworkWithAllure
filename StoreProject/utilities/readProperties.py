import configparser

config = configparser.RawConfigParser()
config.read("C:/Users/JahidulIslam/PycharmProjects/pytestSeleniumEasy2/StoreProject/configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'base_url')
        return url

    @staticmethod
    def getEmail():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
