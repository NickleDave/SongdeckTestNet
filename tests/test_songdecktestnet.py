import unittest
import inspect

import songdeck_test_net
import songdeck


class TestSongdeckTestNet(unittest.TestCase):
    def setUp(self):
        self.songdeck_test_net = songdeck_test_net.SongdeckTestNet()

    def test_attribs(self):
        asn = songdeck.network.AbstractSongdeckNetwork()
        asn_methods = [method[0] for method in inspect.getmembers(asn)
                       if inspect.ismethod(method[1])]
        for asn_method in asn_methods:
            self.assertTrue(hasattr(self.songdeck_test_net, asn_method))


if __name__ == '__main__':
    unittest.main()
