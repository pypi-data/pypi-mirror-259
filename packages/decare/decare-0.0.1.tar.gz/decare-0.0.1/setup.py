from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="decare",
    version='0.0.1',
    author="Likeyi",
    author_email="lky23@mails.tsinghua.edu.cn",
    description="Detection of spatial chromatin accessibility patterns with inter-cellular correlations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/likeyi19/Descartes",
    packages=find_packages(),
    install_requires=[
        'anndata >= 0.9.2',
        'matplotlib >= 3.7.4',
        'numpy >= 1.22.4',
        'pandas >= 1.4.3',
        'scanpy == 1.9.6',
        'scikit-learn >= 1.3.0',
        'scipy >= 1.8.0',
        'seaborn >= 0.12.2',
        ],
)
