import sys
from models.coordinate import Coordinate
from models import marsExploration


def main():
    coordinateString = marsExploration.readInput()

    coordinate = Coordinate(coordinateString)

    if not marsExploration.validations(coordinate):
        return

    index = 0
    directionsAux = coordinate.getDirections()
    while True:
        marsExploration.doAMove(directionsAux[index], coordinate)
        index += 1
        if(checkFinish(index, directionsAux) or marsExploration.flagLost):
            break

    print(coordinate.getDirections())

    if marsExploration.askForRunAgain():
        main()

    return


def checkFinish(index, directionsAux):
    return (index == len(directionsAux))


main()
