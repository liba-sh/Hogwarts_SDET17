import requests

from interface_weixin.wework.base import Base


class WeworkAddress(Base):


    def get_information(self,user_id:str):
        """
        获取用户信息
        :param userid:
        :return:
        """
        params = {"userid":user_id}
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        r = self.send("GET",url,params=params)
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
        url=f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data={
            "userid": user_id,
            "name": name,
            "mobile": mobile,
            "department": department}
        r=self.send("POST",url,json=data)
        return r.json()

    def update(self,user_id:str,name:str):
        """
        更新成员
        :param user_id:
        :param name:
        :return:
        """
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data = {
            "userid": user_id,
            "name": name
        }
        r = self.send("POST",url, json=data)
        return r.json()

    def delete(self,user_id:str):
        """
        删除成员
        :param user_id:
        :return:
        """
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        params={"userid":user_id}
        r = self.send("GET",url,params=params)
        return r.json()