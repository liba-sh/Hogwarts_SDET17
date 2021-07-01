import requests

class TestAddress:
    def setup(self):
        self.token=self.get_token()

    def get_token(self):
        url="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww1b63c2e3cf04ceda&corpsecret=noZe_hDqR91rC_swcoStmY5bxvPWhbf_6XTol_hDUQY"
        r=requests.get(url)
        return r.json()['access_token']

    def test_get_information(self):
        userid='test002'
        url=f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}'
        r=requests.get(url)
        print(r.json())

    def test_create_member(self):
        url=f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}'
        data={
            "userid": "m78001",
            "name": "奥特曼",
            "mobile": "+86 13800004444",
            "department": [1]}
        r=requests.post(url,json=data)
        print(r.json())

    def test_update(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        data = {
            "userid": "m78001",
            "name": "迪迦"
        }
        r = requests.post(url, json=data)
        print(r.json())

    def test_delete(self):
        user_id = "m78001"
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={user_id}'
        r = requests.get(url)
        print(r.json())