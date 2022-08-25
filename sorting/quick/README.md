# Blog Notes: Quick Sort

Today, we're going to be going over quick sort functionality. For this demo, we will be using the list `[5,3,1,7,2]`.

For the first step, we will want to find our 'pivot' point and start to sort from there. For this first iteration, it will be the value associated with the furthest index to the right, which for us will be `2`. We will also now have a 'low' variable, which is your left-most index - 1, so `-1` to begin with for us.

```python
[5,3,1,7,2] -1
 ^
5 !<= 2
[5,3,1,7,2] -1
   ^
3 !<= 2
[5,3,1,7,2] -1
     ^
1 <= 2
[1,3,5,7,2] 0
       ^
7 !<= 2
[1,3,5,7,2] 0
   ^     ^
[1,2,5,7,3] 1
```

In this first step, we get two things, our updated list of `[1,2,5,7,3]` and a new pivot of `1`. Now, we go through the same thing, but our new right-most index will be pivot - 1 (so `0`) and our left value will stay at zero. Since the left value is not less than the right value, we actually can skip this step entirely and move on to the next, running through it with our *left* index as pivot + 1 (so `2`), and our right as the original value of 4. With our left index as 2, our new low is going to be `1` and our new pivot is `3` (the value now residing at the right-most index). Let's jump straight into it!

```python
[1,2,5,7,3] 1
     ^
5 !<= 3
[1,2,5,7,3] 1
       ^
7 !<= 3
[1,2,5,7,3] 1
     ^   ^
[1,2,3,7,5] 2
```

If you can see in the code above, we started out at the low index and didn't bother checking anything before that, because we know those ones are already in order! Now, we have a list of `[1,2,3,7,5]`, which is almost there, but not quite. Luckily, we have one more step to do! With our new pivot as `2`, we can't run the first quick sort again, so we jump to the second one, using `3` (our pivot + 1) as the left index and `4` as the right with our new pivot of `7`.

```python
[1,2,3,7,5] 2
       ^
7 !<= 5
[1,2,3,7,5] 2
       ^ ^
[1,2,3,5,7] 3
```

Now! Lo and behold, our list is in order! We're still a few recursive functions into the stack when we get here, but as we go back up since we were on the second call of each step, we get right back to the top with no hold-ups! And there we have the steps behind quick sorting!

## Approach & Efficiency

For the approach to this challenge, I used recursive calls to create pivot points within the list and continually move things around them until everything was in the correct order. The O notation for space here is O(N^2) because it is using recursive functions and time is O(N) because it will have more steps to achieve for every item in the list that is passed in.

## Solution

[code](../../python/code_challenges/quick_sort.py) |
[tests](../../python/tests/code_challenges/test_quick_sort.py)
