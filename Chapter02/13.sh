#!/bin/sh

paste col1.txt col2.txt > diff.txt
diff diff.txt col3.txt
rm diff.txt
