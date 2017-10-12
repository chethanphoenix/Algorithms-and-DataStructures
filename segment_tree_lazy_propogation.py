#!/usr/bin/python
from math import log

MAX_NUMBER = pow(10, 9) + 7


def construct_min_segment_tree(start, end, array, output_array, node):
    if start == end:
        output_array[node - 1] = array[start - 1]
        return

    else:
        mid = (start + end) / 2
        left_node = 2 * node
        construct_min_segment_tree(start, mid, array, output_array, left_node)
        construct_min_segment_tree(mid + 1, end, array, output_array, left_node + 1)
        output_array[node - 1] = output_array[left_node - 1] if output_array[left_node - 1] < output_array[
            left_node] else output_array[left_node]


def query_segment_tree(qstart, qend, start, end, array, output_array, node):
    if lazy[node-1] != 0:
        output_array[node-1] += lazy[node-1]
        left_node = 2 * node
        if start != end:
            lazy[left_node - 1] = lazy[node-1]
            lazy[left_node] = lazy[node-1]
        lazy[node - 1] = 0

    if qstart > end or qend < start:
        return MAX_NUMBER

    elif start == end or (qstart <= start and qend >= end):
        return output_array[node - 1]

    else:
        mid = (start + end)/2
        left_node = 2*node
        left = query_segment_tree(qstart, qend, start, mid, array, output_array, left_node)
        right = query_segment_tree(qstart, qend, mid+1, end, array, output_array, left_node+1)

        return left if left < right else right


def update_segment_tree_lazy(qstart, qend, start, end, array, output_array, node, diff, lazy):
    if lazy[node-1] != 0:
        output_array[node-1] += lazy[node-1]
        left_node = 2 * node
        if start != end:
            lazy[left_node - 1] = lazy[node-1]
            lazy[left_node] = lazy[node-1]
        lazy[node - 1] = 0

    if start == end and (qstart <= start and qend >= end):
        output_array[node - 1] += diff
        return

    elif qstart > end or qend < start:
        return

    elif qstart <= start and qend >= end:
        mid = (start + end) / 2
        left_node = 2 * node
        output_array[node-1] += diff
        lazy[left_node-1] += diff
        lazy[left_node] += diff

    else:
        mid = (start + end)/2
        left_node = 2*node
        update_segment_tree_lazy(qstart, qend, start, mid, array, output_array, left_node, diff, lazy)
        update_segment_tree_lazy(qstart, qend, mid+1, end, array, output_array, left_node+1, diff, lazy)
        output_array[node - 1] = output_array[left_node - 1] if output_array[left_node - 1] < output_array[left_node] else output_array[left_node]
        return


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    length = len(array)
    height = int(log(length, 2))
    max_nodes = pow(2, height + 1) - 1
    min_output_array = [0] * max_nodes
    lazy = list(min_output_array)
    construct_min_segment_tree(1, length, array, min_output_array, 1)
    print min_output_array

    no_of_q = int(raw_input())
    for _ in xrange(no_of_q):
        q = raw_input().split()
        if q[0] == "2":
            q, l, r, diff = map(int, q)
            update_segment_tree_lazy(l, r, 1, length, array, min_output_array, 1, diff, lazy)
        else:
            q, l, r = map(int, q)
            print query_segment_tree(l, r, 1, length, array, min_output_array, 1)

        # print min_output_array
        # print lazy

