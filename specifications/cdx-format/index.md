---
title: CDX File Format
type: strand
strand: cdx-format
---

A CDX file consists of individual lines of text, each of which summarizes a single web document.
The first line in the file is a legend for interpreting the data, and the following lines contain the data for referencing the corresponding pages within the host. The first character of the file is the field delimiter used in the rest of the file. This is followed by the literal "CDX" and then individual field markers as defined below.

The following is a sample from a CDX file:

~~~
CDX A b e a m s c k r V v D d g M n
0-0-0checkmate.com/Bugs/Bug_Investigators.html 20010424210551 209.52.183.152 0-0-0checkmate.com:80/Bugs/Bug_Investigators.html text/html 200 58670fbe7432c5bed6f3dcd7ea32b221 a725a64ad6bb7112c55ed26c9e4cef63 - 17130110 59129865 1927657 6501523 DE_crawl6.20010424210458 - 5750
0-0-0checkmate.com/Bugs/Insect_Habitats.html 20010424210312 209.52.183.152 0-0-0checkmate.com:80/Bugs/Insect_Habitats.html text/html 200 d520038e97d7538855715ddcba613d41 30025030eeb72e9345cc2ddf8b5ff218 - 47392928 145482381 4426829 15345336 DE_crawl3.20010424210104 - 6356
0-0-0checkmate.com/Hot/index.html 20010424212403 209.52.183.152 0-0-0checkmate.com:80/Hot/index.html text/html 200 52242643710547ff4ce2605ed03ed9e2 b06d037c06e7ffd7afc6db270aca7645 - 21301376 62305547 1855363 6627262 DE_crawl6.20010424212307 - 6317
~~~

Data Specifications
-------------------

The default first line of a CDX file is:

~~~
CDX A b e a m s c k r V v D d g M n
~~~

The letters use in dat files and cdx files are as follows:

~~~
A canonized url
B news group
C rulespace category ***
D compressed dat file offset
F canonized frame
G multi-columm language description (* soon)
H canonized host
I canonized image
J canonized jump point
K Some weird FBIS what's changed kinda thing
L canonized link
M meta tags (AIF) *
N massaged url
P canonized path
Q language string
R canonized redirect
U uniqness ***
V compressed arc file offset *
X canonized url in other href tages
Y canonized url in other src tags
Z canonized url found in script
a original url **
b date **
c old style checksum *
d uncompressed dat file offset
e IP **
f frame *
g file name
h original host
i image *
j original jump point
k new style checksum *
l link *
m mime type of original document *
n arc document length *
o port
p original path
r redirect *
s response code *
t title *
v uncompressed arc file offset *
x url in other href tages *
y url in other src tags *
z url found in script *
# comment
~~~

\* in alexa-made dat file
\** in alexa-made dat file meta-data line
\*** future data
