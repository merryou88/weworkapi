import json

import allure
import pytest
import yaml

from api.baseApi import BaseApi
from api.createMember import CreateMember
from api.gettoken import GetToken


# 读取yaml文件
def yaml_data_with_file(file_name):
    with open('./' + file_name + '.yml', encoding='utf-8') as f:
        return yaml.safe_load(f)


def yaml_data_with_key(file_name, key):
    return yaml_data_with_file(file_name)[key]


class TestCreate(BaseApi):
    @pytest.fixture()
    @pytest.mark.parametrize('env,qid,secret', yaml.safe_load(open('env.yml')))
    def token(self, env, qid, secret):
        t = GetToken()
        return t.gettoken(env, qid, secret)

    @allure.story("测试create接口")
    @pytest.mark.parametrize('env,qid,secret', yaml.safe_load(open('env.yml')))
    @pytest.mark.parametrize('memberinfo', yaml_data_with_key('memberinfo', 'user1'))
    def test_create_case1(self, memberinfo,env,token):
        create_api = env+ "/cgi-bin/user/create"
        c = CreateMember()
        print("memberinfo")
        print(memberinfo)
        with allure.step('添加成员'):
            res = c.create_member(create_api,token,memberinfo)
            print(res)
        #assert res['errcode']=='0'
