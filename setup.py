# Hack to prevent stupid error on exit of `python setup.py test`. (See
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html.)
try:
    import multiprocessing
except ImportError:
    pass

from setuptools import setup, find_packages


setup(
    name='django-subcommander',
    version='0.1',
    description='Write Django management commands that have subcommands.',
    long_description=open('README.rst').read(),
    author='Erik Rose',
    author_email='erikrose@grinchcentral.com',
    license='MIT',
    packages=find_packages(exclude=['ez_setup']),
    tests_require=['nose'],
    test_suite='nose.collector',
    url='https://github.com/votizen/django-subcommander',
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries'],
    keywords=['django', 'subcommand', 'command', 'nested', 'management']
)
