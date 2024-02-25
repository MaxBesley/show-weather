from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as readme:
    LONG_DESCRIPTION = '\n' + readme.read()

DESCRIPTION = 'Tells you the weather of any city/town anywhere in the world over the command line'
VERSION = '0.1.0'


setup(
    name='show-weather',
    version=VERSION,
    author='Max Besley',
    author_email='<besleymax@gmail.com>',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    project_urls={
        'Repository': 'https://github.com/MaxBesley/show-weather-command',
        'Bug Tracker': 'https://github.com/MaxBesley/show-weather-command/issues'
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console'
    ],
    install_requires=['requests>=2.31.0'],
    packages=find_packages(),
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'show_weather = show_weather.show_weather:main'
        ]
    }
)
