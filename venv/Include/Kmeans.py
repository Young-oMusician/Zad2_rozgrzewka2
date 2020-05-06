import random
import matplotlib.pyplot as plt
import numpy as np

class Kmeans:

    def __init__(self, points, centers, epsilon):
        self.points = points
        self.centers = centers
        self.epsilon = epsilon
        self.meanErrors = []

    def plot(self, minxlim, maxxlim, minylim, maxylim, iteration):
        x = []
        y = []
        for point in self.points:
            x.append(point.x)
            y.append(point.y)
        cX = []
        cY = []
        for center in self.centers:
            cX.append(center.x)
            cY.append(center.y)
        plt.plot(x, y, 'k.')
        plt.plot(cX, cY, 'r.')
        plt.title("Iteration "+str(iteration))
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.xlim(minxlim, maxxlim)
        plt.ylim(minylim, maxylim)
        plt.savefig("k" + str(len(self.centers)) + "\k"+str(len(self.centers))+"_it_"+str(iteration)+".png")
        plt.close()
        print("Iteration "+str(iteration))

    def plotError(self):
        x = np.linspace(0, len(self.meanErrors), len(self.meanErrors))
        factors = np.polyfit(x, self.meanErrors, 9)
        plt.plot(x, np.polyval(factors, x), 'g-')
        plt.title("Błąd kwantyzacji dla " + str(len(self.centers)) + " centrów")
        plt.xlabel("Iteracja")
        plt.ylabel("Błąd kwantyzacji")
        plt.xlim(0, len(self.meanErrors))
        plt.grid()
        plt.savefig("blad_kwantyzacji_k" + str(len(self.centers)) + ".png")
        plt.close()

    # szukanie do którego skupienia (centru) należy punkt
    def findWinner(self, point):
        # obliczanie odległości eulkidesowych między punktem a centrami
        distances = []
        for center in self.centers:
            distances.append(center.countDistance(point.x, point.y))
        min = 0
        itDistances = 1
        # szukanie najbliżeszego centra dla punktu
        while itDistances < len(distances):
            if distances[min] > distances[itDistances]:
                min = itDistances
            itDistances += 1
        return min

    # sprawdzanie czy centr jest martwy
    def isDead(self, centerGroup):
        for point in self.points:
            if point.getGroup() == centerGroup:
                return False
        return True

    # obliczanie nowych współrzędnych centru
    def countNewCenters(self):
        # podzielenie punktów na grupy skupień
        group = []
        for center in self.centers:
            group.append([])
        for point in self.points:
            group[point.getGroup()].append(point)
        # obliczanie nowych współrzędnych centrów jako średnia a. współrzędnych punktów grupy
        newCenterX = 0
        newCenterY = 0
        itCenterGroup = 0
        while itCenterGroup < len(self.centers):
            for point in group[itCenterGroup]:
                newCenterX += point.x
                newCenterY += point.y
            newCenterX /= len(group[itCenterGroup])
            newCenterY /= len(group[itCenterGroup])
            self.centers[itCenterGroup].x = newCenterX
            self.centers[itCenterGroup].y = newCenterY
            itCenterGroup += 1

    def countMeanError(self):
        # i = 0
        # result = 0
        # for center in self.centers:
        #     result += center.meanError()
        #     i += 1
        # result /= len(self.centers)
        # return result
        result = 0
        for point in self.points:
            result += self.centers[point.group].countDistance(point.x, point.y)
        result /= len(self.points)
        return result

    def redefineGroups(self):
        for point in self.points:
            point.setGroup(-1)
            
    def setCenters(self, centers):
        self.centers = centers

    def kMeans(self):
        iteration = 0
        random.shuffle(self.points)
        for point in self.points:
            point.setGroup(self.findWinner(point))
        itCenterGroups = 0;
        while itCenterGroups < len(self.centers):
            if self.isDead(itCenterGroups):
                return False
            itCenterGroups += 1
        self.plot(-10,10,-10,10,iteration)
        self.meanErrors.append(self.countMeanError())
        self.countNewCenters()
        while self.meanErrors[iteration] >= self.epsilon:
            self.redefineGroups()
            random.shuffle(self.points)
            for point in self.points:
                point.setGroup(self.findWinner(point))
            iteration += 1
            self.plot(-10,10,-10,10,iteration)
            self.meanErrors.append(self.countMeanError())
            self.countNewCenters()
        return True




