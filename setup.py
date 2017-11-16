from setuptools import setup

VERSION = open('VERSION').read().strip()
with open('requirements.txt') as f:
    INSTALL_REQUIRES = f.read().splitlines()
with open('requirements.txt') as f:
    TEST_REQUIRES = f.read().splitlines()
with open('LICENSE') as f:
    LICENSE = f.read()
with open('README.rst') as f:
    README = f.read()

setup(
    name='NYC-Countdown-Clock',
    version=VERSION,
    author='Shawn Tolidano',
    author_email='shawn@tolidano.com',
    packages=['nyc_countdown_clock'],
    url='https://github.com/tolidano/nyc-countdown-clock',
    download_url='https://github.com/toliadno/nyc-countdown-clock/tarball/%s' % VERSION,
    license=LICENSE,
    description='Countdown clock for mass transit options in NYC',
    keywords="nyc mass transit countdown clock schedule subway bus",
    long_description=README,
    package_data={'': ['README.rst']},
    install_requires=INSTALL_REQUIRES,
    tests_require=TEST_REQUIRES,
    test_suite='nyc_countdown_clock/test',
    entry_points={
        'console_scripts': ['nyctcd=nyc_countdown_clock.cli:run_cli'],
    },
    classifiers=[
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.2',
      'Programming Language :: Python :: 3.3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Development Status :: 3 - Alpha',
      'License :: Freely Distributable',
      'Natural Language :: English',
      'Operating System :: OS Independent',
      'Topic :: Utilities',
    ],
)
