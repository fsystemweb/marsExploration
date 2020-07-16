import sys
from models.coordinate import Coordinate

lostPositions = []
flagLost = False


def readInput():
    flagLost = False
    print("Welcome, please insert cordinates: ")
    return input()


def validations(coordinate):
    if not validateCoordinatesSize(coordinate.getCoordinateString()):
        print("Error invalid length coordinates")
        return False

    if not validatePoints(coordinate.getPointsInPlane()):
        print("Error invalid points")
        return False

    if not validateCardinalPoints(coordinate.getCardinalPoint()):
        print("Error invalid cardinal point")
        return False

    if not validateDirections(coordinate.getDirections()):
        print("Error invalid directions")
        return False

    return True


def validateCoordinatesSize(coordinateString):
    maxLengthCoordinate = 50
    if len(coordinateString) > maxLengthCoordinate:
        return False
    return True


def validatePoints(pointsInPlane):
    for char in pointsInPlane:
        if not char.isnumeric():
            return False

    return True


def validateCardinalPoints(cardinalPoint):
    validCardinalPoints = ["N", "S", "E", "W"]

    if cardinalPoint in validCardinalPoints:
        return True
    return False


def validateDirections(directions):
    validDirections = ["L", "R", "F"]

    for char in directions:
        if not char in validDirections:
            return False

    return True


def doAMove(nextMove, coordinate):
    if isAMove(nextMove):

        newDirection = coordinate.getNewDirection()

        print("prueba", newDirection)

        if checkLostPosition(newDirection):
            print(
                "The robot can't move in this direction beacuse is a lost position")
            flagLost = True
            return

        if isLost(newDirection):
            saveLostPosition(newDirection)
            print("The robot is lost.")
            flagLost = True
            return

        coordinate.updatePointsInPlane(coordinate.getNewDirection())


def isAMove(direction):
    if direction == "F":
        return True
    return False


def checkLostPosition(direction):
    if direction in lostPositions:
        return True
    return False


def isLost(direction):
    # when have a negative value is lost
    if "-" in direction:
        return True

    max = 5
    min = 0

    if (int(direction[0]) > max):
        return True
    elif (int(direction[1]) > max):
        return True
    elif (int(direction[0]) < min):
        return True
    elif (int(direction[1]) < min):
        return True
    else:
        return False


def saveLostPosition(direction):
    if not direction in lostPositions:
        lostPositions.append(direction)


def askForRunAgain():
    print("Do you want to input new Cordinate?y/n ")
    resp = input()

    if resp.lower() == "y":
        return True
    return False
