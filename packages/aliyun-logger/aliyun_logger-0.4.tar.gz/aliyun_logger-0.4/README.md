# build
python setup.py sdist bdist_wheel

# publish
twine upload --config-file .pypirc dist/*