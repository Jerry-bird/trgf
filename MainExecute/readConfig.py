import os
import configparser

from Conf import getpathInfo

path = getpathInfo.get_path()
config_path = os.path.join(path, 'config.ini')
config = configparser.ConfigParser()
con = config.read(config_path, encoding='utf-8')


# print(con)

class ReadConfig:

    def get_http(self, name):
        value = config.get('HTTP', name)
        return value

    def get_con(self, name):
        conNo = config.get('CON', name)
        return conNo


if __name__ == '__main__':
    print('HTTP中的base_url值为：', ReadConfig().get_http('base_url'))
