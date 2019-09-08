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
    version="0.0.1",
    author="Fernando Mezzabotta & Octavio Augusto Coria",
    author_email="octa.ac@gmail.com",
    description="An open source HTTP terminal client.",
    url="https://github.com/dev-lemon/httlemon",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    pymodules=['httlemon'],
    install_requires=install_requires,
    test_requires=test_requires,
    extras_require={
        'dev': dev_requires,
        'testing': test_requires,
    },
    entry_points={
        'console_scripts': [
            'httlemon=command.httlemon:httlemon'
        ]
    },
    packages=find_packages(),
)
