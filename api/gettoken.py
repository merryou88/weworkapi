from api.baseApi import BaseApi


class GetToken(BaseApi):
    def gettoken(self,env,qid,secret):
        data={
            "method":"get",
            "url":f"{env}/cgi-bin/gettoken",
            "params":{
                "corpid":qid,
                "corpsecret":secret
            }
        }
        r=self.send_api(data)
        return r['access_token']
