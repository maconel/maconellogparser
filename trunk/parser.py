#!/usr/bin/env python

import time

class Log:
    def __init__(self):
        self.__file = None

    def __del__(self):
        if self.__file <> None:
            self.__file.close()
            self.__file = None

    def setLogFile(self, filename):
        self.__file = open(filename, 'rt')

    def readRecord(self):
        if self.__file == None:
            return None

        line = self.__file.readline()
        if len(line) == 0:
            return None

        fields = [f.strip().lstrip('[').rstrip(']') for f in line.split(' - ')]
        if len(fields) <> 4:
            return None

        r = Record()
        r._moduleName = fields[0]
        r._time = time.strptime(fields[1], '%Y-%m-%d %H:%M:%S')
        r._level = int(fields[2])
        r._content = fields[3]

        return r

class Record:
    def __init__(self):
        self._moduleName = None
        self._time = None
        self._level = None
        self._content = None

    def __str__(self):
        return ", ".join((self._moduleName, time.strftime('%Y-%m-%d %H:%M:%S', self._time), str(self._level), self._content))

if __name__ == '__main__':
    l = Log()
    l.setLogFile('20080827.log.test')
    print l.readRecord()
