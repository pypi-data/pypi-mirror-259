from setuptools import setup

name = "types-olefile"
description = "Typing stubs for olefile"
long_description = '''
## Typing stubs for olefile

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`olefile`](https://github.com/decalage2/olefile) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`olefile`.

This version of `types-olefile` aims to provide accurate annotations
for `olefile==0.47.*`.
The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/olefile. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `e05098681f326b98c635853a40287ac21f771fa2` and was tested
with mypy 1.8.0, pyright 1.1.350, and
pytype 2024.2.27.
'''.lstrip()

setup(name=name,
      version="0.47.0.20240301",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/olefile.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['olefile-stubs'],
      package_data={'olefile-stubs': ['__init__.pyi', 'olefile.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      python_requires=">=3.8",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
