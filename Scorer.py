class Scorer(object):

    def __init__(self):
        self.itsThrows = []
        self.itsCurrentThrow = 0

    def addThrow(self, pins):
        self.itsThrows.insert(self.itsCurrentThrow, pins)
        self.itsCurrentThrow += 1

    def scoreForFrame(self, theFrame):
        score = 0
        self.ball = 0
        for currentFrame in range(theFrame):
            self.firstThrow = self.itsThrows[self.ball]
            if self.strike():
                score += 10 + self.nextTwoBallsForStrike()
                self.ball += 1
            elif self.spare():
                score += 10 + self.nextBallForSpare()
                self.ball += 2
            else:
                score += self.twoBallsInFrame()
                self.ball += 2
        return score

    def strike(self):
        return self.itsThrows[self.ball] == 10

    def spare(self):
        return (self.itsThrows[self.ball] + self.itsThrows[self.ball + 1]) == 10

    def nextTwoBallsForStrike(self):
        return self.itsThrows[self.ball + 1] + self.itsThrows[self.ball + 2]

    def nextBallForSpare(self):
        return self.itsThrows[self.ball + 2]

    def twoBallsInFrame(self):
        return self.itsThrows[self.ball] + self.itsThrows[self.ball + 1]

