rm -rf dist build *.egg-info
venv/bin/pip install build wheel twine
venv/bin/python -m build