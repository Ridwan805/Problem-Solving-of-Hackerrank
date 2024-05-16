<h1 align = 'center'>Problem</h1>

<p>
  You are given the pointer to the head node of a linked list and an integer to add to the list. Create a new node with the given integer. Insert this node at the tail of the linked list and return the head node of the linked list formed after inserting this new node. The given head pointer may be null, meaning that the initial list is empty.
<h4>Function Description</h4>
  Complete the insertNodeAtTail function in the editor below.<br>

insertNodeAtTail has the following parameters:
<ul>
  <li>
    SinglyLinkedListNode pointer head: a reference to the head of a list
  </li>
  <li>
    int data: the data value for the node to insert
  </li>
</ul>
<h4>Returns</h4>
<ul>
  <li>
    SinglyLinkedListNode pointer: reference to the head of the modified linked list
  </li>
</ul>
<h4>Input Format</h4>
The first line contains an integer <i>n</i>, the number of elements in the linked list.<br>
the next <i>n</i> lines contains an integer each, the value that needs to be inserted at tail.
<h4>Constraints</h4>
<ul>
  <li>
    1 ≤ <i>n</i> ≤ 1000
  </li>
  <li>
    1 ≤ <i>list<sub>i</sub></i> ≤ 1000
  </li>
</ul>
<h3>Sample Input</h3>
STDIN Function ----- -------- 5 size of linked list n = 5 141 linked list data values 141..474 302 164 530 474
<h3>
  Sample Output
</h3>
141<br>
302<br>
164<br>
530<br>
474
<h3>
  Explanation
</h3>
First the linked list is NULL. After inserting 141, the list is 141 -> NULL.<br>
After inserting 302, the list is 141 -> 302 -> NULL.<br>
After inserting 164, the list is 141 -> 302 -> 164 -> NULL.<br>
After inserting 530, the list is 141 -> 302 -> 164 -> 530 -> NULL. After inserting 474, the list is 141 -> 302 -> 164 -> 530 -> 474 -> NULL, which is the final list.


</p>
