import unittest
from flight import Flight, Vertex, Graph, FlightAgency

class TestFlight(unittest.TestCase):

    def setUp(self):
        self.airportE = Vertex("E", [])
        self.airportD = Vertex("D", [self.airportE])
        self.airportB = Vertex("B", [self.airportD])
        self.airportC = Vertex("C", [self.airportB])
        self.airportA = Vertex("A", [self.airportB, self.airportC, self.airportE])

        self.flights = [
            Flight('1', self.airportA, self.airportB,  2, 1),
            Flight('2', self.airportA, self.airportC,  4, 3),
            Flight('3', self.airportA, self.airportE,  12, 1),
            Flight('4', self.airportB, self.airportD,  6, 4),
            Flight('5', self.airportC, self.airportB,  5, 3),
            Flight('6', self.airportD, self.airportE,  8, 6),
        ]

        self.graph = Graph([self.airportA, self.airportB, self.airportC, self.airportD, self.airportE])

    def test_flightagency(self):
        # From A to B
        self.assertEqual( FlightAgency(self.flights, self.graph, self.airportA, self.airportB, 1), 2 )
        # From A to B after flight missed
        self.assertEqual( FlightAgency(self.flights, self.graph, self.airportA, self.airportB, 5), float('inf') )
        # From B to A
        self.assertEqual( FlightAgency(self.flights, self.graph, self.airportB, self.airportA, 1), float('inf') )

        # From A to C
        self.assertEqual( FlightAgency(self.flights, self.graph, self.airportA, self.airportC, 1), 4 )

        # To E
        self.assertEqual( FlightAgency(self.flights, self.graph, self.airportA, self.airportE, 1), 8 )
        self.assertEqual( FlightAgency(self.flights, self.graph, self.airportB, self.airportE, 1), 8 )

if __name__ == "__main__":
    unittest.main()