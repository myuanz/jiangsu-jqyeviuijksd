import os
from dataclasses import dataclass, field
from json import loads
from typing import Optional, List
from logging import getLogger

from jiangsu_jqyeviuijksd.school_prefix import prefix

logger = getLogger(__name__)


@dataclass
class Answer:
    id: str
    title: str
    subId: str


@dataclass
class Question:
    id: str
    title: str
    type: str
    topic: str
    right: str
    know: str
    answers: List[Answer]

    @staticmethod
    def from_json(json: str) -> List["Question"]:
        j = loads(json)
        ret = [Question(**dict(i, answers=[Answer(**k) for k in i['answers']])) for i in j]
        return ret


def school_to_prefix(school_name: str) -> Optional[str]:
    """
    获取学校的前缀
    :param school_name: 学校名
    :return: 学校前缀
    """
    ret = prefix.get(school_name)
    if not ret:
        raise Exception(f"找不到学校 {school_name} 对应的前缀")
    return ret


@dataclass
class Constant:
    SCHOOL_NAME: str
    SCHOOL_PREFIX: str = field(init=False)
    ROOT_URL: str = field(init=False)
    CAPTCHA_URL: str = field(init=False)
    LOGIN_URL: str = field(init=False)
    QUESTION_PAGE_URL: str = field(init=False)
    ANSWER_URL: str = field(init=False)
    SAVE_ANSWER_URL: str = field(init=False)

    def __post_init__(self):
        self.SCHOOL_PREFIX = school_to_prefix(self.SCHOOL_NAME)
        self.ROOT_URL = f"http://{self.SCHOOL_PREFIX}.91job.org.cn"
        self.CAPTCHA_URL = f"{self.ROOT_URL}/user/captcha/v/5f6eb838209d2"
        self.LOGIN_URL = (
            f"{self.ROOT_URL}/user/login?referer=/contest/question&callback=login"
        )
        self.QUESTION_PAGE_URL = f"{self.ROOT_URL}/contest/question"
        self.ANSWER_URL = f"{self.ROOT_URL}/contest/answer"
        self.SAVE_ANSWER_URL = f"{self.ROOT_URL}/contest/savedata"


const = Constant("南京大学")


def set_const(new_const: Constant) -> Constant:
    global const
    const = new_const
    return const


def get_const() -> Constant:
    global const
    return const


def get_question_from_file(filepath: str) -> List[Question]:
    if not os.path.exists(filepath):
        raise Exception("未找到问题文件, 请运行 `js-job get-question-and-save` 以获取")

    with open(filepath, "r") as f:
        json_str = f.read()

    return Question.from_json(json_str)
