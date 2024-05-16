<h1 align = 'center'>Problem</h1>

<p>
  A left rotation operation on an array of size <i>n</i> shifts each of the array's elements 1 unit to the left. Given an integer, <i>d</i>, rotate the array that many steps left and return the result.<br>
  <h4>Example</h4>
  <i>d=2</i><br>
  <i>arr</i> = [1,2,3,4,5]
  After 2 rotation <i>arr'</i> = [3,4,5,1,2]<br>
  <h4>Function Description</h4>
  Complete the rotateLeft function in the editor below.<br>
  rotateLeft has the following parameters:<br>
  <ul>
    <li>
      int d: the amount to rotate by
    </li>
    <li>
      int arr[n] the array to rotate
    </li>
  </ul>
  <h4>Returns</h4>
  <ul>
    <li>
      int[n]: the rotated array
    </li>
  </ul>
  <h4>Input Format</h4>
  The first line contains two space-sperated integers that denote <i>n</i> the number of integers, and <i>d</i> the number of left rotations to perform <br>
The second line contains n space separated integers that describe arr[]<br><br><br>
  <h4>Constraints</h4>
  <ul>
    <li>
      1 ≤ <i>n</i> ≤ 10<sup>5</sup>
    </li>
    <li>
      1 ≤ <i>d</i> ≤ <i>n</i>
    </li>
    <li>
      1 ≤ <i>a[i]</i> ≤ 10<sup>6</sup> 
    </li>
  </ul>

  <h4>Sample Input</h4>
  5 4<br>
  1 2 3 4 5
  <h4>Sample Output</h4>
  5 1 2 3 4<br>
  <h4>Explanation</h4>
  To perform <i>d = 4</i> left rotation, the array undergoes the following sequence of charges:<br>
  [1,2,3,4,5] --> [2,3,4,5,1] --> [3,4,5,1,2] --> [4,5,1,2,3] --> [5,1,2,3,4}
</p>
