class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.group = -1

    def setGroup(self, group):
        self.group = group

    def getGroup(self):
        return self.group