from pathlib2 import Path

import click
import logging

from jiangsu_jqyeviuijksd.common import get_const, get_question_from_file

logger = logging.getLogger(__name__)


@click.group()
def main():
    print("仅供 Python 和 HTTP 相关知识的学习交流只用, 勿用于其他途径, 作者不承担任何连带责任")
    print()

@main.command()
@click.option("-u", help="学号", required=True)
@click.option("-p", help="密码", required=True)
@click.option("-s", help="学校名", required=True)
def get_sess(u: str, p: str, s: str):
    """使用用户名和密码获取会话, 自动计算验证码"""
    from jiangsu_jqyeviuijksd.get_session import get_session

    sess = get_session(u, p, s)
    print(sess)


@main.command()
@click.option("-u", help="学号", required=True)
@click.option("-p", help="密码", required=True)
@click.option("-s", help="学校名", required=True)
def get_question_and_save(u: str, p: str, s: str):
    """获取答案并保存, 需特殊条件, 除研究外勿用"""
    from jiangsu_jqyeviuijksd.get_question import get_question
    from jiangsu_jqyeviuijksd.get_session import get_session

    sess = get_session(u, p, s)
    questions = get_question(sess, Path('./questions.json').absolute)

    logger.debug(questions)


@main.command()
@click.option("-u", help="学号", required=True)
@click.option("-p", help="密码", required=True)
@click.option("-s", help="学校名", required=True)
@click.option("--delay", help="两个问题之间的延时/s, 默认为 3s", default=3)
def answer_question(u: str, p: str, s: str, delay: int):
    """使用本命令自动做题"""
    from jiangsu_jqyeviuijksd.answer_question import answer_question
    from jiangsu_jqyeviuijksd.get_session import get_session
    path = Path('./questions.json').absolute()
    questions = get_question_from_file(path)
    sess = get_session(u, p, s)
    answer_question(sess, questions, delay)
