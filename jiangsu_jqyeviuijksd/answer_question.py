import logging
import time
from typing import List

import requests
from lxml import etree

from jiangsu_jqyeviuijksd.common import Question, get_const

logger = logging.getLogger(__name__)


def answer_question(sess: requests.Session, questions: List[Question], delay: int = 3):
    const = get_const()
    while True:
        index = sess.get(const.ANSWER_URL)
        root = etree.fromstring(index.content, etree.HTMLParser())
        question = root.xpath('//div[@class="title"]/b/text()')
        if question:
            question = question[0][3:]  # 前三个是废字符
        else:
            logger.info("未找到问题, 退出")
            print(index.text)
            break
        q = next((i for i in questions if i.topic == question))
        print(q)
        proxies = {"http": "http://127.0.0.1:8889", "https": "http://127.0.0.1:8889"}

        to_post = []
        if q.type == 'checkbox':
            to_post = [("value[]", i) for i in q.right] + [("tid", q.id)]
        else:
            to_post = [("value", q.right), ("tid", q.id)]
        save_res = sess.post(const.SAVE_ANSWER_URL, to_post, proxies=proxies)
        print([("value", i) for i in q.right] + [("tid", q.id)])
        if save_res.text != '{"msg":"ok"}':
            logger.error("出现未期待的返回值: %s", save_res.text)
            break

        logger.info(q.topic)
        for a in q.answers:
            logger.info("\t" + a.title)
        logger.info("\t答案: %s", q.right)
        logger.info("\t解析: %s\n", q.know)

        time.sleep(delay)
