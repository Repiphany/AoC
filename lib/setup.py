#!/usr/bin/env python3

import setuptools

setuptools.setup(
        name = 'aoc',
        version = '0.0.1',
        packages = ['aoc'],
        entry_points = {
            'console_scripts':[
                'aoc = aoc.__main__:main',
                ]
            },
        )
