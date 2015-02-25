from string_lists import list1, list2
from pprint import pprint
from parsers import get_parsers


class StringParser():

    # PUBLIC
    def parse_string_list(self, str_list):

        results = {}

        for str_element in str_list:
            category, res = self._parse_string(str_element)

            if category and res:
                # create category in results, if non existent
                self._create_category(results, category)

                results[category].append(res)

            else:
                print str_element, " - ", "could not be parsed!"

        return results

    # PRIVATE
    def _parse_string(self, str_element):
        category, res = None, None

        # ask parsers for input validation
        for parser_class in get_parsers():
            if parser_class.accepts(str_element):

                parser = parser_class()
                res = parser.parse(str_element)
                category = parser.CATEGORY
                break

        return category, res

    def _create_category(self, results, category):

        # an empty list is needed to append first result of category
        if category not in results:
            results[category] = []


def main():

    sp = StringParser()
    res = sp.parse_string_list(list1)
    res = sp.parse_string_list(list2)

    print "\n"
    pprint(res)


if __name__ == '__main__':
    main()
