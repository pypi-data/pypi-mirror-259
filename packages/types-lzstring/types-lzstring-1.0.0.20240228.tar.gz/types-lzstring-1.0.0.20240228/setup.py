from setuptools import setup

name = "types-lzstring"
description = "Typing stubs for lzstring"
long_description = '''
## Typing stubs for lzstring

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`lzstring`](https://github.com/gkovacs/lz-string-python) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`lzstring`.

This version of `types-lzstring` aims to provide accurate annotations
for `lzstring==1.0.*`.
The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/lzstring. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `1f3cf143a528fe8febcbd02f7f5b24226e799dd6` and was tested
with mypy 1.8.0, pyright 1.1.342, and
pytype 2024.2.27.
'''.lstrip()

setup(name=name,
      version="1.0.0.20240228",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/lzstring.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['lzstring-stubs'],
      package_data={'lzstring-stubs': ['__init__.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      python_requires=">=3.8",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
