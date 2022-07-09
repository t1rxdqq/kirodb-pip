from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='kiroDB',
    url='https://github.com/t1rxdqq',
    author='t1rxdqq',
    author_email='danilmerkulov63@gmail.com',
    # Needed to actually package something
    packages=['kirodb'],
    # Needed for dependencies
    install_requires=['requests','aiohttp','json'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Free cloudy database.',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)