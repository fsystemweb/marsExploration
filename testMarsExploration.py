import unittest
from unittest.mock import patch
from models import marsExploration


class TestMarsExploration(unittest.TestCase):
    @patch('models.marsExploration.readInput', return_value='X')
    def test_readInput(self, input):
        self.assertEqual(marsExploration.readInput(), 'X')

    def test_validateCoordinatesSize(self):
        self.assertTrue(marsExploration.validateCoordinatesSize("validSize"))
        self.assertFalse(marsExploration.validateCoordinatesSize(
            "invalidCordinateinvalidCordinateinvalidCordinateinvalidCordinateinvalidCordinate"))

    def test_validatePoints(self):
        self.assertTrue(marsExploration.validatePoints("03"))
        self.assertTrue(marsExploration.validatePoints("51"))
        self.assertFalse(marsExploration.validatePoints("0N"))
        self.assertFalse(marsExploration.validatePoints("UU"))

    def test_validateCardinalPoints(self):
        self.assertTrue(marsExploration.validateCardinalPoints("N"))
        self.assertTrue(marsExploration.validateCardinalPoints("W"))
        self.assertFalse(marsExploration.validateCardinalPoints("B"))
        self.assertFalse(marsExploration.validateCardinalPoints("2"))

    def test_validateDirections(self):
        self.assertTrue(marsExploration.validateDirections("RRR"))
        self.assertTrue(marsExploration.validateDirections("LLL"))
        self.assertTrue(marsExploration.validateDirections("FFF"))
        self.assertTrue(marsExploration.validateDirections("FLR"))
        self.assertFalse(marsExploration.validateDirections("DJK"))
        self.assertFalse(marsExploration.validateDirections("RLJ"))
        self.assertFalse(marsExploration.validateDirections("IOR"))

    def test_isAMove(self):
        self.assertTrue(marsExploration.isAMove("F"))
        self.assertFalse(marsExploration.isAMove("L"))
        self.assertFalse(marsExploration.isAMove("R"))

    def test_isLost(self):
        self.assertTrue(marsExploration.isLost("65"))
        self.assertFalse(marsExploration.isLost("11"))
        self.assertFalse(marsExploration.isLost("23"))
        self.assertTrue(marsExploration.isLost("26"))
        self.assertTrue(marsExploration.isLost("-12"))

    def test_saveLostPosition(self):
        marsExploration.lostPositions = []
        self.assertEqual(0, len(marsExploration.lostPositions))

        marsExploration.saveLostPosition("65N")

        self.assertEqual("65N", marsExploration.lostPositions[0])

    def test_checkLostPosition(self):
        marsExploration.lostPositions = ["65N"]
        self.assertTrue(marsExploration.checkLostPosition("65N"))
        self.assertFalse(marsExploration.checkLostPosition("56N"))
