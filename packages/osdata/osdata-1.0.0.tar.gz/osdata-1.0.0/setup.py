from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="osdata",
    version="1.0.0",
    author='Osyris Technologies, Inc.',
    packages=find_packages(),
    install_requires=[
        'pandas', 'numpy', 'matplotlib', 'scikit-learn', 'segment-analytics-python~=2.3.2'
    ],
    # Additional metadata about your package.
    author_email="dev@osyris.io",
    description="A Universal SDK for discovering and analyzing research datasets",
    keywords=["osyris", "data", "dataset", "ai"],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
