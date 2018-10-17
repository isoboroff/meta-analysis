#!/usr/bin/env python3

from bs4 import BeautifulSoup as BS
import argparse

argparser = argparse.ArgumentParser(description='Convert DD XML topic file to old-school topic and qrels files',
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
argparser.add_argument('xml', help='Dynamic Domain format XML truth data file')
argparser.add_argument('topics', help='Name of topics file to output to', default='topics')
argparser.add_argument('qrels', help='Name of qrels file to output to', default='qrels')

args = argparser.parse_args()

xmlfile = BS(open(args.xml, 'r'), 'xml')
topicsfile = open(args.topics, 'w')
qrelsfile = open(args.qrels, 'w')

for topic in xmlfile.find_all('topic'):
    tid = topic.get('id').split('-')[-1]
    print('<top>', file=topicsfile)
    print('<num> Number:', tid, '</num>', file=topicsfile)
    print('<title> ', topic.get('name'), '</title>', file=topicsfile)
    print('<description> Description:', file=topicsfile)
    print(topic.description.get_text(), file=topicsfile)
    print('</description>', file=topicsfile)
    print('<narrative> Narrative:', file=topicsfile)
    print(topic.narrative.get_text(), file=topicsfile)
    print('</narrative>', file=topicsfile)
    print('</top>', file=topicsfile)

    qrels = dict()
    for psg in topic.find_all('passage'):
        docno = psg.docno.string
        rel = psg.rating.string
        if docno not in qrels:
            qrels[docno] = rel
        elif docno in qrels and qrels[docno] > rel:
            qrels[docno] = rel
    for docno, rel in qrels.items():
        print(tid, '0', docno, rel, file=qrelsfile)
        
            
