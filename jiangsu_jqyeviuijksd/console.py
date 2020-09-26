from pathlib2 import Path

import click
import logging

from .common import get_const, get_question_from_file

logger = logging.getLogger(__name__)


@click.group()
def main():
    print("面!")


@main.command()
@click.option("-u", help="学号")
@click.option("-p", help="密码")
@click.option("-s", help="学校名")
def get_sess(u: str, p: str, s: str):
    """使用用户名和密码获取会话, 自动计算验证码"""
    from .get_session import get_session

    sess = get_session(u, p, s)
    print(sess)


@main.command()
@click.option("-u", help="学号")
@click.option("-p", help="密码")
@click.option("-s", help="学校名")
def get_question_and_save(u: str, p: str, s: str):
    """获取答案并保存"""
    from .get_question import get_question
    from .get_session import get_session

    sess = get_session(u, p, s)
    questions = get_question(sess, Path('./questions.json').absolute)

    logger.debug(questions)


@main.command()
@click.option("-u", help="学号")
@click.option("-p", help="密码")
@click.option("-s", help="学校名")
@click.option("--delay", help="两个问题之间的延时/s, 默认为 3s", default=3)
def answer_question(u: str, p: str, s: str, delay: int):
    from .answer_question import answer_question
    from .get_session import get_session
    path = Path('./questions.json').absolute()
    questions = get_question_from_file(path)
    sess = get_session(u, p, s)
    answer_question(sess, questions, delay)
