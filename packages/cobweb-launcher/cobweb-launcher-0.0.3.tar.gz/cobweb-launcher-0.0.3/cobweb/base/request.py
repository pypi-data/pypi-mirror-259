import random
from typing import Union

import requests


class Request:

    def __init__(self):
        pass


def gen_user_agent(platform: str = 'android', redis_client=None):
    user_agent = ''
    if platform == 'android':
        os_version = f'{random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}'
        model = (redis_client and redis_client.srandmember('(md)set_android_model').decode()) or ''
        webkit_version = f'{random.randint(450, 550)}.{random.randint(0, 100)}.{random.randint(0, 100)}'
        version = f'{random.randint(3, 6)}.{random.randint(0, 9)}.{random.randint(0, 9)}'
        chrome_version = f'{random.randint(50, 88)}.{random.randint(0, 9)}.{random.randint(1000, 5000)}.{random.randint(0, 1000)}'
        user_agent = f'Mozilla/5.0 (Linux; U; Android {os_version}; zh-cn; {model} Build/{model}) AppleWebKit/{webkit_version} (KHTML, like Gecko) Version/{version} Chrome/{chrome_version} Mobile Safari/{webkit_version}'
    elif platform == 'iphone':
        os_version = f'{random.randint(5, 13)}_{random.randint(0, 9)}_{random.randint(0, 9)}'
        webkit_version = f'{random.randint(550, 650)}.{random.randint(0, 100)}.{random.randint(0, 100)}'
        version = f'{random.randint(4, 13)}.{random.randint(0, 9)}.{random.randint(0, 9)}'
        user_agent = f'Mozilla/5.0 (iPhone; CPU iPhone OS {os_version} like Mac OS X) AppleWebKit/{webkit_version} (KHTML, like Gecko) Version/{version} Mobile Safari/{webkit_version}'

    return user_agent


def config(
        url,
        method: str = "GET",
        headers: dict = None,
        proxies: dict = None,
        cookies: dict = None,
        params: dict = None,
        timeout: int = None,
        stream: bool = False,
        data: Union[dict, str, tuple] = None,
) -> dict:
    if not headers:
        headers = {"accept": "*/*", "user-agent": gen_user_agent()}

    elif "user-agent" not in [key.lower() for key in headers.keys()]:
        headers["user-agent"] = gen_user_agent()

    return {
        "method": method,
        "url": url,
        "data": data,
        "params": params,
        "cookies": cookies,
        "headers": headers,
        "proxies": proxies,
        "stream": stream,
        "timeout": timeout or 3,
    }


def request(**kwargs):
    return requests.request(**kwargs)
