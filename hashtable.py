#!/usr/bin/env python

import hashlib

# Key/value getter/setter using an array

class HashTable(object):
    def __init__(self):
        self.array = []
        self.array_length = 2
        for i in range(self.array_length):
            self.array.append([])

    def get(self, k):
        values = self.array[self.hash(k)]
        for i in values:
            if i[0] == k:
                return i[1]

    def set(self, k, v):
        self.array[self.hash(k)].append([k,v])
        return v

    def hash(self, data):
        return int(hashlib.md5(data).hexdigest(), 16) % self.array_length

	
if __name__ == "__main__":
    data = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3',
        'key4': 'value4',
        'key5': 'value5',
        'key6': 'value6',
        'key7': 'value7'
    }
    ht = HashTable()
    for k,v in data.iteritems():
        print 'get(): %s' % ht.get(k)
        print 'set(): %s' % ht.set(k, v)
        print 'get(): %s' % ht.get(k)
