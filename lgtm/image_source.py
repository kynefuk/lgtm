import requests
from io import BytesIO
from pathlib import Path


class LocalImage:
    """ファイルから画像を取得する"""

    def __init__(self, path):
        self._path = path

    def get_image(self):
        return open(self._path, 'rb')


class RemoteImage:
    """URLから画像を取得する"""

    def __init__(self, path):
        self._url = path

    def get_image(self):
        data = requests.get(self._url)
        # バイトデータをファイルオブジェクトに変換
        return BytesIO(data.content)


class _LoremFlickr(RemoteImage):
    """キーワードから画像を取得する"""

    LOREM_FLICKR_URL = 'https://loremflickr.com'
    WIDTH = 800
    HEIGHT = 600

    def __init__(self, keyword):
        super().__init__(self._build_url(keyword))

    def _build_url(self, keyword):
        return (f'{self.LOREM_FLICKR_URL}/'
                f'{self.WIDTH}/{self.HEIGHT}/{keyword}')


# KeywordImageという別名で参照できるようにしておくと
# 将来LoremFlickrから別の画像検索サービスへの以降が必要に
# なったとしても、内部のクラスを差し替えるだけで済むため、保守性が向上
KeywordImage = _LoremFlickr


# コンストラクタとして利用するため
# 単語を大文字始まりにしてクラスのように見せる

def ImageSource(keyword):
    """最適なイメージソースクラスを返す"""

    # コマンドライン引数の情報を元に内部で適切なクラスを利用して
    # 画像取得を行い、取得した画像のファイルオブジェクトを返す
    if keyword.startswith(('http://', 'https://')):
        return RemoteImage(keyword)
    elif Path(keyword).exists():
        return LocalImage(keyword)
    else:
        return KeywordImage(keyword)


def get_image(keyword):
    """画像のファイルオブジェクトを返す"""
    return ImageSource(keyword).get_image()
