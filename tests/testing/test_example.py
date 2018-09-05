# -*- coding: utf-8 -*-
import unittest


class Widget:

    def __init__(self, name):
        self.name = name

    def dispose(self):
        pass


class WidgetTestCase(unittest.TestCase):

    def setUp(self):
        # self.widget = Widget('The Widget')
        pass

    def tearDown(self):
        # self.widget.dispose()
        pass

    def test_widget_resize(self):
        self.assertEqual(
            'foo'.upper(),
            'FOO'
        )

    def test_default_widget_size(self):
        self.assertTrue(
            'TRUE'.isupper()
        )


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(test_suite())
