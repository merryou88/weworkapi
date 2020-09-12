from api.baseApi import BaseApi


class CreateMember(BaseApi):
    def create_member(self, env, token,member_info):
        data = {
            "method": "post",
            "url": f"{env}?access_token={token}",
            "json": member_info
        }
        r = self.send_api(data)
        return r
