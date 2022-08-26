# Hashtables

A hashtable is a method of storing data as key-value pairs in a series of different data structures to best optimize searching and storage

## Challenge

Create a Hashtable class with the methods set, get, contains, keys, and hash

## Approach & Efficiency

The approach I took for this was to create an average hashtable (a list of linked lists), and then for the traversal I would find the bucket with the correct hash for the key and then do whatever I needed to do with those values. Time for this should be O(1) for the lookup and the worst it should get is O(n) for going through and finding all of the keys. For space, we should have O(n), because it should be the same amount of space no matter what data we put in since we predefine the space required.
