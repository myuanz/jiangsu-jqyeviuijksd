import re
from dataclasses import dataclass, asdict
from json import load, loads, dumps, dump
from pathlib2 import Path
from typing import List
from jiangsu_jqyeviuijksd.common import get_const, Question

import requests


def get_question(sess: requests.Session, save_path: Path = None) -> List[Question]:
    const = get_const()

    question_page = sess.get(const.QUESTION_PAGE_URL)
    json_str = re.findall("(?<=var jsonStr = [']).+(?=['];)", question_page.text)
    if not json_str:
        print(const.QUESTION_PAGE_URL, question_page.text)
        raise Exception("未找到题目")
    else:
        json_str = json_str[0]

    if save_path:
        with open(save_path, "w") as f:
            f.write(json_str)

    return Question.from_json(json_str)
