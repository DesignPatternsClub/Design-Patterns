import unittest
import nose
import os
from bs4 import BeautifulSoup


def load_html_file(path):
    """Call test with a html file of the same name.

    Args:
        path: Relative path where the html file is located."""

    def test_decorator(fn):
        base_path = os.path.join(os.path.dirname(__file__), path)
        file_name = fn.__name__ + ".html"
        file_path = os.path.join(base_path, file_name)

        html_f = open(file_path, "r")

        def test_decorated(self):
            fn(self, html_f)

        return test_decorated
    return test_decorator


class SomeScrapingTest(unittest.TestCase):

    @load_html_file("mock_html_files")
    def test_mock_html_1(self, html_f):

        scrape_this = "I am mock html number 1, scrape me!"

        bs = BeautifulSoup(html_f)
        test_scraped = bs.find("p").get_text()

        self.assertEqual(test_scraped, scrape_this)

    @load_html_file("mock_html_files")
    def test_mock_html_2(self, html_f):

        scrape_this = "I am mock html number 2, scrape me!"

        bs = BeautifulSoup(html_f)
        test_scraped = bs.find("p").get_text()

        self.assertEqual(test_scraped, scrape_this)

    @load_html_file("mock_html_files")
    def test_mock_html_3(self, html_f):

        scrape_this = "I am mock html number 3, scrape me!"

        bs = BeautifulSoup(html_f)
        test_scraped = bs.find("p").get_text()

        self.assertEqual(test_scraped, scrape_this)

    @load_html_file("mock_html_files")
    def test_mock_html_4(self, html_f):

        scrape_this = "I am mock html number 4, scrape me!"

        bs = BeautifulSoup(html_f)
        test_scraped = bs.find("p").get_text()

        self.assertEqual(test_scraped, scrape_this)


if __name__ == '__main__':
    nose.run(defaultTest=__name__)
