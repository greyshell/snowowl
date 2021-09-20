# Guideline
```
# install dependencies
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
pip install bumpversion

# get the virtual env information
poetry env info

# add the dev dependency
poetry add -D pytest

# add the project dependency
poetry add <package_name>

# installing the build dependency
poetry install  

# run the pytest
cd tests/
poetry run pytest test_heap.py

# freeze the requirements
pip freeze > requirements.txt

# commit before bumping up the version
git commit -am "message"

# git push

# bump up the version
bumpversion major

# build project
poetry build

# publish project
poetry publish
```