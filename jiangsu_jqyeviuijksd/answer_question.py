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
            break
        q = next((i for i in questions if i.topic == question))
        save_res = sess.post(const.SAVE_ANSWER_URL, {"value": q.right, "tid": q.id})
        if save_res.json() != {"msg": "ok"}:
            logger.error("出现未期待的返回值: %s", save_res.json())
            break

        logger.info(q.topic)
        logger.info("\t" + "\n\t".join([a.title for a in q.answers]))
        logger.info("\t答案: %s", q.right)
        logger.info("\t解析: %s\n", q.know)

        time.sleep(delay)
