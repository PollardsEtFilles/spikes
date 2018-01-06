from setuptools import setup

setup(name='dockerpython',
      version='0.0.1',
      description='See environment variables easily in Python a bit like bash source',
      url='http://github.com/PollardsEtFilles/spikes',
      author='PEF Spike',
      author_email='spikes@pollardsetfilles.com',
      license='MIT',
      packages=['dockerpython.source', 'dockerpython.db'],
      zip_safe=False,
      install_requires=['mysql-connector-python-rf==2.2.2']
      )
