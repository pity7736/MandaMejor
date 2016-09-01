import datetime
import unittest

from ..utils.parse_datetime import ParseDatetime


class ParseDatetimeTests(unittest.TestCase):

    def test_parse_from_day_month_year(self):
        parse = ParseDatetime('30-08-2016')
        datetime_parsed = parse.get_parsed()

        self.assertIsInstance(datetime_parsed, datetime.datetime)
        self.assertEqual(datetime_parsed.day, 30)
        self.assertEqual(datetime_parsed.month, 8)
        self.assertEqual(datetime_parsed.year, 2016)
