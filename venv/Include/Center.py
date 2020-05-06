class Center:

    def __init__(self, x, y, group):
        self.x = x
        self.y = y
        self.group = group
        self.errors = []

    def countDistance(self, x, y):
        return ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5

    def countError(self, point):
        self.errors.append(self.countDistance(point.x, point.y))

    def appendError(self, errorValue):
        self.errors.append(errorValue)

    def clearErrors(self):
        self.errors.clear()

    def meanError(self):
        i = 0
        result = 0
        if (len(self.errors) > 0):
            for error in self.errors:
                result += error
                i += 1
            result /= len(self.errors)
        return result
