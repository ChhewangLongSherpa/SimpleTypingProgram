# -*- coding: utf-8 -*-
from urllib2 import urlopen
from argsParseSimple import *


#Web-Based Portion
def linkCheck(key):
    link = oneArgParse(key)
    if link is None or "":
        link = askForInput("{}?".format(link))
    return link


def urlRead(link):
    uf = urlopen(link)
    html = uf.read()
    return html
