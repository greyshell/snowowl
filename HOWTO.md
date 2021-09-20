# Guideline

- Install dependencies
```
 pyenv virtualenv 3.9.7 snowowl
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
pip install bumpversion
```

- Get the virtual env information
```
poetry env info
```

- Add the dev dependency
```
poetry add -D pytest
```

- Add the project dependency
```
poetry add <package_name>
```

- Installing the build dependency
```
poetry install  
```

- Run the pytest
```
cd tests/
poetry run pytest test_heap.py
```

- Freeze the requirements
```
pip freeze > requirements.txt
```

- Commit and push the code before bumping up the version
```
git commit -am "message"
git push
```

- Bump up the version
```
bumpversion major
```

- Build the project library
```
poetry build
```

- Publish the project
```
poetry publish
```