import re
import pyclbr
import os
from pprint import pprint


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
        return re.match(cls.VALIDATION_PATTERN, str_element, re.U)

    @classmethod
    def _parse(cls, str_element):
        return None


class BaseTitleParser(BaseParser):

    """Parser for title."""

    CATEGORY = "title"

    @classmethod
    def _parse(cls, title):
        res = {}

        short_str = title.replace(cls.REPLACE_STR, "")
        token = short_str.index(cls.TOKEN)

        res["id"] = short_str[:token]
        res["desc"] = short_str[token + 2:]

        return res


class TitleParser1(BaseTitleParser):

    """Parser 1 for title."""

    VALIDATION_PATTERN = "TITLE [0-9]+[:]"
    REPLACE_STR = "TITLE "
    TOKEN = ":"


class TitleParser2(BaseTitleParser):

    """Parser 1 for title."""

    VALIDATION_PATTERN = "title [0-9]+[.]"
    REPLACE_STR = "title "
    TOKEN = "."


class ChapterParser(BaseParser):

    """Parser for chapter."""

    CATEGORY = "chapter"
    VALIDATION_PATTERN = "[0-9][.][a-z][)]"

    @classmethod
    def _parse(cls, chapter):
        res = {}

        token = chapter.index(")")

        res["id"] = chapter[:token]
        res["desc"] = chapter[token + 2:]

        return res


class BaseSubChapterParser(BaseParser):

    """Parser for sub_chapter."""

    CATEGORY = "sub_chapter"

    @classmethod
    def _parse(cls, sub_chapter):
        res = {}

        token = sub_chapter.index(cls.TOKEN)

        res["id"] = sub_chapter[:token]
        res["desc"] = sub_chapter[token + 2:]

        return res


class SubChapterParser1(BaseSubChapterParser):

    """Parser 1 for sub_chapter."""

    VALIDATION_PATTERN = "[0-9][.]"
    TOKEN = "."


class SubChapterParser2(BaseSubChapterParser):

    """Parser 2 for sub_chapter."""

    VALIDATION_PATTERN = "[0-9][,]"
    TOKEN = ","


class BaseProductParser(BaseParser):

    """Parser for product."""

    CATEGORY = "product"
    TOKEN = ")."

    @classmethod
    def _parse(cls, product):
        res = {}

        short_str = product.replace(cls.REPLACE_STR, "")
        token = short_str.index(cls.TOKEN)

        res["id"] = short_str[:token]
        res["desc"] = short_str[token + 3:]

        return res


class ProductParser1(BaseProductParser):

    """Parser 1 for product."""

    VALIDATION_PATTERN = "[(]Tariff number [0-9]+[)][.]"
    REPLACE_STR = "(Tariff number "


class ProductParser2(BaseProductParser):

    """Parser 2 for product."""

    VALIDATION_PATTERN = "[(]Tarifi number [0-9]+[)][.]"
    REPLACE_STR = "(Tarifi number "


class ProductParser3(BaseProductParser):

    """Parser 3 for product."""

    VALIDATION_PATTERN = "[*]Tariff number [0-9]+[)][.]"
    REPLACE_STR = "*Tariff number "


def get_parsers_names():
    """Returns a list of the parsers names, whith no Base classes."""

    name = os.path.splitext(os.path.basename(__file__))[0]
    list_cls_names = (pyclbr.readmodule(name).keys())
    list_no_base_cls_names = [cls_name for cls_name in list_cls_names
                              if cls_name[:4] != "Base"]

    return list_no_base_cls_names


def get_parsers():
    """Returns a list of references to the parsers classes."""

    return [globals()[cls_name] for cls_name in get_parsers_names()]


if __name__ == '__main__':
    pprint(sorted(get_parsers_names()))
