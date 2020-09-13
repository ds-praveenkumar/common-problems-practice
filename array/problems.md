# Array problems

 ***1. Longest consecutive subsequence***
 ###
Given an array of positive integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.
* Input: <br />
The first line of input contains T, number of test cases. First line of line each test case contains a single integer N.
Next line contains N integer array.
* Output: <br />
Print the output of each test case in a seprate line.
* Constraints: <br />
1 <= T <= 100 <br />
1 <= N <= 105 <br />
0 <= a[i] <= 105 <br />
* Example: <br />
Input: <br />
2 <br />
7 <br />
2 6 1 9 4 5 3 <br />
7 <br />
1 9 3 10 4 20 2 <br />

* Output: <br />
6 <br />
4 <br />


***2. Subarray with given sum***
###
Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.
* Input: <br />
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.
* Output: <br />
For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else print -1.
* Constraints: <br />
1 <= T <= 100 <br />
1 <= N <= 107 <br />
1 <= Ai <= 1010 <br />
* Example: <br />
* Input <br/>
2<br/>
5 12<br/>
1 2 3 7 5<br/>
10 15<br/>
1 2 3 4 5 6 7 8 9 10<br/>
* Output: <br />
2 4<br />
1 5<br />
* Explanation : <br />
Testcase1: sum of elements from 3rd position to 4th position is 12<br />
Testcase2: sum of elements from 1st position to 5th position is 15


***3. Maximum sub sum in an array***
###
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.
* Input:<br />
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.
* Output: <br />
Print the maximum sum of the contiguous sub-array in a separate line for each test case.
* Constraints: <br />
1 ≤ T ≤ 110<br />
1 ≤ N ≤ 106<br />
-107 ≤ A[i] <= 107<br />
* Example
* Input <br/>
2<br />
5<br />
1 2 3 -2 5<br />
4<br />
-1 -2 -3 -4<br />
* Output: <br />
9<br />
-1<br />
* Explanation : <br />
Testcase 1: Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.

***4. Missing number in array***
###
Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number is to be found.
* Input:<br />
The first line of input contains an integer T denoting the number of test cases. For each test case first line contains N(size of array). The subsequent line contains N-1 array elements.
* Output: <br />
Print the missing number in array.
* Constraints: <br />
1 ≤ T ≤ 200 <br />
1 ≤ N ≤ 107<br />
1 ≤ C[i] ≤ 107<br />
* Input <br/>
2<br />
5<br />
1 2 3 5<br />
10<br />
1 2 3 4 5 6 7 8 10<br />
* Output: <br />
4<br />
9<br />
* Explanation : <br />
Testcase 1: Given array : 1 2 3 5. Missing element is 4.

***5. Missing number in array***
###
* Input:<br />
* Output: <br />
* Constraints: <br />
* Input <br/>
* Output: <br />
* Explanation : <br />


***6. Missing number in array***
###
* Input:<br />
* Output: <br />
* Constraints: <br />
* Input <br/>
* Output: <br />
* Explanation : <br />