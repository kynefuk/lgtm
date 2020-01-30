import click


# Clickでは@click.commandを付けた関数を呼び出すと実行される
@click.command()
def cli():
    lgtm()
    click.echo('lgtm')


def lgtm():
    # ここにロジックを書く
    pass