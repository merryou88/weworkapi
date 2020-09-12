import allure
import pytest
import yaml

from api.gettoken import GetToken


@pytest.mark.parametrize('env,qid,secret', yaml.safe_load(open('env.yml')))
class TestGettoken:

    @allure.story("测试获取token")
    def test_gettoken_case1(self, env, qid, secret):
        tok = GetToken()
        token = tok.gettoken(env, qid, secret)
        print('获得了token')
        return token
