#!/usr/bin/python
from math import log

MAX_NUMBER = pow(10, 9) + 7
def construct_sum_segment_tree(start, end, array, output_array, node):
    if start == end:
        output_array[node - 1] = array[start - 1]
        return

    else:
        mid = (start + end) / 2
        left_node = 2 * node
        construct_sum_segment_tree(start, mid, array, output_array, left_node)
        construct_sum_segment_tree(mid + 1, end, array, output_array, left_node + 1)
        output_array[node - 1] = output_array[left_node - 1] + output_array[left_node]


def update_segment_tree(qstart, qend, start, end, array, output_array, node, diff):
    if qstart > end or qend < start:
        return

    elif start == end:
        output_array[node - 1] += diff
        return

    elif qstart <= start or qend >= end:
        mid = (start + end) / 2
        left_node = 2 * node
        update_segment_tree(qstart, qend, start, mid, array, output_array, left_node, diff)
        update_segment_tree(qstart, qend, mid + 1, end, array, output_array, left_node + 1, diff)

        output_array[node - 1] = output_array[left_node - 1] if output_array[left_node - 1] < output_array[
            left_node] else output_array[left_node]
        return

def query_segment_tree(qstart, qend, start, end, array, output_array, node, diff):
    if qstart > end or qend < start:
        return MAX_NUMBER

    elif start == end or (qstart <= start and qend >= end):
        return output_array[node - 1]

    elif qstart <= start or qend >= end:
        mid = (start + end) / 2
        left_node = 2 * node
        left = query_segment_tree(qstart, qend, start, mid, array, output_array, left_node, diff)
        right = query_segment_tree(qstart, qend, mid + 1, end, array, output_array, left_node + 1, diff)

        return left if left < right else right


if __name__ == "__main__":
    # array = [1, 2, 3, 4, 5, 6, 7, 8]
    string = "1. update the segment tree in the range\n2. query the segment tree in the range"
    array = map(int, raw_input("Enter the array: ").split())
    length = len(array)
    height = int(log(length, 2)) + 1
    max_nodes = pow(2, height + 1) - 1
    sum_output_array = [0] * max_nodes
    min_output_array = list(sum_output_array)
    max_output_array = list(sum_output_array)
    construct_sum_segment_tree(1, length, array, sum_output_array, 1)
    no_of_queries = int(raw_input("Enter the number of queries: "))
    print "Enter queries in the format: query_type start_range end_range update_val(if query type is update)\n%s" %string
    for _ in xrange(no_of_queries):
        query = raw_input("enter the query:")
    # construct_min_segment_tree(1, length, array, min_output_array, 1)
    # construct_max_segment_tree(1, length, array, max_output_array, 1)


    print sum_output_array
    print min_output_array
    print max_output_array
