import unittest
from unittest.mock import patch
from models.coordinate import Coordinate


class TestCoordinate(unittest.TestCase):

    def test_extractDirections(self):
        coordinate = Coordinate("01N FRL")

        self.assertEqual("FRL", coordinate.getDirections())

    def test_extractPointsInPlane(self):
        coordinate = Coordinate("01N FRL")

        self.assertEqual("01", coordinate.getPointsInPlane())

    def test_extractCardinalPoint(self):
        coordinate = Coordinate("01N FRL")

        self.assertEqual("N", coordinate.getCardinalPoint())

    def test_getNewDirection(self):
        coordinate = Coordinate("00N FRL")

        self.assertEqual(coordinate.getNewDirection(), "01N")
