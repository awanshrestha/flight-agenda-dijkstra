# flight-agenda-dijkstra
An implementation of Dijkstra's Algorithm for Flight Agenda problem.

It is the Python implementation of Dijkstra's Algorithm for Flight Agenda problem as given in http://www.csl.mtu.edu/cs2321/www/newLectures/30_More_Dijkstra.htm

### Problem Statement
A travel agent requests software for making an agenda of flights for clients. The agent has access to a data base with all airports and flights. Besides the flight number, origin airport and destination, the flights have departure and arrival time. Specifically the agent wants to determine the earliest arrival time for the destination given an origin airport and start time.

### Problem Overview
This is the shortest path algorithm problem as we need to calculate the earliest arrival time, with a given start time. So, we can take the problem as a di graph where all the airports are nodes and the flights are the di edges with weight of time interval i.e. the time difference between arrival time of destination airport and departure time of source airport.

Here we need to take care that while going from origin airport to destination airport, and while taking flights from one airport to another, we can take only those flights which can be caught. So, time plays an important role in this problem as we can take only the flights whose departure time from the airport is later than our arrival time at the airport.

So, to solve this we use Dijkstra’s Algorithm with a little modification.

### Algorithm
(Given in http://www.csl.mtu.edu/cs2321/www/newLectures/30_More_Dijkstra.htm)
The algorithm for this problem is the slight modification of Dijkstra’s Algorithm. Here we have the database about airports and the flights. There is information about flight number, origin airport and destination, the flights have departure and arrival time. So, given origin and destination airports and start time we need to make our data structure properly to keep the data and find the shortest arrival time. 

Here the di graph is used where the airports are the vertices and flights are di-edges with weights: departure time and arrival time. The distance should be the function of earliest arrival times at airports. Then based upon those earliest arrival time, we use a minimum priority queue for airports. 

For the initial origin airport let the earliest arrival time be start time and for others it will be infinity in the beginning. Now, until the queue is not empty, adjacent loop is to be formed where we can only select the flights which can be caught, and we also want the flight with minimum arrival time. So, for that we create another priority queue of flights where its departure time should be later than arrival time of another flight at the airport. And we also use another variable time, which is used to update the flight priority queue. And finally, we perform relaxation, where if the above time is less than the earliest arrival time at adjacent airport, then we change the earliest arrival time of the airport to be the time and update in the airport queue accordingly.
