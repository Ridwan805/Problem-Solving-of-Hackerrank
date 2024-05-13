<h1 align = "center">Problem</h1>


<p>
<ul>
  <li>Declare a 2-dimensional array, <i>arr</i>, of n empty arrays. All arrays are zero indexed</li>
  <li>Declare a integer, <i><b>lastAnswer</b></i>, and initialize it to 0</li>
  <li>
    There are 2 types of queries, given as an array of strings for you to parse:
    <ol type="1">
      <li>
        Query: 1 x y
        <ol type="1">
          <li>Let idx = ((x ⊕ <i><b>lastAnswer)%n)</b></i></li>
          <li>Append the integer <i>y</i> to arr[idx]</li>
        </ol>
      </li>
      <li>
        Query: 2 x y
        <ol type="1">
          <li>Let <i>idx = ((x ⊕ lastAnswer)%n)</i></li>
          <li>Assign the value <i><b>arr[idx][y%size(arr[idx])]</b></i> to <i><b>lastAnswer</b></i>.</li>
          <li>Store the new value of <i><b>lastAnswer</b></i> to an answers array.</li>
        </ol>
      </li>
    </ol>
  </li>
</ul>
</p>
            
<p>
<b>Note:</b> ⊕ is the bitwise XOR operation, which corresponds to the ^ operator in most languages. Learn more about it on <a href="https://en.wikipedia.org/wiki/Exclusive_or" target= _blank>Wikipedia</a>. % is the modulo operator.
Finally, size(arr[idx]) is the number of elements in arr[idx]<br><br><br>
<b>Function Description</b><br><br>
Complete the dynamicArray function below.<br><br>
dynamicArray has the following parameters:<br>
- int n: the number of empty arrays to initialize in arr<br>
- string queries[q]: query strings that contain 3 space-separated integers<br><br>
  
<h4>Returns</h4><br>
<ul>
  <li>int[]: the results of each type 2 query in the order they are presented</li>
</ul>
<h4>Input Format</h4><br>
The first line contains two space-separated integers, <i>n</i>, the size of arr to create, and <i>q</i>, the number of queries, respectively.<br>
Each of the <i>q</i> subsequent lines contains a query string, <i><b>queries[i]</b></i>.

</p>

![image](https://github.com/Ridwan805/Problem-Solving-of-Hackerrank/assets/154875891/f7c8bf74-e38c-469b-84f5-82447a743617)

![image](https://github.com/Ridwan805/Problem-Solving-of-Hackerrank/assets/154875891/f17646ea-fb45-44a6-9ace-3cf727cb7b2e)

![image](https://github.com/Ridwan805/Problem-Solving-of-Hackerrank/assets/154875891/d3a5048b-763d-49d5-a811-fc48f00a0be2)

![image](https://github.com/Ridwan805/Problem-Solving-of-Hackerrank/assets/154875891/2ba9c845-544e-4f68-8112-55e673748f0b)

![image](https://github.com/Ridwan805/Problem-Solving-of-Hackerrank/assets/154875891/e6d45bfc-e4e0-4f6b-bc0a-85caacf377dd)




