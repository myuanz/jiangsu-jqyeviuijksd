import click


@click.group()
def main():
    print("面!")


@main.command()
@click.option('-u', help='学号')
@click.option('-p', help='密码')
@click.option('-s', help='学校名')
def get_sess(u: str, p: str, s: str):
    """使用用户名和密码获取会话, 自动计算验证码"""
    from .get_session import get_session
    sess = get_session(u, p, s)
    print(sess)