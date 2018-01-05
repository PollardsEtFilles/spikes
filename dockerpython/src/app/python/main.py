#!/usr/bin/env python

from pefspike.source import Source


if __name__ == '__main__':
    print("hello world")
    asource = Source('env/env.sh')
    assert 'some env' in asource.atestenv
