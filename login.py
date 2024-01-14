import mechanize
import http.cookiejar
from datetime import datetime
import sys
import re
import json
import os
import argparse
import requests

# Log in with your account and password to obtain cookies


def login(account, password):
    br = mechanize.Browser()
    cj = http.cookiejar.LWPCookieJar()
    br.set_cookiejar(cj)  # 关联cookies

    # 设置一些参数，因为是模拟客户端请求，所以要支持客户端的一些常用功能，比如gzip,referer等
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    # 这个是degbug##你可以看到他中间的执行过程，对你调试代码有帮助
    br.set_debug_http(True)
    # br.set_debug_redirects(True)
    # br.set_debug_responses(True)

    br.addheaders = [
        ('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')]  # 模拟浏览器头

    # 设定登陆url
    response = br.open('https://www.postcrossing.com/login')
    print("--------------------")

    br.select_form(nr=0)  # 选择表单1，
    br.form['signin[username]'] = account
    br.form['signin[password]'] = password

    # 将标准输出重定向到文件
    sys.stdout = open('log.txt', 'w')
    response = br.submit()  # 提交表单
    # 恢复标准输出
    sys.stdout = sys.__stdout__

    # 读取文件内容
    with open('log.txt', 'r') as file:
        content = file.read()

    # 使用正则表达式提取目标字符串中的内容
    pattern_host = r'Set-Cookie: __Host-postcrossing=(.*?);'
    pattern_remember = r'Set-Cookie: PostcrossingRemember=(.*?);'

    match_host = re.search(pattern_host, content)
    match_remember = re.search(pattern_remember, content)

    # 提取到的内容
    if match_host:
        extracted_host = match_host.group(1)
    else:
        extracted_host = None
        print("账号/密码错误，已退出")
        os.remove("log.txt")
        raise SystemExit(
            "Account/password error.\n\n账号/密码错误")  # 引发异常并退出程序

    if match_remember:
        extracted_remember = match_remember.group(1)

    Cookie = f"__Host-postcrossing={extracted_host}; PostcrossingRemember={extracted_remember}"
    print("Cookie_new:", Cookie)
    os.remove("log.txt")
    return Cookie

# download your own sent.json/received.json


def getUpdateID(account, type, Cookie):
    headers = {
        'Host': 'www.postcrossing.com',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Fetch-Site': 'same-origin',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Sec-Fetch-Mode': 'cors',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0.1 Mobile/15E148 Safari/604.1',
        'Connection': 'keep-alive',
        'Referer': f'https://www.postcrossing.com/user/{account}/{type}',
        'Cookie': Cookie,
        'Sec-Fetch-Dest': 'empty'
    }
    url = f'https://www.postcrossing.com/user/{account}/data/{type}'
    response = requests.get(url, headers=headers).json()
    with open(f"./data/{account}_{type}.json", 'w') as f:
        json.dump(response, f, indent=2)


def getUserStat(account, Cookie):
    headers = {
        'Host': 'www.postcrossing.com',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Fetch-Site': 'same-origin',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Sec-Fetch-Mode': 'cors',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0.1 Mobile/15E148 Safari/604.1',
        'Connection': 'keep-alive',
        'Referer': f'https://www.postcrossing.com/user/{account}/stats',
        'Cookie': Cookie,
        'Sec-Fetch-Dest': 'empty'
    }
    url = f'https://www.postcrossing.com/user/{account}/feed'
    a_data = requests.get(url, headers=headers).json()
    with open(f"./data/{account}_UserStats.json", "w") as file:
        json.dump(a_data, file, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("account", help="input your account")
    parser.add_argument("password", help="input your password")
    options = parser.parse_args()

    account = options.account
    password = options.password

    Cookie = login(account, password)
    getUpdateID(account, "sent", Cookie)
    getUpdateID(account, "received", Cookie)
    getUserStat(account, Cookie)
