import requests
from aip import AipNlp


class Util:
    pass

    def __init__(self):
        pass
        self.appid = '21353382'
        self.ak = '6Kv2IxxO6K7vAwHElovH8Y49'
        self.sk = 'xViPUYhYIV0I76cH10GnC3I4XbzzPjoF'
        self.client = AipNlp(self.appid, self.ak, self.sk)
        # self.get_token()

    def label(self, title, content):
        # request_url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/keyword?charset=UTF-8&access_token=" + self.token
        # params = {"title": title, 'content': content}
        # header = {'Content-Type': 'application/json'}
        return self.client.keyword(title, content,options={})

        # print(params)
        # response = requests.post(request_url, data=params, headers=header)
        # print(response.json())
        # exit()
        # return response.json()

        pass

    def similar(self, text1, text2):
        return self.client.simnet(text1, text2)

    # def
    def get_token(self):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' % (
            self.ak, self.sk)
        print(host)
        response = requests.get(host)
        print(response)
        if response:
            self.token = response.json()['access_token']
            return True, response.json()['access_token']
        raise Exception("get token error.")

        return False, False

    def request(self, url):
        pass
