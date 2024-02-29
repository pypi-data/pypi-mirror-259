How to generate a PIP package?
https://packaging.python.org/en/latest/tutorials/packaging-projects/

change setup.cfg version
py -m build
py -m twine upload --skip-existing dist/*