# Blog Notes: Merge Sort

Today we will be going over the merge sort function. The idea of merge sort is to split your list into smaller and smaller chunks to make it easier to sort them each, then to slowly put those chunks together until you have the complete list.

For this demonstration, we will be using `[5,3,1,4,2]` as our list that we would like to sort. Our first step is to find the midpoint and split the list in half there, forming two smaller lists.

```python
[5,3] - [1,4,2]
```

In this case, we are splitting the list before the one into two slightly different sizes, as the original has an odd valued length. Next we will split the left side again and leave the right side out for the moment.

```python
[5] - [3]
```

Now that we've made these lists as small as they can get, we send the two lists and the immediate ancestor list in to the actual merge functionality.

```python
[5,3]  [5]  [3]
 ^      ^    ^
5 > 3
[3,3]  [5]  [3]
   ^    ^     x
[3,5]
```

In the above code, we start at the first index of each list, and check the first item of each of the two minimized lists against each other. We know that `5` is greater than `3`, so the first item of the parent list is changed to be `3` and we move on to the second index of anything affected (being the parent list and the right value), which is outside of the minimized list, so we add whatever is left in the other list to the new index of the parent and return the altered parent. Now, we hold onto that value and go back to our other list from earlier.

```python
[1] - [4,2]
```

Our left list is down to a single number, but we still have further to go in our right list, so we will need to run that through one more time before moving on.

```python
[4] - [2]
```

Now we run these two numbers through the same way as before.

```python
[4,2]  [4]  [2]
 ^      ^    ^
4 > 2
[2,2]  [4]  [2]
   ^    ^     x
[2,4]
```

Once we return that value, we can't go all the way back and merge up with the left values yet, because we still have one more piece of the previous split for the list on the right, so now we will send the list we just got back through with the next level up's left value.

```python
[1,4,2]  [1]  [2,4]
 ^        ^    ^
1 < 2
[1,4,2]  [1]  [2,4]
   ^       x   ^
[1,2,4]
```

Here, as the values on the left had all been exhausted, we were able to move everything from the right to overwrite the rest of the list without checking each value since, if we've done our job right, they will all be in order. Now, we can finally go up to the last level and rejoin the original right and left sides!

```python
[5,3,1,4,2]  [3,5]  [1,2,4]
 ^            ^      ^
3 > 1
[1,3,1,4,2]  [3,5]  [1,2,4]
   ^          ^        ^
3 > 2
[1,2,1,4,2]  [3,5]  [1,2,4]
     ^        ^          ^
3 < 4
[1,2,3,4,2]  [3,5]  [1,2,4]
       ^        ^        ^
5 > 4
[1,2,3,4,2]  [3,5]  [1,2,4]
         ^      ^         x
[1,2,3,4,5]
```

And there we have it! We've got our list fully sorted into ascending order.

## Approach & Efficiency

The approach I took today was to use a recursive function to sort the list into smaller sections and sort each of those until they're as small as they can get, then sort each of these smaller sections as they go back up the call stack. The O notation for time here will be O(N) since there will be extra steps for each item in the list, and for space it will be O(N^2) as the function is recursive and will take more space in the stack the larger the input list is.

## Solution

[code](../../python/code_challenges/merge_sort.py) |
[tests](../../python/tests/code_challenges/test_merge_sort.py)
