import click
import logging
from lgtm.drawer import save_with_message
from lgtm.image_source import get_image
from lgtm.logging import log_info_deco


logger = logging.getLogger('basicLogger')

# Clickでは@click.commandを付けた関数を呼び出すと実行される
@click.command()
@click.option('--message', '-m', default='LGTM', show_default=True, help='画像に乗せる文字列')
@click.argument('keyword')
def cli(**kwargs):
    """LGTM画像生成ツール"""

    keyword = kwargs['keyword']
    message = kwargs['message']

    lgtm(keyword, message)


@log_info_deco(logger)
def lgtm(keyword, message):
    # ファイルオブジェクトはコンテキストマネージャ
    with get_image(keyword) as fp:
        save_with_message(fp, message)
