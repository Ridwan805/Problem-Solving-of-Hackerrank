<h1 align = 'center'>Problem</h1>

<p>
  Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.
  <br>
  <b>Example</b><br>
  <i>n</i> = 10 <br>
  <i>queries = [[1,5,3],[4,8,7],[6,9,1]]</i><br>
  Queries are interpreted as follows:
</p>

![image](https://github.com/Ridwan805/Problem-Solving-of-Hackerrank/assets/154875891/389c6b51-d971-431f-b05f-57fd70cccf70)

<p>
  Add the values of <i>k</i>  between the indices <i>a</i> and <i>b</i> inclusive:
</p>

![image](https://github.com/Ridwan805/Problem-Solving-of-Hackerrank/assets/154875891/94755aaa-8bb2-423c-958b-67d9af4cc475)

<p>
  The largest value is 10 after all operations are performed.<br>
  <b>Function Description</b><br>
  Complete the function arrayManipulation in the editor below.<br>
  arrayManipulation has the following parameters:
  <ul>
    <li>
      int n - the number of elements in the array
    </li>
    <li>
      int queries[q][3] - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.
    </li>
  </ul>
  <b>Returns</b><br>
  <ul>
    <li>
      int - the maximum value in the resultant array
    </li>
  </ul>
  <b>Input Format</b><br>
  The first line contains two space-separated integers <i>n</i> and <i>m</i>, the size of the array and the number of operations.<br>
  Each of the next <i>m</i> lines contains three space-separated integers <i>a</i>, <i>b</i> and <i>k</i>, the left index, right index and summand.<br>
  <b>Constraints</b>
</p>

![image](https://github.com/Ridwan805/Problem-Solving-of-Hackerrank/assets/154875891/bfb365c1-54e5-493b-a73e-5ab11177c08e)

<p><b>Sample Input</b><br>

![image](https://github.com/Ridwan805/Problem-Solving-of-Hackerrank/assets/154875891/adcf647a-14a9-4e2d-ac63-548d3561e068)

<b>Sample Output</b><br>

![image](https://github.com/Ridwan805/Problem-Solving-of-Hackerrank/assets/154875891/d8c435a9-0d2c-4ca3-88c6-b83e7e8e533f)

<b>Explanation</b><br>

After the first update the list is 100 100 0 0 0.<br>
After the second update list is 100 200 100 100 100.<br>
After the third update list is 100 200 200 200 100.<br>

The maximum value is 200.
</p>

