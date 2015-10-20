#!/usr/bin/env python

__description__ = 'Recover JPEG files'
__author__ = 'Didier Stevens'
__version__ = '0.0.1'
__date__ = '2015/10/12'

"""

Source code put in public domain by Didier Stevens, no Copyright
https://DidierStevens.com
Use at your own risk

History:
  2015/10/12: start

Todo:
"""

import optparse
import textwrap
import os

def PrintManual():
    manual = '''
Manual:

To be written
'''
    for line in manual.split('\n'):
        print(textwrap.fill(line))

def File2String(filename):
    try:
        f = open(filename, 'rb')
    except:
        return None
    try:
        return f.read()
    finally:
        f.close()

def String2File(string, filename):
    try:
        f = open(filename, 'wb')
    except:
        return None
    try:
        return f.write(string)
    finally:
        f.close()

def Recover(currentDir, filename, rootname):
    content = File2String(os.path.join(currentDir, filename))
    if content == None:
        return 0
    position = content.find('\xFF\xDB\x00\xC5')
    if position == -1:
        return 0
    if String2File('\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46\x00\x01\x01\x01\x00\x48\x00\x48\x00\x00' + content[position:], os.path.join(currentDir, rootname + '.jpg')):
        return 0
    return 1

def RecoverJpegFiles(options):
    currentDir = '.'
    suffix = '.jpg.id-9737394708_help2015@mail.bg'
    countFiles = 0
    countFilesDecoded = 0
    for filename in os.listdir(currentDir):
        if os.path.isfile(os.path.join(currentDir, filename)) and filename.endswith(suffix):
            countFiles += 1
            countFilesDecoded += Recover(currentDir, filename, filename[:-len(suffix)])
    print('Files read: %d' % countFiles)
    print('Jpegs recovered: %d' % countFilesDecoded)
    print('press <RETURN> to terminate')
    raw_input()

def Main():
    oParser = optparse.OptionParser(usage='usage: %prog [options] file\n' + __description__, version='%prog ' + __version__)
    oParser.add_option('-m', '--man', action='store_true', default=False, help='Print manual')
    (options, args) = oParser.parse_args()

    if options.man:
        oParser.print_help()
        PrintManual()
        return

    if len(args) != 0:
        oParser.print_help()
        print('')
        print('  Source code put in the public domain by Didier Stevens, no Copyright')
        print('  Use at your own risk')
        print('  https://DidierStevens.com')
        return
    else:
        RecoverJpegFiles(options)

if __name__ == '__main__':
    Main()
