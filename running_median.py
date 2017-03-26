#!/usr/bin/python
#
# https://www.hackerrank.com/challenges/ctci-find-the-running-median

import sys
import heapq

class MaxWrap:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return other.val < self.val

class RunStore:
    def __init__(self):
        # max heap goes to the left , min heap goes to the right
        self.min_heap = []
        self.max_heap = []

    def add(self, val):
        if len(self.min_heap) <= 0:
            self.min_heap.append(val)

        else:
            if val >= self.min_heap[0]:
                heapq.heappush(self.min_heap, val)
            else:
                heapq.heappush(self.max_heap, MaxWrap(val))

        #print "---------- aded"
        #print "---- left %s" % [x.val for x in self.max_heap]
        #print "---- right %s" % self.min_heap

        if len(self.min_heap) - len(self.max_heap) > 1:
            popped_min = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, MaxWrap(popped_min))

        if len(self.max_heap) - len(self.min_heap) > 1:
            popped_max = heapq.heappop(self.max_heap).val
            heapq.heappush(self.min_heap, popped_max)

    def median(self):
        if len(self.max_heap) > len(self.min_heap):
            return float(self.max_heap[0].val)
        elif len(self.min_heap) > len(self.max_heap):
            return float(self.min_heap[0])

        return (float(self.max_heap[0].val) + self.min_heap[0]) / 2

store = RunStore()
n = int(raw_input().strip())

for a in xrange(n):
    val = int(raw_input().strip())
    store.add(val)
    print "%.1f" % store.median()
