#!/usr/bin/python

# quicksort
# Pick a pivot, return cat(less-than-pivot,pivot,greater-than-pivot)
# Pivot can be first element, but that sucks for sorted lists
# O(nLogn)

def quicksort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    less_than_pivot = []
    greater_than_pivot = []
    for i in data[1:]:
        if i < pivot:
            less_than_pivot.append(i)
        else:
            greater_than_pivot.append(i)

    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

if __name__ == "__main__":
    data = [12,4,1,4,6,7]
    print "quicksorting %s" % data
    print quicksort2(data)
