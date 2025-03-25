from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    author='Conor C',
    description='A simple emotion detection wrapper using IBM Watson NLP',
)
