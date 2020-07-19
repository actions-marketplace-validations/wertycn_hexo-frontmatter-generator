import requests
from aip import AipNlp


class Util:
    aip_client = None

    @classmethod
    def get_aip_client(cls):
        # print(cls)
        if cls.aip_client == None:
            cls.appid = '21353382'
            cls.ak = '6Kv2IxxO6K7vAwHElovH8Y49'
            cls.sk = 'xViPUYhYIV0I76cH10GnC3I4XbzzPjoF'
            cls.aip_client = AipNlp(cls.appid, cls.ak, cls.sk)
        return cls.aip_client

    @classmethod
    def label(self, title, content):
        return Util.get_aip_client().keyword(title, content, options={})

    @classmethod
    def similar(self, text1, text2):
        return Util.get_aip_client().simnet(text1, text2)


    def request(self, url):
        pass
