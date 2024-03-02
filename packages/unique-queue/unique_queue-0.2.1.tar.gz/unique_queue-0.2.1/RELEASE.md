# Release

This is a guide to release this projec to PyPi.

## Prerequisites

```bash
# use a venv
pip install --upgrade pip
pip install --upgrade build twine
```

## Build and Deploy

```bash
python -m build
python -m twine upload --repository unique-queue dist/*
git tag v0.x.x
```
