from flight import Flight, Vertex, Graph, FlightAgency

# The airports as vertices
airportE = Vertex("E", [])
airportD = Vertex("D", [airportE])
airportB = Vertex("B", [airportD, airportE])
airportC = Vertex("C", [airportB])
airportA = Vertex("A", [airportC, airportB])

def run():

    # List the flights for airports
    flights = [
        Flight('FN-101', airportA, airportB,  6, 2),
        Flight('FN-102', airportA, airportC,  8, 2),
        Flight('FN-103', airportB, airportD,  13, 12),
        Flight('FN-104', airportB, airportE,  17, 11),
        Flight('FN-105', airportC, airportB,  10, 9),
        Flight('FN-106', airportC, airportD,  10, 6,),
        Flight('FN-107', airportD, airportE,  14, 13),
    ]

    # Graph with airports as vertices
    graph = Graph([airportA, airportB, airportC, airportD, airportE])

    # Origin Airport be airportA and destination be airportE
    startVertex = airportA
    endVertex = airportE
    # Start time be 2 (Time in 24 hour format)
    startT = 2

    earliestArrivalTime = FlightAgency(flights, graph, startVertex, endVertex, startT)
    if (earliestArrivalTime != float("inf")):
        print(f'The earliest arrival time for the airport {endVertex} from airport {startVertex} is {earliestArrivalTime}:00.')
    else:
        print(f'No flight from airport {startVertex} to airport {endVertex} after {startT}:00.')

if __name__ == '__main__':
    run()
