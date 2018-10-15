#!/usr/bin/env python3

import sys

cur_topic = -1
last_doc = 'foo'

for line in sys.stdin:
    line = line.rstrip()
    (topic, q0, docno, rank, sim, runtag) = line.split()
    if cur_topic != topic:
        cur_topic = topic
        print(line)
        continue
    elif docno == last_doc:
        continue
    else:
        last_doc = docno
        print(line)
    
