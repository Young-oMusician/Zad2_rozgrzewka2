from Point import Point
from Center import Center
from Kmeans import Kmeans
import random

def circleCheck(x0,y0,r,x,y):
    check = True
    tmp = (x - x0)**2 + (y - y0)**2

    if tmp > r:
        check = False

    return check

def main():
    points = []
    centers = []
    r = 2
    x01 = -3
    y01 = 0
    x02 = 3
    y02 = 0
    centersNumber = 2
    i = 0
    # losowanie punktów
    while i < 100:
        tmpX = random.uniform(x01 - r, x01 + r)
        tmpY = random.uniform(y01 - r, y01 + r)
        check = circleCheck(x01, y01, r, tmpX, tmpY)
        if check:
            points.append(Point(tmpX, tmpY))
            i += 1
    i = 0
    while i < 100:
        tmpX = random.uniform(x02 - r, x02 + r)
        tmpY = random.uniform(y02 - r, y02 + r)
        check = circleCheck(x02, y02, r, tmpX, tmpY)
        if check:
            points.append(Point(tmpX,tmpY))
            i += 1
    i = 0
    while i < centersNumber:
        centers.append(Center(random.uniform(-10,10), random.uniform(-10,10), i))
        i += 1
    kmean = Kmeans(points, centers, 1)
    while not kmean.kMeans():
        centers.clear()
        i = 0
        while i < centersNumber:
            centers.append(Center(random.uniform(-10, 10), random.uniform(-10, 10), i))
            i += 1
        kmean.setCenters(centers)
    kmean.plotError()
if __name__ == "__main__":
    main()