from setuptools import setup, find_packages

setup(
    name='mngdataclean',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    description='Text preprocessing package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Nagaganesh21/mngdataclean',
    author='Nagaganesh',
    author_email='mnagaganesh21@gmail.com',
    keywords=['text', 'preprocessing'],
    install_requires=[
        'spacy',
        'beautifulsoup4',
        'textblob'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
