from setuptools import setup, find_packages

install_requires = [
    'click',
    'requests',
]
test_requires = [
    'coveralls',
    'pytest',
    'pytest-cov',
]
dev_requires = [
    'ipdb',
    'ipython',
] + test_requires


setup(
    name="httlemon",
    pymodules=['httlemon'],
    install_requires=install_requires,
    test_requires=test_requires,
    extras_require={
        'dev': dev_requires
    },
    entry_points={
        'console_scripts': [
            'httlemon=command.httlemon:httlemon'
        ]
    },
    version="0.1.0",
    packages=find_packages(),
)
