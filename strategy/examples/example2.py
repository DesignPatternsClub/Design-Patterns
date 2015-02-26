from string_lists import list2
from pprint import pprint
import re


class StringParser():

    # PUBLIC
    def parse_string_list(self, str_list):

        results = {}

        for str_element in str_list:
            category, res = self._parse_string(str_element)

            # create category in results, if non existent
            self._create_category(results, category)

            results[category].append(res)

        return results

    # PRIVATE
    def _parse_string(self, str_element):

        if "TITLE" in str_element or "title" in str_element:
            category = "title"
            res = self._parse_title(str_element)

        elif re.match("[0-9][.][a-z][)]", str_element, re.U):
            category = "chapter"
            res = self._parse_chapter(str_element)

        elif re.match("[0-9][.,]", str_element, re.U):
            category = "sub_chapter"
            res = self._parse_sub_chapter(str_element)

        elif "Tariff" in str_element or "Tarifi" in str_element:
            category = "product"
            res = self._parse_product(str_element)

        elif re.match("[*]Tariff number [0-9]+[)].",
                      str_element, re.U):
            category = "product"
            res = self._parse_product2(str_element)

        else:
            print "Unidentified string!"
            return None

        return category, res

    def _create_category(self, results, category):

        # an empty list is needed to append first result of category
        if category not in results:
            results[category] = []

    # parsers
    def _parse_title(self, title):
        res = {}

        short_str = title.replace("TITLE ", "")
        short_str = title.replace("title ", "")

        if ":" in short_str:
            token = short_str.index(":")
        elif "." in short_str:
            token = short_str.index(".")
        else:
            print "No token found!"
            return None

        res["id"] = short_str[:token]
        res["desc"] = short_str[token + 2:]

        return res

    def _parse_chapter(self, chapter):
        res = {}

        token = chapter.index(")")

        res["id"] = chapter[:token]
        res["desc"] = chapter[token + 2:]

        return res

    def _parse_sub_chapter(self, sub_chapter):
        res = {}

        if "," in sub_chapter:
            token = sub_chapter.index(",")
        elif "." in sub_chapter:
            token = sub_chapter.index(".")
        else:
            print "No token found!"
            return None

        res["id"] = sub_chapter[:token]
        res["desc"] = sub_chapter[token + 2:]

        return res

    def _parse_product(self, product):
        res = {}

        short_str = product.replace("(Tariff number ", "")
        short_str = product.replace("(Tarifi number ", "")
        short_str = product.replace("*Tariff number ", "")

        token = short_str.index(").")

        res["id"] = short_str[:token]
        res["desc"] = short_str[token + 3:]

        return res

    def _parse_product2(self, product):
        res = {}

        short_str = product.replace("*Tariff number ", "")
        token = short_str.index(").")

        res["id"] = short_str[:token]
        res["desc"] = short_str[token + 3:]

        return res


def main():

    sp = StringParser()
    res = sp.parse_string_list(list2)

    print "\n"
    pprint(res)


if __name__ == '__main__':
    main()
