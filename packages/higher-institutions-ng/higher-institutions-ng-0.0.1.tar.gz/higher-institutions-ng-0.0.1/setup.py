from setuptools import setup, find_packages
import io

with io.open('README.md', 'r', encoding='utf-8') as f:
    readme_content = f.read()

setup(
    name='higher-institutions-ng',
    version='0.0.1',
    packages=find_packages(exclude=["tests"]),
    author='Awesome Goodman',
    author_email='goodman.awesome@gmail.com',
    description='Information about Nigerian higher institutions.',
    long_description=readme_content,
    long_description_content_type='text/markdown',
    keywords=[
    "Nigerian School List",
    "Nigerian Schools",
    "Nigerian Colleges",
    "Nigerian Universities",
    "Nigerian Polytechnics",
    "Nigerian Higher Institutions",
    "State", 
    "Federal",
    "Nigeria"
  ],
    url='https://github.com/awesomegoodman/higher-institutions-ng.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        "Intended Audience :: Developers",
        'Operating System :: OS Independent',
    ],
    install_requires=[],
    exclude=[".pre-commit-config.yaml", "mypy.ini"]
)
