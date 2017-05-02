#!/bin/sh

cut -f1 hightemp.txt > a.txt
cut -f2 hightemp.txt > b.txt

diff a.txt col1.txt
diff b.txt col2.txt

rm a.txt
rm b.txt
