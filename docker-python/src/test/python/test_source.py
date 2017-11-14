
import os
from source import Source


def test_source():
    pef_home = os.getcwd() + '/..'
    os.putenv('pef_home', pef_home)

    # needs python 3

    asource = Source('src/test/env/env.sh')
    assert 'some env' in asource.atestenv
    assert 'some env2' in asource.atestenv2

if __name__ == '__main__':
    test_source()