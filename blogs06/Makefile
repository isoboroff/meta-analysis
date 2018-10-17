COLL = blog06
INDEX = /mnt/blogs06-index.aspt
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

TOPICS = 06-08.all-blog-topics
QRELS = 08.qrels.opinion.all-topics

.SECONDARY:

no_stem.$(COLL).atire : $(TOPICS) $(QRELS) $(INDEX)
	$(ATIRE_BIN)/atire -findex $(INDEX) -QN:t -q $(TOPICS) -l1000 -et -o$@

krovetz.$(COLL).atire: $(TOPICS) $(QRELS) $(INDEX)
	$(ATIRE_BIN)/atire -findex $(INDEX) -QN:t -q $(TOPICS) -l1000 -et -o$@ -tk

prf.$(COLL).atire: $(TOPICS) $(QRELS) $(INDEX)
	$(ATIRE_BIN)/atire -findex $(INDEX) -QN:t -Qr:20:50 -q $(TOPICS) -l1000 -et -o$@

