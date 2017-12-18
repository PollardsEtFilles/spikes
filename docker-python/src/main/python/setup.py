from setuptools import setup

setup(name='pefspike',
      version='0.0.2',
      description='See environment variables easily in Python a bit like bash source',
      url='http://github.com/PollardsEtFilles/spikes',
      author='PEF Spike',
      author_email='spikes@pollardsetfilles.com',
      license='MIT',
      packages=['pefspike.source', 'pefspike.db'],
      zip_safe=False)
