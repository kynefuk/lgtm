import io
import unittest
from lgtm import image_source


class TestImageSource(unittest.TestCase):
    def test_get_image(self):
        keyword = 'book'
        file = image_source.get_image(keyword)

        self.assertTrue(isinstance(file, io.BytesIO))

    def test_ImageSource_remote(self):
        remote_image_keyword = 'http://'
        image = image_source.ImageSource(remote_image_keyword)

        self.assertTrue(isinstance(image, image_source.RemoteImage))

    def test_ImageSource_local(self):
        local_image_keyword = './output.png'
        source = image_source.ImageSource(local_image_keyword)

        self.assertTrue(isinstance(source, image_source.LocalImage))

    def test_ImageSource_keyword(self):
        keyword_image_keyword = 'book'
        source = image_source.ImageSource(keyword_image_keyword)

        self.assertTrue(isinstance(source, image_source.KeywordImage))
