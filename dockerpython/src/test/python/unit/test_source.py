
import os
from pefspike.source import Source
from pefspike.db import Database


def test_source():
    pef_home = os.getcwd() + '/..'
    os.putenv('pef_home', pef_home)

    # needs python 3

    asource = Source('env/env.sh')
    assert 'some env' in asource.atestenv
    assert 'some env2' in asource.atestenv2

if __name__ == '__main__':
    test_source()
    print("Finished Test")
