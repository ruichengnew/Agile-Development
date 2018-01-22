import unittest
from bowling import Game

class TestGame(unittest.TestCase):


    def test_TwoThrowsNoMark(self):
        g = Game.Game()
        g.add(5)
        g.add(4)
        self.assertEqual(g.score(), 9)

    def test_FourThrowsNoMark(self):
        g = Game.Game()
        g.add(5)
        g.add(4)
        g.add(7)
        g.add(2)
        self.assertEqual(g.score(), 18)
        self.assertEqual(g.scoreForFrame(1), 9)
        self.assertEqual(g.scoreForFrame(2), 18)

    def test_SimpleSpare(self):
        g = Game.Game()
        g.add(3)
        g.add(7)
        g.add(3)
        self.assertEqual(g.scoreForFrame(1), 13)

    def test_SimpleFrameAfterSpare(self):
        g = Game.Game()
        g.add(3)
        g.add(7)
        g.add(3)
        g.add(2)
        self.assertEqual(g.scoreForFrame(1), 13)
        self.assertEqual(g.scoreForFrame(2), 18)
        self.assertEqual(g.score(), 18)

    def test_SimpleStrike(self):
        g = Game.Game()
        g.add(10)
        g.add(3)
        g.add(6)
        self.assertEqual(g.scoreForFrame(1), 19)
        self.assertEqual(g.score(), 28)

    def test_PerfectGame(self):
        g = Game.Game()
        for _ in range(12):
            g.add(10)
        self.assertEqual(g.score(), 300)
    
    def test_EndOfArray(self):
        g = Game.Game()
        for _ in range(9):
            g.add(0)
            g.add(0)
        g.add(2)
        g.add(8)
        g.add(10)
        self.assertEqual(g.score(), 20)

    def test_SampleGame(self):
        g = Game.Game()
        g.add(1)
        g.add(4)
        g.add(4)
        g.add(5)
        g.add(6)
        g.add(4)
        g.add(5)
        g.add(5)
        g.add(10)
        g.add(0)
        g.add(1)
        g.add(7)
        g.add(3)
        g.add(6)
        g.add(4)
        g.add(10)
        g.add(2)
        g.add(8)
        g.add(6)
        self.assertEqual(g.score(), 133)
       
    def test_HeartBreak(self):
        g = Game.Game()
        for _ in range(11):
            g.add(10)
        g.add(9)
        self.assertEqual(g.score(), 299)

    def test_TenthFrameSpare(self):
        g = Game.Game()
        for _ in range(9):
            g.add(10)
        g.add(9)
        g.add(1)
        g.add(1)
        self.assertEqual(g.score(), 270)


if __name__ == '__main__':
    unittest.main()
