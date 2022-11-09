import unittest

from order import Order


class TestOrderClass(unittest.TestCase):
    def test_01_valid_order(self):
        text = "GBPJPY BUY NOW @ 168.59\n\nSL: 168.30\n\nTP1:168.79\nTP2:169.09"
        order = Order(text)
        self.assertEqual(order.is_valid(), True)

    def test_02_valid_order(self):
        text = "GBPJPY BUY NOW @ 168.59\n\nTP1:168.79\nTP2:169.09"
        order = Order(text)
        self.assertEqual(order.is_valid(), False)



if __name__ == '__main__':
    unittest.main()
