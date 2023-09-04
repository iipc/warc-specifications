---
title: The CDX File Format
type: specification
status: proposed
version: (2015)
numbered: false
latest: true
version-of: cdx-format
previous-version: (c.2006)
---

> FWIW, IA has been using this 11-field format as pretty much standard for new > CDX files:
> 
>     CDX N b a m s k r M S V g
> 
> (You can see it as the default in their [CDX-Writer](https://github.com/internetarchive/CDX-Writer/blame/2e044a5719d45e46fdb5dbc21be3a1025e908143/cdx_writer.py#L862))
> 
> An older 9-field format that was in use a few years back:
> 
>     CDX N b a m s k r V g
> 
> I think most of the other fields are obsolete, and date back to an even older Alexa .dat format.

<pre>
CDX N b a m s k r M S V g
<a href="#N" title="N - massaged url">au,gov,financeminister)/</a> <a href="#b" title="b - date">20150914222034</a> <a href="#" title="a - original url">http://www.financeminister.gov.au/</a> <a href="#" title="m - mime type of original document">text/html</a> <a href="#" title="s - response code">200</a> <a href="#" title="k - new style checksum">ZMSA5TNJUKKRYAIM5PRUJLL24DV7QYOO</a> <a href="#" title="r - redirect">-</a> <a href="#" title="M - AIF meta tags">-</a> <a href="#" title="S - compressed record size">83848</a> <a href="#" title="V - compressed arc file offset">117273</a> <a href="#" title="g - file name">WEB-20150914222031256-00000-43190~heritrix.nla.gov.au~8443.warc.gz</a>
</pre>

----

A CDX file consists of individual lines of text, each of which summarizes a single web document.
The first line in the file is a legend for interpreting the data, and the following lines contain the data for referencing the corresponding pages within the host. The first character of the file is the field delimiter used in the rest of the file. This is followed by the literal "CDX" and then individual field markers as defined below.

The following is a sample from a CDX file:

~~~
CDX A b e a m s c k r V v D d g M n
0-0-0checkmate.com/Bugs/Bug_Investigators.html 20010424210551 209.52.183.152 0-0-0checkmate.com:80/Bugs/Bug_Investigators.html text/html 200 58670fbe7432c5bed6f3dcd7ea32b221 a725a64ad6bb7112c55ed26c9e4cef63 - 17130110 59129865 1927657 6501523 DE_crawl6.20010424210458 - 5750
0-0-0checkmate.com/Bugs/Insect_Habitats.html 20010424210312 209.52.183.152 0-0-0checkmate.com:80/Bugs/Insect_Habitats.html text/html 200 d520038e97d7538855715ddcba613d41 30025030eeb72e9345cc2ddf8b5ff218 - 47392928 145482381 4426829 15345336 DE_crawl3.20010424210104 - 6356
0-0-0checkmate.com/Hot/index.html 20010424212403 209.52.183.152 0-0-0checkmate.com:80/Hot/index.html text/html 200 52242643710547ff4ce2605ed03ed9e2 b06d037c06e7ffd7afc6db270aca7645 - 21301376 62305547 1855363 6627262 DE_crawl6.20010424212307 - 6317
~~~

Field Specifications
--------------------

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
G multi-column language description (* soon)
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
S compressed record size
U uniqueness ***
V compressed arc file offset *
X canonized url in other href tags
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

*   in alexa-made dat file
**  in alexa-made dat file meta-data line
*** future data
~~~

Document History
----------------

*2020-09-26* -- Minor, fixed some typos.

*2015-11-30* -- Added example CDX-11 record with tooltips and added 'S compressed record size' to the list.

*2015-07-10* -- Copied from v.2006 and added notes from [Ilya Kreymer](https://github.com/ikreymer).

*2015-07-09* -- Imported from the Internet Archive [CDX File Format](http://web.archive.org/web/20031226073353/http://www.archive.org/web/researcher/cdx_file_format.php) and [CDX Legend](http://web.archive.org/web/20031226073353/http://www.archive.org/web/researcher/cdx_legend.php) documents.
