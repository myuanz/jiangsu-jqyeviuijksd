from dataclasses import dataclass, field
from typing import Optional

from .school_prefix import prefix


def school_to_prefix(school_name: str) -> Optional[str]:
    """
    获取学校的前缀
    :param school_name: 学校名
    :return: 学校前缀
    """
    ret = prefix.get(school_name)
    if not ret:
        raise Exception(f'找不到学校 {school_name} 对应的前缀')
    return ret


@dataclass
class Constant:
    SCHOOL_NAME: str
    SCHOOL_PREFIX: str = field(init=False)
    ROOT_URL: str = field(init=False)
    CAPTCHA_URL: str = field(init=False)
    LOGIN_URL: str = field(init=False)
    QUESTION_PAGE_URL: str = field(init=False)

    def __post_init__(self):
        self.SCHOOL_PREFIX = school_to_prefix(self.SCHOOL_NAME)
        self.ROOT_URL = f"http://{self.SCHOOL_PREFIX}.91job.org.cn"
        self.CAPTCHA_URL = f"{self.ROOT_URL}/user/captcha/v/5f6eb838209d2"
        self.LOGIN_URL = f"{self.ROOT_URL}/user/login?referer=/contest/question&callback=login"
        self.QUESTION_PAGE_URL = f"{self.ROOT_URL}/contest/question"


const = Constant('南京大学')


def set_const(new_const: Constant) -> Constant:
    global const
    const = new_const
    return const

def get_const() -> Constant:
    global const
    return const
