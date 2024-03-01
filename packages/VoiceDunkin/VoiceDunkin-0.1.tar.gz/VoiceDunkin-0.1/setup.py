from setuptools import setup, find_packages

setup(
    name='VoiceDunkin',
    version='0.1',
    packages=find_packages(),
    install_requires=[line.strip() for line in open("requirements.txt").readlines()],
    entry_points={
        'console_scripts': [
            'VoiceDunkin=main:main_function',
        ],
    },
)
