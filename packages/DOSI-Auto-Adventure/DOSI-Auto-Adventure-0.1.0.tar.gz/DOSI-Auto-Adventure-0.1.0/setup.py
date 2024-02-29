from setuptools import setup, find_packages

setup(
    name='DOSI-Auto-Adventure',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'dosi-auto-adventure = dosi:dosi_main',
        ],
    },
    author='monkeybosking',
    author_email='monkeybosking55@gmail.com',
    description='Simple Auto Adventure for DOSI platform',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/OniCrypto/DOSI',
    license='MIT',
)
