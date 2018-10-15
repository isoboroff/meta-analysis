COLL = cd45
ATIRE_BIN = /Users/soboroff/atire/atire-hgtip/bin
TREC_EVAL = /Users/soboroff/trec_eval/trec_eval.github/trec_eval

all: no_stem.$(COLL).eval \
	krovetz.$(COLL).eval \
	porter.$(COLL).eval \
	prf-20-50.$(COLL).eval

prfs: prf-20-50.$(COLL).eval \
	prf-17-5.$(COLL).eval \
	prf-17-10.$(COLL).eval \
	prf-17-20.$(COLL).eval \
	prf-17-30.$(COLL).eval \
	prf-17-40.$(COLL).eval \
	prf-17-50.$(COLL).eval \
	prf-17-60.$(COLL).eval \
	prf-17-70.$(COLL).eval \
	prf-17-100.$(COLL).eval \
	prf-30-5.$(COLL).eval \
	prf-30-10.$(COLL).eval \
	prf-30-20.$(COLL).eval \
	prf-30-30.$(COLL).eval \
	prf-30-40.$(COLL).eval \
	prf-30-50.$(COLL).eval \
	prf-30-60.$(COLL).eval \
	prf-30-70.$(COLL).eval \
	prf-30-100.$(COLL).eval \
	prf-40-10.$(COLL).eval \
	prf-50-10.$(COLL).eval \
	prf-60-10.$(COLL).eval \
	prf-70-10.$(COLL).eval \
	prf-80-10.$(COLL).eval \
	prf-90-10.$(COLL).eval \
	prf-100-10.$(COLL).eval

models: model-tfidf.$(COLL).eval \
	model-lmd.$(COLL).eval \
	model-DLH13.$(COLL).eval \
	model-DFIW.$(COLL).eval \
	model-lmds.$(COLL).eval \
	model-kbtfidf.$(COLL).eval \
	model-TFlodop.$(COLL).eval \
	model-BM25ADPT.$(COLL).eval

lmp: lmp-plain.t.$(COLL).eval \
	lmp-tfidf.t.$(COLL).eval \
	lmp-plain.td.$(COLL).eval \
	lmp-tfidf.td.$(COLL).eval \
	lmp-plain.t.Qm.$(COLL).eval \
	lmp-tfidf.t.Qm.$(COLL).eval \
	lmp-plain.td.Qm.$(COLL).eval \
	lmp-tfidf.td.Qm.$(COLL).eval


%.eval: %.run
	$(TREC_EVAL) -q -M1000 qrels $< > $@

%.run: %.atire
	cat $< | ./force-dedupe.py | sed "s/unknown/$*/" > $@

index.aspt :
	$(ATIRE_BIN)/index -sa -N10000 -rtrec -findex index.aspt -Cz -kt cd45-cr.sgml

lmp.aspt :
	$(ATIRE_BIN)/index -sa -N10000 -rtrec -findex lmp.aspt -Ilmp -Cz -kt cd45-cr.sgml

lmptfidf.aspt :
	$(ATIRE_BIN)/index -sa -N10000 -rtrec -findex lmptfidf.aspt -Ilmptfidf -Cz -kt cd45-cr.sgml


topics: topics.301-350.gz topics.351-400.gz topics.401-450.gz
	gzip -dc $^ > $@

qrels: qrels.trec6 qrels.trec7 qrels.trec8
	cat $^ > $@

no_stem.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -QN:t -q topics -l1000 -et -o$@

krovetz.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -QN:t -q topics -l1000 -et -o$@ -tk

porter.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -QN:t -q topics -l1000 -et -o$@ -tXe

prf-20-50.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:20:50 -q topics -l1000 -et -o$@

prf-17-5.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:17:5 -q topics -l1000 -et -o$@

prf-17-10.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:17:10 -q topics -l1000 -et -o$@

prf-17-20.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:17:20 -q topics -l1000 -et -o$@

prf-17-30.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:17:30 -q topics -l1000 -et -o$@

prf-17-40.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:17:40 -q topics -l1000 -et -o$@

prf-17-50.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:17:50 -q topics -l1000 -et -o$@

prf-17-60.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:17:60 -q topics -l1000 -et -o$@

prf-17-70.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:17:70 -q topics -l1000 -et -o$@

prf-17-100.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:17:100 -q topics -l1000 -et -o$@

prf-30-5.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:30:5 -q topics -l1000 -et -o$@

prf-30-10.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:30:10 -q topics -l1000 -et -o$@

prf-30-20.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:30:20 -q topics -l1000 -et -o$@

prf-30-30.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:30:30 -q topics -l1000 -et -o$@

prf-30-40.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:30:40 -q topics -l1000 -et -o$@

prf-30-50.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:30:50 -q topics -l1000 -et -o$@

prf-30-60.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:30:60 -q topics -l1000 -et -o$@

prf-30-70.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:30:70 -q topics -l1000 -et -o$@

prf-30-100.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:30:100 -q topics -l1000 -et -o$@

prf-40-10.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:40:10 -q topics -l1000 -et -o$@

prf-50-10.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:50:10 -q topics -l1000 -et -o$@

prf-60-10.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:60:10 -q topics -l1000 -et -o$@

prf-70-10.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:70:10 -q topics -l1000 -et -o$@

prf-80-10.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:80:10 -q topics -l1000 -et -o$@

prf-90-10.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:90:10 -q topics -l1000 -et -o$@

prf-100-10.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25 -QN:t -Qr:100:10 -q topics -l1000 -et -o$@

model-tfidf.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -Rtfidf -QN:t -q topics -l1000 -et -o$@

model-lmd.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -Rlmd -QN:t -q topics -l1000 -et -o$@

model-DLH13.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RDLH13 -QN:t -q topics -l1000 -et -o$@

model-DFIW.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RDFIW -QN:t -q topics -l1000 -et -o$@

model-lmds.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -Rlmds -QN:t -q topics -l1000 -et -o$@

model-TFlodop.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RTFlodop -QN:t -q topics -l1000 -et -o$@

model-kbtfidf.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -Rkbtfidf -QN:t -q topics -l1000 -et -o$@

model-BM25ADPT.$(COLL).atire: topics qrels index.aspt
	$(ATIRE_BIN)/atire -findex index.aspt -RBM25ADPT -QN:t -q topics -l1000 -et -o$@

lmp-plain.t.$(COLL).atire: topics qrels lmp.aspt
	$(ATIRE_BIN)/atire -findex lmp.aspt -QN:t -Rlmp -q topics -l1000 -et -o$@

lmp-tfidf.t.$(COLL).atire: topics qrels lmptfidf.aspt
	$(ATIRE_BIN)/atire -findex lmptfidf.aspt -QN:t -Rlmp -q topics -l1000 -et -o$@

lmp-plain.td.$(COLL).atire: topics qrels lmp.aspt
	$(ATIRE_BIN)/atire -findex lmp.aspt -QN:td -Rlmp -q topics -l1000 -et -o$@

lmp-tfidf.td.$(COLL).atire: topics qrels lmptfidf.aspt
	$(ATIRE_BIN)/atire -findex lmptfidf.aspt -QN:td -Rlmp -q topics -l1000 -et -o$@

lmp-plain.t.Qm.$(COLL).atire: topics qrels lmp.aspt
	$(ATIRE_BIN)/atire -findex lmp.aspt -QN:t -Qm -Rlmp -q topics -l1000 -et -o$@

lmp-tfidf.t.Qm.$(COLL).atire: topics qrels lmptfidf.aspt
	$(ATIRE_BIN)/atire -findex lmptfidf.aspt -QN:t -Qm -Rlmp -q topics -l1000 -et -o$@

lmp-plain.td.Qm.$(COLL).atire: topics qrels lmp.aspt
	$(ATIRE_BIN)/atire -findex lmp.aspt -QN:td -Qm -Rlmp -q topics -l1000 -et -o$@

lmp-tfidf.td.Qm.$(COLL).atire: topics qrels lmptfidf.aspt
	$(ATIRE_BIN)/atire -findex lmptfidf.aspt -QN:td -Qm -Rlmp -q topics -l1000 -et -o$@
