import requests


class Base:
    def __init__(self):
        self.s = requests.Session()
        self.token = self.get_token()
        self.s.params = {"access_token": self.token}

    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {"corpid": "ww1b63c2e3cf04ceda",
                  "corpsecret": "noZe_hDqR91rC_swcoStmY5bxvPWhbf_6XTol_hDUQY"}
        r = self.s.get(url, params=params)
        return r.json()['access_token']

    def send(self,*args,**kwargs):
        return self.s.request(*args,**kwargs)
