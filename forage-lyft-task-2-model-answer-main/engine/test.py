import unittest
import capulet_engine

class TestCapuletEngine(unittest.TestCase):

    def test_constructor(self):
        result = capulet_engine.__init__(100_000 ,3000)
        self.assertGreater(result, 30_000)


if __name__ == '__main__':
    unittest.main()