import re
from dataclasses import dataclass, asdict
from json import load, loads, dumps, dump
from typing import List
from .common import get_const

import requests


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
    def from_json(json: str) -> List['Question']:
        j = loads(json)
        ret = [Question(**i) for i in j]
        return ret


def get_question(sess: requests.Session) -> List[Question]:
    const = get_const()
    proxies = {"http": "http://127.0.0.1:8889", "https": "http://127.0.0.1:8889"}

    question_page = sess.get(const.QUESTION_PAGE_URL, proxies=proxies)
    json_str = re.findall("(?<=var jsonStr = [']).+(?=['];)", question_page.text)
    if not json_str:
        print(question_page.text)
        raise Exception('未找到题目')
    else:
        json_str = json_str[0]

    with open('./questions.json', 'w') as f:
        f.write(json_str)

    return Question.from_json(json_str)


def get_question_from_file(filepath: str) -> List[Question]:
    with open(filepath, 'r') as f:
        json_str = f.read()
    return Question.from_json(json_str)
