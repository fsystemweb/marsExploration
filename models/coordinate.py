class Coordinate:
    def __init__(self, coordinate):
        self.coordinateString = coordinate
        self.directions = self.extractDirections(coordinate)
        self.cardinalPoint = self.extractCardinalPoint(coordinate)
        self.pointsInPlane = self.extractPointsInPlane(coordinate)

    def extractDirections(self, stringCoordinate):
        lastCharPosition = len(stringCoordinate)
        return self.getStructure(stringCoordinate, 4, lastCharPosition)

    def getStructure(self, stringCoordinate, start, end):
        return (stringCoordinate[start:end])

    def extractCardinalPoint(self, stringCoordinate):
        return self.getStructure(stringCoordinate, 2, 3)

    def extractPointsInPlane(self, stringCoordinate):
        return self.getStructure(stringCoordinate, 0, 2)

    def getDirections(self):
        return self.directions

    def getPointsInPlane(self):
        return self.pointsInPlane

    def getCardinalPoint(self):
        return self.cardinalPoint

    def getCoordinateString(self):
        return self.coordinateString

    def getNewDirection(self):
        positionX = int(self.pointsInPlane[0])
        positionY = int(self.pointsInPlane[1])

        if self.cardinalPoint == "N":
            positionY += 1

        elif self.cardinalPoint == "O":
            positionX -= 1

        elif self.cardinalPoint == "S":
            positionY -= 1

        else:
            positionX += 1

        return str(positionX)+str(positionY)+self.cardinalPoint

    def setDirections(self, newDirections):
        self.directions = newDirections

    def updatePointsInPlane(self, newDirections):
        self.pointsInPlane = self.getStructure(newDirections, 0, 2)
