from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Botte',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'requests',  # Required for the synchronous client
        'aiohttp',
        'openai',   # Required for the asynchronous client
    ],
    author='Avishek Bhattacharjee',
    author_email='wbavishek@gmail.com',
    description='The most easiest telegram package that helps you to code your bot faster',
)
