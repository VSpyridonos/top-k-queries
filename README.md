# top-k-queries
Implementing two top-k join algorithms with Python 3, calculating their run times and creating a graph.

<p>
Algorithms intend to find top-K pairs from two files (males_sorted and females_sorted) that have the highest sum of the instance weight field. Data is taken from: https://archive.ics.uci.edu/ml/datasets/Census-Income+(KDD)
</p>

<p><h2>Algorithm A (topkjoinA.py)</h2>
Implements HRJN algorithm (https://cs.uwaterloo.ca/~ilyas/papers/rank_join2.pdf). Algorithm reads next valid line from either males_sorted or females_sorted files, updates corresponding dictionaries which contain previously read lines from each file and have the age field as key. On every run, threshold is updated and results of joining current line with the other file's hash table are found. Algorithm is implemented as a generator function: every time the corresponding function is called, it returns the next join result. For example, the first 5 join results are the following:
<ol>
  <li> pair: 135085,67141 score: 25785.54</li>
  <li> pair: 135085,44307 score: 24247.12</li>
  <li> pair: 135085,111291 score: 23657.66</li>
  <li> pair: 135085,12112 score: 23644.20</li>
  <li> pair: 135085,183898 score: 23046.54</li>
</ol>
Program run time is printed.
</p>

<p><h2>Algorithm B (topkjoinB.py)</h2>
Algorithm reads entire males_sorted file and puts valid tuples into a dictionary that has the age field as key. Then, reads the tuples from females_sorted file one by one and for each one of them, finds the tuples that join using the dictionary. Top-k results so far, are stored in a min-heap, which at the end of the algorithm will have the top-k pairs. Program run time is printed.
</p>

<p><h2>Usage:</h2>
python3 algorithm_file K*
<br>
* where K = any number
</p>
