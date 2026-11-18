RANDOMIZED LOAD BALANCER FOR SERVICE REQUESTS
=============================================

PROJECT TYPE
------------
DAA Mini Project
Programming language: Python 3
Libraries: Python standard library + Matplotlib

PROJECT DESCRIPTION
-------------------
This project simulates how incoming service requests can be assigned to a
group of servers. It compares three algorithms:

1. Randomized Load Balancing
   Every request is assigned to a uniformly random server.

2. Round Robin
   Requests are assigned sequentially, cycling through all servers.

3. Power of Two Choices
   Two distinct servers are selected randomly. The request is assigned to
   whichever of the two currently has fewer requests. Ties are broken in
   favour of the first selected server.

FEATURES
--------
- User enters the number of servers and requests.
- Displays request count for every server.
- Calculates maximum, minimum, average, standard deviation and load range.
- Measures execution time for each algorithm.
- Saves four comparison charts in a 'charts' directory.

HOW TO RUN ON macOS
-------------------
1. Extract the ZIP file.
2. Open the extracted folder in VS Code.
3. Open Terminal in VS Code.
4. (Recommended) Create and activate a virtual environment:

   python3 -m venv .venv
   source .venv/bin/activate

5. Install dependency:

   python3 -m pip install -r requirements.txt

6. Run:

   python3 main.py

7. Enter at least 2 servers and a non-negative request count.

FILES
-----
main.py           Main program and user interaction
algorithms.py     Implementations of the three algorithms
performance.py    Performance metrics and comparison table
visualization.py  Chart generation
requirements.txt  Required Python package

DAA COMPLEXITY ANALYSIS
-----------------------
Let:
N = number of servers
R = number of requests

Algorithm                     Time             Auxiliary space
Randomized Load Balancing     O(R) expected    O(N)
Round Robin                   O(R)             O(N)
Power of Two Choices          O(R) expected    O(N)

The O(N) space is used for the server-load array. The algorithms perform
constant expected work per request. Power of Two Choices selects two
distinct servers using random.sample; its expected selection cost is
constant for the standard Python implementation.

METRICS
-------
Maximum load: Highest number of requests assigned to any server.
Minimum load: Lowest number of requests assigned to any server.
Average load: Total requests divided by number of servers.
Standard deviation: Measures how spread out server loads are.
Load range: Maximum load minus minimum load.
Execution time: Measured runtime on the current computer.

IMPORTANT NOTES
---------------
- Randomized results can change from run to run.
- Round Robin produces counts differing by at most one when every request
  is treated equally and every server is available.
- Power of Two Choices often reduces imbalance compared with choosing one
  server uniformly at random, but a particular run is not guaranteed to
  outperform every other algorithm.
- This is a simulation. It does not send real network requests or measure
  real server response times.
- Execution-time results depend on computer load and Python environment.

CONCLUSION
----------
The project demonstrates randomized algorithm design and compares it with
a deterministic scheduling approach. It illustrates how random selection
and partial load information can affect the distribution of service
requests across servers.
