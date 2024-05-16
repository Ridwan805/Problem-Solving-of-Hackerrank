<h1 align = "center">Problem</h1>

<p>
  There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.<br>
<h4>Example:</h4>
  <i>StringList</i> = [<i>'ab','ab','abc'</i>]<br>
  <i>queries</i> = [<i>'ab','abc','bc'</i>]<br>
  There are 2 instance of <i>'ab'</i>, 1 of <i>'abc'</i> and 0 of<i>'bc'</i>. For each query add an element to the return array, <i>results</i> = [2,1,0]

  <h4>Functions Description</h4>

  Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of  occurrence of each query string in stringList.<br>
  matchingStrings has the following parameters:
  <ul>
    <li>
      string stringList[n] - an array of strings to search
    </li>
    <li>
      string queries[q] - an array of query stings
    </li>
  </ul>
  <h4>Returns</h4>
  <ul>
    <li>
      int[q]: an array of results for each query
    </li>
  </ul>
  <h4>
    Input Format
  </h4>
  The first line contains and integer <i>n</i>, the size of <i>stringList[].</i><br>
  Each of the next <i>n</i> lines contains a string <i>stringList[i].</i><br>
  The next line contains <i>q</i> the size of <i>queries[].</i><br>
  Each of the next <i>q</i> line contains a string <i>queries[i].</i>

  <h4>Constraints</h4>

  1 ≤ <i>n</i> ≤ 1000 <br>
  1 ≤ <i>q</i> ≤ 1000 <br>
  1 ≤ |<i>stringList[i]</i>|,|<i>queries[i]</i>| ≤ 20

  <h4>Sample Input 1</h4>
  
  ![image](https://github.com/Ridwan805/Problem-Solving-of-Hackerrank/assets/154875891/5f4b2c46-a692-452e-a376-bf33b56b5018)

<h4>Sample Output 1</h4>
2<br>
1<br>
0<br>

<h4>Explanation 1</h4>
Here, "aba" occurs twice, in the first and third string. The string "xzxb" occurs once in the fourth string and "ab" does not occur at all.
<h4>Sample Input 2</h4>

![image](https://github.com/Ridwan805/Problem-Solving-of-Hackerrank/assets/154875891/77ddc39e-1c50-46f8-9e07-2e67f4bb69d5)

<h4>Sample Output 2</h4>
1<br>
0<br>
1<br>
</p>
