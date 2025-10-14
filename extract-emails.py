#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os, codecs
import re

def getFiles(path, filePaths=None):
    if filePaths is None:
        filePaths = []

    for fileName in sorted(os.listdir(path)):
        if fileName.startswith('.'):
            continue
        filePath = path + fileName 
        if os.path.isdir(filePath):
            getFiles(filePath + '/', filePaths)
        elif fileName == 'mbox':
            filePaths.append(filePath)
    return filePaths

SKIP = ('t-mobile.nl', '@petr.com', 'aliexpress.com', 'chase.com', 'kabk.nl', 'ikea.nl', 'zoom.us', 
    'notarisgouda.nl', 'booking.com', 'github.com', 'nsinternational.nl', 'linkedin.com', 
    'amnesty.nl', 'wetransfer.com', 'ebhlegal.nl', 'webhostingserver.nl', 'hcc.nl', 'coolblue.nl', )

SKIP_LENGTH = len('T0AFA69BJ.U0B4N2B50.506f72152497f09f7755173352c6955f')

PATH = '_newsletter/'
PATH = '/Volumes/Archiv-T2/TYPETR-Newsletter-Email-Addressen/'

XXXX = (

)
YEAR_PATHS = (
    'ARCHIVE 2004.mbox/',
    'ARCHIVE 2005-2015.mbox/',
    'ARCHIVE 2007/',
    'ARCHIVE 2008/',
    'ARCHIVE 2009/',
    'ARCHIVE 2010/',
    'ARCHIVE 2011/',
    'ARCHIVE 2012/',
    'ARCHIVE 2013/',
    'ARCHIVE 2014/',
    'ARCHIVE 2015/',
    'ARCHIVE 2016/',
    'ARCHIVE 2017/',
    'ARCHIVE 2018/',
    'ARCHIVE 2019/',
    'ARCHIVE 2020/',
    'ARCHIVE 2021/',
    'INBOX.mbox/',
    'SENT 2014.mbox/',

)
XXXX = (
)
emails = set()
emailLines = {}

# Regular expression for email matching
pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

def doSkip(email):
    for skip in SKIP:
        if skip in email.lower():
            return True
    if len(email) > SKIP_LENGTH:
        return True

    return False

def processLine(t, emails, emailLines):
    for lIndex, line in enumerate(t.split('\n')):

        if line.startswith('X-Sent-To'):
            continue
        if 'From:' in line or 'To:' in line:
            for email in re.findall(pattern, line):
                if doSkip(email):
                    continue
                emails.add(email)
                if email not in emailLines:
                    emailLines[email] = set()
                emailLines[email].add(line)

for yearPath in YEAR_PATHS:
    for mailPath in getFiles(PATH + yearPath):
        print('===', mailPath)
        f = codecs.open(mailPath, 'r')
        t = f.read()
        f.close()
        processLine(t, emails, emailLines)

f = codecs.open(PATH + 'emails.py', 'w', encoding='utf-8')
f.write(str(emails).replace("', '", "',\n'"))
f.close()

f = codecs.open(PATH + 'emailLines.py', 'w', encoding='utf-8')
f.write(str(emailLines).replace("', '", "',\n'"))
f.close()


print(len(emails))
