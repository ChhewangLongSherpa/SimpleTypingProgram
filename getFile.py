# -*- coding: utf-8 -*-
from urllib2 import urlopen
from argsParseSimple import *


def linkCheck(key):
    link = oneArgParse(key)
    if link is None or "":
        link = askForInput("{}?".format(link))
    return link


def getTextFrom(link):
    soup = BeauticulSoup(contents, 'html.parser')
    print soup.find_all('a')


def urlRead(link):
    uf = urlopen(link)
    html = uf.read()
    return html
