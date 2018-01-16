class Frame(object):

    def __init__(self):
        self.itsScore = 0

    def getScore(self):
        return self.itsScore

    def add(self, pins):
        self.itsScore += pins

