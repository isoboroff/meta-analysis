COLL = nyt
ATIRE_BIN = /Users/soboroff/atire/atire-hgtip/bin
TREC_EVAL = /Users/soboroff/trec_eval/trec_eval.github/trec_eval

all: no_stem.$(COLL).eval \
	krovetz.$(COLL).eval \
	prf.$(COLL).eval

%.eval: %.run
	$(TREC_EVAL) -q -M1000 qrels $< > $@

%.run: %.atire
	cat $< | sed 's/\/.*\///' | sed 's/\.xml//' | sed "s/unknown/$*/" > $@

# I don't want this to run even by accident
index.aspt :
	$(ATIRE_BIN)/index -sa -N10000 -r -Cz -findex index.aspt '/Users/soboroff/nyt_corpus/data/*/*/*/*xml'

topics qrels : truth_data_nyt_2017_v2.3.xml
	./convert-xml.py truth_data_nyt_2017_v2.3.xml topics qrels

no_stem.$(COLL).atire : topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -QN:t -q topics -l1000 -et -o$@

krovetz.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -QN:t -q topics -l1000 -et -o$@ -tk

porter.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -QN:t -q topics -l1000 -et -o$@ -tXe

prf.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -QN:t -Qr:20:50 -q topics -l1000 -et -o$@
