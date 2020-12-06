import queue

class Flight:
    def __init__(self, name, origin, dest, arrivalT, departT):
        self.name = name
        self.origin = origin
        self.dest = dest
        self.arrivalT = arrivalT
        self.departT = departT
        self.weight = departT - arrivalT

    def __str__(self):
        return str(self.origin) + " - " + str(self.dest)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.arrivalT < other.arrivalT


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices

class Schedule:
    def __init__(self, vertex, time):
        self.vertex = vertex
        self.time = time

    def __hash__(self):
        return hash(str(self.vertex) + ":" + str(self.time))

    def __lt__(self, other):
        return self.time < other.time

    def __str__(self):
        return "{" + str(self.vertex) + ":" + str(self.time) + "}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Schedule):
            return (self.vertex == other.vertex) and (self.time == other.time)
        return False

class Vertex:

    def __init__(self, name, adjacentVertices):
        self.name = name
        self.adjacentVertices = adjacentVertices

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.adjacentVertices == other.adjacentVertices
        return False

    def __hash__(self):
        return hash(str(self.name))


def FlightAgency(F, G, s, d, startT):
# F - flights, G - airports, s - source, d -destination, startT - sourceStartTime

    T = {}
    T[s] = startT

    # for all vertex, v != s do T[v] ← infinity
    for vertex in G.vertices:
        if(vertex is not s):
            T[vertex] = float("inf")

    # Priority Queue, q, of vertices keyed by T
    q = queue.PriorityQueue()
    for vertex in G.vertices:
        q.put(Schedule(vertex, T[vertex]))

    while not q.empty():
        v = q.get()

        for adjacentVertex in v.vertex.adjacentVertices:
            if Schedule(adjacentVertex, T[adjacentVertex]) in q.queue:
                # Priority Queue, p, of fights, f, with f.departT ≥ T[v] keyed by f.arriveT
                p = queue.PriorityQueue()
                for flight in F:
                    if(flight.origin == v.vertex and flight.dest == adjacentVertex):
                        if(flight.departT >= T[v.vertex]):
                            p.put(flight)

                t = float("inf")

                if not p.empty():
                    t = p.queue[0].arrivalT

                # relaxation
                if t < T[adjacentVertex]:
                    T[adjacentVertex] = t
                    q.put(Schedule(adjacentVertex, t))

            else:
                break
    
    earliestTime = T[d]
    
    return earliestTime
