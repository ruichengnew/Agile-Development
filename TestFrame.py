import unittest
from bowling import Frame
from bowling import Game

class TestFrame(unittest.TestCase):


    def test_ScoreNoThrows(self):
        f = Frame.Frame()
        self.assertEqual(f.getScore(), 0)

    def test_addOneThrow(self):
        f = Frame.Frame()
        f.add(5)
        self.assertEqual(f.getScore(), 5)

    def test_oneThrows(self):
        g = Game.Game()
        g.add(5)
        g.add(4)  #If there is only one throw here, we will meet a error with no eanough throws to decide whether spare or not.
        self.assertEqual(g.score(), 9)

if __name__ == '__main__':
    unittest.main()
