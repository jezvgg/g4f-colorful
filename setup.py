from setuptools import setup

setup(
    name='gpt',
    version='0.1.0',
    py_modules=['gpt',
                'prettier'],
    install_requires=[
        'Click',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'gpt = gpt:ask_gpt',
        ],
    },
)