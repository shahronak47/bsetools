from setuptools import setup

setup(
    name='bsetools',
    version='0.1.1',
    packages=['bsetools'],
    url='https://github.com/shahronak47/bsetools',
    license='MIT',
    author='Ronak Shah',
    author_email='shahronak47@yahoo.in',
    description='Get BSE quotes',
    install_requires=[
          'beautifulsoup4',
          'Google-Search-API',
          'selenium'
    ],
)
