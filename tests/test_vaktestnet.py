import unittest
import inspect

import vak_test_net
import vak


class TestVakTestNet(unittest.TestCase):
    def setUp(self):
        self.vak_test_net = vak_test_net.VakTestNet()

    def test_attribs(self):
        avn = vak.network.AbstractVakNetwork()
        avn_methods = [method[0] for method in inspect.getmembers(avn)
                       if inspect.ismethod(method[1])]
        for avn_method in avn_methods:
            self.assertTrue(hasattr(self.vak_test_net, avn_method))


if __name__ == '__main__':
    unittest.main()
