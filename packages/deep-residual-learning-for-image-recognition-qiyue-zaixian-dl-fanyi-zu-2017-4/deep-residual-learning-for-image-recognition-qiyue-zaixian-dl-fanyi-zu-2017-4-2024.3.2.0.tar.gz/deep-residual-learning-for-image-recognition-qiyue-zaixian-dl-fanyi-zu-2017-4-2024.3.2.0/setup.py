#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import DeepResidualLearningForImageRecognitionQiyueZaixianDlFanyiZu20174
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('DeepResidualLearningForImageRecognitionQiyueZaixianDlFanyiZu20174'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="deep-residual-learning-for-image-recognition-qiyue-zaixian-dl-fanyi-zu-2017-4",
    version=DeepResidualLearningForImageRecognitionQiyueZaixianDlFanyiZu20174.__version__,
    url="https://github.com/apachecn/deep-residual-learning-for-image-recognition-qiyue-zaixian-dl-fanyi-zu-2017-4",
    author=DeepResidualLearningForImageRecognitionQiyueZaixianDlFanyiZu20174.__author__,
    author_email=DeepResidualLearningForImageRecognitionQiyueZaixianDlFanyiZu20174.__email__,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: Other/Proprietary License",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Text Processing :: Markup :: Markdown",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Documentation",
        "Topic :: Documentation",
    ],
    description="Deep Residual Learning for Image Recognition（七月在线DL翻译组2017.4）",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "deep-residual-learning-for-image-recognition-qiyue-zaixian-dl-fanyi-zu-2017-4=DeepResidualLearningForImageRecognitionQiyueZaixianDlFanyiZu20174.__main__:main",
            "DeepResidualLearningForImageRecognitionQiyueZaixianDlFanyiZu20174=DeepResidualLearningForImageRecognitionQiyueZaixianDlFanyiZu20174.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
