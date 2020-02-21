import requests
import pytest
import allure
def setup():
    print("整个模块开始的时候只运行一次")
def teardown():
    print("整个模块结束时候运行一次")
@allure.feature("步骤一：登录获取token")
def test_one():
    url = 'https://admin.rxall.com/admin/view/user/adminLogin'
    body = {
        "userMail":"admin@admin.com" ,
        "userPassword": "21232f297a57a5a743894a0e4a801fc3"
    }
    headers = {
        "Content-Type": "application/json"
    }
    r = requests.post(url, json=body, headers=headers)
    try:
        result = r.json()
        # print(result)
        token = result['data']
        print(token)
        return token
    except Exception as msg:
        print("获取失败原因：%s" %msg)
        print("返回结果：%s"%r.text)
        return ""
@allure.feature("步骤二：登录获取详情")
def test_two():
    url = 'https://admin.rxall.com/admin/view/user/info'
    headers = {
        "Content-Type": "application/json",
        "Authorization": test_one()
    }
    r = requests.get(url, headers=headers)
    result = r.json()
    a= result["status"]
    print(a)
    print(result)
    assert a == 1
# if __name__ == '__main__':
#     pytest.main(['-s','test_a.py'])