from setuptools import setup, find_packages

# Package metadata.
NAME = 'envease'
DESCRIPTION = 'A Python package to easily work with environment variables, inspired by the method used in Laravel framework to read the .env file.'
VERSION = '1.0.1'
AUTHOR = 'Alireza Abedini'
URL = 'https://github.com/Persian-Immortal/envutils'
LICENSE = 'MIT'
KEYWORDS = ['management', 'organizing', 'variables', 'variable', 'environment', 'environment variables', 'easy', 'simple', 'simplest', 'easiest']

# Long description from README.md file.
with open('README.md', 'r', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

with open('requirements.txt', 'r') as f:
    INSTALL_REQUIRES = [line.strip() for line in f if line.strip()]

# # Entry points, scripts, etc. might be available later
# ENTRY_POINTS = {
#     'console_scripts': [
#         'your_script_name = your_package.module:main_function',
#     ],
# }

# Setup function call.
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    url=URL,
    license=LICENSE,
    keywords=KEYWORDS,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    # entry_points=ENTRY_POINTS, # might be available later
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
