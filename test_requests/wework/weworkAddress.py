import requests


class WeworkAddress:
    def __init__(self):
        self.token=self.get_token()

    def get_token(self):
        url="https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params={"corpid":"ww1b63c2e3cf04ceda",
                "corpsecret":"noZe_hDqR91rC_swcoStmY5bxvPWhbf_6XTol_hDUQY"}
        r=requests.get(url,params=params)
        return r.json()['access_token']

    def get_information(self,user_id:str):
        """
        获取用户信息
        :param userid:
        :return:
        """
        params={"access_token":self.token,"userid":user_id}
        url='https://qyapi.weixin.qq.com/cgi-bin/user/get'
        r=requests.get(url,params=params)
        return r.json()

    def create_member(self,user_id:str,name:str,mobile:str,department:str):
        """
        创建成员
        :param user_id:
        :param name:
        :param mobile:
        :param department:
        :return:
        """
        url=f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}'
        data={
            "userid": user_id,
            "name": name,
            "mobile": mobile,
            "department": department}
        r=requests.post(url,json=data)
        return r.json()

    def update(self,user_id:str,name:str):
        """
        更新成员
        :param user_id:
        :param name:
        :return:
        """
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        data = {
            "userid": user_id,
            "name": name
        }
        r = requests.post(url, json=data)
        return r.json()

    def delete(self,user_id:str):
        """
        删除成员
        :param user_id:
        :return:
        """
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        params={"access_token":self.token,"userid":user_id}
        r = requests.get(url,params=params)
        return r.json()