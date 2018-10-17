COLL = gov2
INDEX = /mnt/gov2-index.aspt
ATIRE_BIN = /home/ubuntu/atire-hgtip/bin
TREC_EVAL = /home/ubuntu/trec_eval/trec_eval

VPATH=/mnt

all: no_stem.$(COLL).eval \
	krovetz.$(COLL).eval \
	prf.$(COLL).eval

%.eval: %.run
	$(TREC_EVAL) -q -M1000 $(QRELS) $< > $@

%.run: %.atire
	cat $< | sed "s/unknown/$*/" > $@

# I don't want this to run even by accident
# index.aspt :
#	$(ATIRE_BIN)/index -sa -N10000 -rtrec -findex index cd45-cr.sgml

TOPICS = 06.topics.701-850.txt
QRELS = qrels

qrels: 04.qrels.12-Nov-04 05.adhoc_qrels qrels.tb06.top50
	cat $^ > $@

.SECONDARY:

no_stem.$(COLL).atire : $(TOPICS) $(QRELS) $(INDEX)
	$(ATIRE_BIN)/atire -findex $(INDEX) -QN:t -q $(TOPICS) -l1000 -et -o$@

krovetz.$(COLL).atire: $(TOPICS) $(QRELS) $(INDEX)
	$(ATIRE_BIN)/atire -findex $(INDEX) -QN:t -q $(TOPICS) -l1000 -et -o$@ -tk

prf.$(COLL).atire: $(TOPICS) $(QRELS) $(INDEX)
	$(ATIRE_BIN)/atire -findex $(INDEX) -QN:t -Qr:20:50 -q $(TOPICS) -k1000 -l1000 -et -o$@
