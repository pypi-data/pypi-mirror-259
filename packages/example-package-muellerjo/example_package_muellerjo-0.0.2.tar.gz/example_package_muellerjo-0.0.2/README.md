# dl_PyPI

Minimal Example for generating public libraries

# Generating distribution archives

```
py -m pip install --upgrade build
```

```
py -m build
```

# Uploading the distribution archives

```
py -m pip install --upgrade twine
```


```
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```

You will be prompted for a username and password. For the username, use __token__. For the password, use the token value, including the pypi- prefix.



After the command completes, you should see output similar to this:

```
Uploading distributions to https://test.pypi.org/legacy/
Enter your username: __token__
Uploading example_package_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.2/8.2 kB • 00:01 • ?
Uploading example_package_YOUR_USERNAME_HERE-0.0.1.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.8/6.8 kB • 00:00 • ?
```

Once uploaded, your package should be viewable on TestPyPI; for example:
https://test.pypi.org/project/example_package_YOUR_USERNAME_HERE.