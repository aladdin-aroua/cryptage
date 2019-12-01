import unittest

from Cesar import Cesar


class TestCesarMethod(unittest.TestCase):

    def test_encryption(self):
        c = Cesar()
        self.assertEqual(c.encryption("informatique"), "lqirupdwltxh")

    def test_decryption(self):
        c = Cesar()
        self.assertEqual(c.decryption("lqirupdwltxh"), "informatique")


if __name__ == '__main__':
    unittest.main()
