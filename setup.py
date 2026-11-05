from setuptools import setup

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='bpemb',
    version='0.3.6',
    description='Byte-pair embeddings in 275 languages',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prabeakarve/bpemb",
    author="prabeakarve",
    author_email="328289300+prabeakarve@users.noreply.github.com",
    license='MIT',
    packages=['bpemb'],
    install_requires=[
        "gensim",
        "numpy",
        "requests",
        "sentencepiece",
        "tqdm"],
    zip_safe=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3"
    ])
