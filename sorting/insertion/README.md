# Blog Notes: Insertion Sort

Today we're going to go over how the insertion sort method works.

We're going to be using the list `[8,4,23,42,16,15]` for this demonstration.

Now, to start out, we have the above list, which is unsorted. The first step we're going to take in the method of insertion sorting is to 'pull out' the second item in the list.

``` python
   4
   ^
[8, ,23,42,16,15]
```

Once we have this value, we will want to compare it against the value to it's immediate left, which in this case is `8`. Since `4 < 8` we will want to move the 8 to the right into the space the `4` left behind.

``` python
   4

[ ,8,23,42,16,15]
```

Now that we've reached the beginning of the list and there are no more values to the left to check, we will put the held value of `4` into the remaining space, which right now is the first index of the list.

``` python
[4,8,23,42,16,15]
```

We then move one space to the right, which will have us looking at the third item in the list now, and perform the previous steps again.

``` python
     23
     ^
[4,8, ,42,16,15]

23 > 8

[4,8,23,42,16,15]
```

In this example, the next item in the list is correctly sorted so we don't need to move any values around, and we also don't need to check any further to the left, as we know that the values there are already correctly sorted, so the first value we check will be the highest.

Now that we've determined this, we can move to the next value in the list.

``` python
        42
        ^
[4,8,23, ,16,15]

42 > 23

[4,8,23,42,16,15]
```

Once again, we don't have any need to move values around and can move on.

``` python
           16
           ^
[4,8,23,42, ,15]

16 < 42

        16

[4,8,23, ,42,15]

16 < 23

     16

[4,8, ,23,42,15]

16 > 8

[4,8,16,23,42,15]
```

For this value, we had to move over two items before we found a lower value and cound stop the search, which meant that each of those two items moved forward one index and our held value dropped into the index that previously held the lowest of the moved values. Then, we can move on to the final item in the list.

``` python
              15
              ^
[4,8,16,23,42, ]

15 < 42

           15

[4,8,16,23, ,42]

15 < 23

        15

[4,8,16, ,23,42]

15 < 16

     15

[4,8, ,16,23,42]

15 > 8

[4,8,15,16,23,42]
```

And now you have your sorted list using the insertion method!

## Approach & Efficiency

The approach I took to this challenge was to run through the list item by item and check all the way to the beginning of the list with each run. I think the Big O for space in this will be O(1), as I am modifying everything in place, but time will be O(N^2) because for each item in the list, there is the possibility it will need to check every previous item in the list again for each iteration.

## Solution

[code](../../python/code_challenges/insertion_sort.py) |
[tests](../../python/tests/code_challenges/test_insertion_sort.py)
