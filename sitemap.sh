#!/bin/bash
wget --spider --recursive --no-verbose --output-file=wgetlog.txt http://silica-gel.org
sed -n "s@.\+ URL:\([^ ]\+\) .\+@\1@p" wgetlog.txt | sed "s@&@\&amp;@" > sedlog.txt
cat sedlog.txt |sort > sitemap.txt
wc sitemap.txt
rm sedlog.txt wgetlog.txt
diff sitemap.txt templates/sitemap.txt

