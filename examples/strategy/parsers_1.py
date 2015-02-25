import re
import pyclbr


class BaseParser(object):

    """BaseParser class for all parsers."""

    # PUBLIC INTERFACE
    @classmethod
    def accepts(cls, str_element):
        return cls._accepts(str_element)

    @classmethod
    def parse(cls, str_element):
        return cls._parse(str_element)

    # PRIVATE METHODS
    @classmethod
    def _accepts(cls, str_element):
        return None

    @classmethod
    def _parse(cls, str_element):
        return None


class TitleParser(BaseParser):

    """Parser for title."""

    CATEGORY = "title"

    @classmethod
    def _accepts(cls, str_element):
        return re.match("TITLE [0-9]+[:]", str_element, re.U)

    @classmethod
    def _parse(cls, title):
        res = {}

        short_str = title.replace("TITLE ", "")
        token = short_str.index(":")

        res["id"] = short_str[:token]
        res["desc"] = short_str[token + 2:]

        return res


class ChapterParser(BaseParser):

    """Parser for chapter."""

    CATEGORY = "chapter"

    @classmethod
    def _accepts(cls, str_element):
        return re.match("[0-9][.][a-z][)]", str_element, re.U)

    @classmethod
    def _parse(cls, chapter):
        res = {}

        token = chapter.index(")")

        res["id"] = chapter[:token]
        res["desc"] = chapter[token + 2:]

        return res


class SubChapterParser(BaseParser):

    """Parser for sub_chapter."""

    CATEGORY = "sub_chapter"

    @classmethod
    def _accepts(cls, str_element):
        return re.match("[0-9][.]", str_element, re.U)

    @classmethod
    def _parse(cls, sub_chapter):
        res = {}

        token = sub_chapter.index(".")

        res["id"] = sub_chapter[:token]
        res["desc"] = sub_chapter[token + 2:]

        return res


class ProductParser(BaseParser):

    """Parser for product."""

    CATEGORY = "product"

    @classmethod
    def _accepts(cls, str_element):
        return re.match("[(]Tariff number [0-9]+[)][.]", str_element, re.U)

    @classmethod
    def _parse(cls, product):
        res = {}

        short_str = product.replace("(Tariff number ", "")
        token = short_str.index(").")

        res["id"] = short_str[:token]
        res["desc"] = short_str[token + 3:]

        return res


def get_parsers():

    list_cls = (pyclbr.readmodule(__name__).keys())
    list_cls_refs = [globals()[cls_name] for cls_name in list_cls]

    return list_cls_refs


if __name__ == '__main__':
    get_parsers()
