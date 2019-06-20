import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
noves_fora = getattr(undertest, 'noves_fora', None)

class PublicTests(unittest.TestCase):

   def test_exemplo(self):
     assert noves_fora([9, 7, 5, 4, 3, 1]) == (2, [[9, 7, 5, 4, 3, 1], [7, 5, 4, 3, 1], [4, 3, 3, 1], [7, 3, 1], [1, 1], [2]])

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
