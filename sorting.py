#!/usr/bin/python
from time import time

def bubble_sort(unsorted_array):
    length = len(unsorted_array)
    for i in xrange(1, length):
        for j in xrange(length - i):
            if unsorted_array[j] > unsorted_array[j+1]:
                tmp = unsorted_array[j]
                unsorted_array[j] = unsorted_array[j+1]
                unsorted_array[j+1] = tmp
    return unsorted_array

def selection_sort(unsorted_array):
    l = len(unsorted_array)
    for i in xrange(l):
        large = unsorted_array[i]
        pos = i
        for j in xrange(i, l):
            if unsorted_array[j] < large:
                large = unsorted_array[j]
                pos = j
        if pos != i:
            tmp = unsorted_array[i]
            unsorted_array[i] = unsorted_array[pos]
            unsorted_array[pos] = tmp
    return unsorted_array

def insertion_sort(unsorted_array):
    l = len(unsorted_array)
    for i in xrange(1, l):
        for j in xrange(i, 0, -1):
            if unsorted_array[j] < unsorted_array[j-1]:
                tmp = unsorted_array[j]
                unsorted_array[j] = unsorted_array[j - 1]
                unsorted_array[j - 1] = tmp
            else:
                break
    return unsorted_array

def merge_sort(unsorted_array):
    l = len(unsorted_array)

    mid = l/2
    sort = []
    if mid < 1:
        return unsorted_array
    left = merge_sort(unsorted_array[0:mid])
    right = merge_sort(unsorted_array[mid:l])
    sort = merge(left, right)
    return sort

def merge(left, right):
    i = 0
    j = 0
    sort = []
    l_l = len(left)
    r_l = len(right)
    while i < l_l and j < r_l:
        if left[i] < right[j]:
            sort.append(left[i])
            i += 1
        else:
            sort.append(right[j])
            j += 1

    while j < r_l:
        sort.append(right[j])
        j += 1

    while i < l_l:
        sort.append(left[i])
        i += 1

    return sort


if __name__ == "__main__":
    array = map(int, raw_input("Enter the array to be sorted: ").split())
    start = time()
    print bubble_sort(list(array))
    print "done by bubble sort in: ", time() - start
    start = time()

    print selection_sort(list(array))
    print "done by selection sort in: ", time() - start

    start = time()
    print insertion_sort(list(array))
    print "done by insertion sort in: ", time() - start

    start = time()
    print merge_sort(list(array))
    print "done by merge sort in:", time() - start