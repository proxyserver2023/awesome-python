import unittest
from xml.etree import ElementTree
from urllib.parse import parse_qs, urlparse


class AlipayTests(unittest.TestCase):
    def Alipay(self, *args, **kwargs):
        from alipay import Alipay
        return Alipay(*args, **kwargs)

    def WapAlipay(self, *a, **kw):
        from alipay import WapAlipay
        return WapAlipay(*a, **kw)

    def setUp(self):
        self.alipay = self.Alipay(
            pid='pid',
            key='key',
            seller_email='abc@gmail.com'
        )
        self.wapalipay = self.WapAlipay(
            pid='pid',
            key='key',
            seller_email='abc@gmail.com'
        )

    def test_create_direct_pay_by_user_url(self):
        params = {
            'out_trade_no': '1',
            'subject': 'test',
            'price': '0.01',
            'quantity': 1
        }
        self.assertIn(
            'create_direct_pay_by_user',
            self.alipay.create_direct_pay_by_user_url(**params)
        )

    def test_create_direct_pay_by_user_url_with_unicode(self):
        params = {'out_trade_no': '1',
                  'subject': u'测试',
                  'price': '0.01',
                  'quantity': 1}
        self.assertIn('create_direct_pay_by_user',
                      self.alipay.create_direct_pay_by_user_url(**params))

