from io import BytesIO
import requests
from typing import Optional
import muggle_ocr
import logging
from faker import Faker
import muggle_ocr
import requests
import re
from dataclasses import dataclass, field
from PIL import Image

from jiangsu_jqyeviuijksd.school_prefix import prefix
from jiangsu_jqyeviuijksd.common import Constant, get_const, set_const

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ocr: Optional[muggle_ocr.SDK] = None
fake = Faker()

if not ocr:
    ocr = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)


def get_session(username: str, password: str, school_name: str) -> requests.Session:
    """
    获取一个登录成功的会话
    :param username: 学号
    :param password: 密码
    :param school_name: 学校
    :return:
    """
    const = set_const(Constant(school_name))

    ua = fake.chrome()
    while "Windows NT" not in ua:
        ua = fake.chrome()
    headers = {"User-Agent": ua}

    sess = requests.Session()
    sess.headers = headers

    max_try = 3
    for i in range(max_try):
        img_res = sess.get(const.CAPTCHA_URL)
        if i != 0:
            img: Image = Image.open(BytesIO(img_res.content))
            img.show()
            captcha = input("请输入验证码: ")
        else:
            captcha = ocr.predict(img_res.content)
        logging.info("captcha 识别结果: %s" % captcha)
        LOGIN_DATA = {
            "username": username,
            "university": "",
            "loginType": "normal",
            "password": password,
            "verifyCode": captcha,
            "loginsubmit": "1",
        }
        login_res = sess.post(const.LOGIN_URL, data=LOGIN_DATA)
        if "验证码不正确" in login_res.text:
            if i == 0:
                logging.error(f"验证码自动识别错误, 进入手动模式")

            if i == max_try - 1:
                raise Exception(f"验证码识别错误, 请重试")
        elif "登录成功" not in login_res.text:
            raise Exception(f"登录未成功, 死亡前消息为: {login_res.text}")
        else:
            logging.info(f"登录成功: {username}")
            return sess
